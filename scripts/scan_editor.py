"""Read the active KKWE node catalogue and compare it with a local snapshot."""
import argparse
import hashlib
import json
import os
import sqlite3
import tempfile
import uuid
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, urlopen


class MCP:
    def __init__(self, url):
        address = urlsplit(url)
        if address.hostname not in ('127.0.0.1', 'localhost', '::1') or address.scheme != 'http':
            raise ValueError('请使用本机编辑器的 http MCP 地址。')
        self.url = url
        self.headers = {'Content-Type': 'application/json', 'Accept': 'application/json, text/event-stream'}
        self.counter = 0
        self.encoding_warnings = []
        self.info = self.request('initialize', {
            'protocolVersion': '2025-03-26', 'capabilities': {},
            'clientInfo': {'name': 'kkwe-trigger-coach', 'version': '1.1'}})
        self.request('notifications/initialized', notification=True)

    def request(self, method, params=None, notification=False):
        self.counter += 1
        body = {'jsonrpc': '2.0', 'method': method}
        if not notification:
            body['id'] = self.counter
        if params is not None:
            body['params'] = params
        data = json.dumps(body).encode('utf-8')
        with urlopen(Request(self.url, data=data, headers=self.headers), timeout=30) as response:
            session = response.headers.get('Mcp-Session-Id')
            if session:
                self.headers['Mcp-Session-Id'] = session
            if notification:
                return None
            if 'text/event-stream' in response.headers.get('Content-Type', ''):
                chunks = []
                for line in response:
                    line = self.decode(line, method, params).rstrip('\r\n')
                    if line.startswith('data:'):
                        chunks.append(line[5:].lstrip())
                    elif not line and chunks:
                        result = json.loads('\n'.join(chunks))
                        chunks = []
                        if result.get('id') == body['id']:
                            break
                else:
                    raise ValueError('MCP 数据流未返回本次请求的结果。')
            else:
                result = json.loads(self.decode(response.read(), method, params))
        if result.get('id') != body['id'] or 'error' in result:
            raise ValueError('MCP 请求失败：' + str(result.get('error', result)))
        return result['result']

    def decode(self, data, method, params):
        text = data.decode('utf-8', errors='surrogateescape')
        invalid = sum(0xDC80 <= ord(char) <= 0xDCFF for char in text)
        if invalid:
            self.encoding_warnings.append({'method': method, 'params': params, 'invalidBytes': invalid})
        return text

    def call(self, name, arguments):
        result = self.request('tools/call', {'name': name, 'arguments': arguments})
        if result.get('isError'):
            raise ValueError('读取失败：' + name + ' ' + str(result.get('content')))
        text = '\n'.join(c['text'] for c in result['content'] if c['type'] == 'text')
        return json.loads(text)


def semantic(record):
    """Exclude catalogue offsets, while preserving names and parameter definitions."""
    ignored = {'index', 'section_id', 'return_type_id', 'type_id'}
    if isinstance(record, dict):
        return {key: semantic(value) for key, value in record.items() if key not in ignored}
    if isinstance(record, list):
        return [semantic(value) for value in record]
    return record


def functions(call):
    entries = {}
    for section in ('event', 'condition', 'action', 'call'):
        offset = 0
        total = None
        while total is None or offset < total:
            page = call('list_trigger_functions', {'section': section, 'offset': offset, 'limit': 200})
            if total is None:
                total = page['total']
            if page['total'] != total or not isinstance(total, int) or total < 0:
                raise ValueError('扫描过程中目录数量发生变化，请重新扫描。')
            rows = page['functions']
            if not rows and offset < total:
                raise ValueError('节点目录分页不完整，本次扫描未保存。')
            for row in rows:
                key = section + '/' + row['name']
                if row['section'] != section or key in entries:
                    raise ValueError('节点目录分页重叠或分类不匹配。')
                entries[key] = semantic(row)
            offset += len(rows)
            if offset > total:
                raise ValueError('节点数量超过目录声明。')
    return entries


