import sys

from library import ensure_library
from search import KINDS, ROOT, main
from scan_editor import MCP


def check_editor(url):
    try:
        client = MCP(url)
        info = client.call('get_map_info', {})
        if not isinstance(info, dict) or not info.get('map_name'):
            raise ValueError('get_map_info 未返回有效地图名称')
    except (OSError, ValueError, KeyError, TypeError) as error:
        raise RuntimeError('KKWE 官方 MCP 接入检查失败，请打开目标地图并核对实际端口。' + str(error)) from error
    print('KKWE MCP 已连接，当前地图为「' + info['map_name'] + '」。', file=sys.stderr)


def database():
    bundled = ROOT / 'references' / 'library.sqlite3'
    if bundled.is_file():
        return bundled
    return ensure_library(check_updates='--show' not in sys.argv[1:])


if __name__ == "__main__":
    try:
        main(database,
             kinds=tuple(k for k in KINDS if k != "群问题"), before_search=check_editor)
    except (OSError, ValueError, RuntimeError) as exc:
        sys.exit(str(exc))