def compare(old, new):
    result = {}
    for category in ('functions', 'types', 'tools'):
        before = old[category]
        after = new[category]
        changed = {}
        for key in sorted(before.keys() & after.keys()):
            if before[key] != after[key]:
                changed[key] = {'before': before[key], 'after': after[key]}
        result[category] = {
            'added': sorted(after.keys() - before.keys()),
            'removed': sorted(before.keys() - after.keys()), 'changed': changed}
    return result


def write_json(path, value):
    with tempfile.NamedTemporaryFile(dir=path.parent, delete=False) as stream:
        temporary = Path(stream.name)
    try:
        # Escaped surrogate bytes retain malformed UTF-8 returned by the plugin.
        temporary.write_text(json.dumps(value, ensure_ascii=True, indent=2), 'utf-8')
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def scan(url, profile, cache):
    folder = cache / hashlib.sha256(profile.encode()).hexdigest()[:24]
    folder.mkdir(parents=True, exist_ok=True)
    lock = sqlite3.connect(folder / 'scan-lock.sqlite3', timeout=120)
    try:
        lock.execute('BEGIN IMMEDIATE')
        latest = folder / 'latest.json'
        old = json.loads(latest.read_text('utf-8')) if latest.exists() else None
        client = MCP(url)
        tools = {}
        cursor = None
        seen = set()
        while True:
            page = client.request('tools/list', {'cursor': cursor} if cursor else {})
            for tool in page['tools']:
                if tool['name'] in tools:
                    raise ValueError('MCP 工具目录分页重叠。')
                tools[tool['name']] = tool
            cursor = page.get('nextCursor')
            if not cursor:
                break
            if cursor in seen:
                raise ValueError('MCP 工具目录游标重复。')
            seen.add(cursor)
        for required in ('get_map_info', 'list_trigger_functions', 'list_trigger_types'):
            if required not in tools:
                raise ValueError('当前 MCP 缺少扫描能力：' + required)
        map_info = client.call('get_map_info', {})
        nodes = functions(client.call)
        types = {}
        for row in client.call('list_trigger_types', {}):
            if row['type'] in types:
                raise ValueError('参数类型目录重复。')
            types[row['type']] = semantic(row)
        current = {'format': 1, 'profile': profile, 'endpoint': url,
                   'checkedUTC': datetime.now(timezone.utc).isoformat(),
                   'serverInfo': client.info.get('serverInfo', {}),
                   'encodingWarnings': client.encoding_warnings,
                   'functions': nodes, 'types': types, 'tools': tools}
        changes = compare(old, current) if old else None
        revision = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid.uuid4().hex[:8]
        report = {'profile': profile, 'map': map_info.get('map_name'),
                  'firstScan': old is None, 'checkedUTC': current['checkedUTC'],
                  'previousUTC': old['checkedUTC'] if old else None,
                  'counts': {'functions': len(nodes), 'types': len(types), 'tools': len(tools)},
                  'changes': changes, 'snapshot': str(folder / (revision + '.json')),
                  'encodingWarningPages': len(client.encoding_warnings),
                  'report': str(folder / (revision + '-changes.json'))}
        write_json(Path(report['snapshot']), current)
        write_json(Path(report['report']), report)
        write_json(latest, current)
        return report
    finally:
        lock.close()


def main():
    parser = argparse.ArgumentParser(description='只读扫描当前 KKWE 的节点、类型和 MCP 工具定义。')
    parser.add_argument('url', help='从实际编辑器实例确认的本机 MCP 地址')
    parser.add_argument('--profile', required=True, help='同一 KKWE 安装目录使用固定标识，升级后沿用')
    base = os.environ.get('LOCALAPPDATA') or os.environ.get('XDG_CACHE_HOME') or Path.home() / '.cache'
    parser.add_argument('--cache', type=Path, default=Path(base) / 'kkwe-trigger-coach' / 'editor-scans')
    args = parser.parse_args()
    try:
        report = scan(args.url, args.profile, args.cache)
    except (OSError, ValueError, KeyError, TypeError, sqlite3.Error) as error:
        parser.exit(1, '扫描未完成，已有快照保留。' + str(error) + '\n')
    summary = {key: value for key, value in report.items() if key != 'changes'}
    if report['changes'] is not None:
        summary['differenceCounts'] = {category: {kind: len(value) for kind, value in changes.items()}
                                       for category, changes in report['changes'].items()}
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
