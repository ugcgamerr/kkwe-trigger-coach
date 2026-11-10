"""Fetch a release index once, then use the validated per-user copy."""
import gzip
import hashlib
import json
import os
import re
import sqlite3
import sys
import tempfile
import time
from pathlib import Path
from urllib.error import URLError
from urllib.request import urlopen


REPO = "ugcgamerr/kkwe-trigger-coach"
MANIFEST = "library-manifest.json"
INDEX = "library.sqlite3.gz"
MAX_DB = 128 * 1024 * 1024


def download(tag, asset, limit):
    release = "latest/download" if tag is None else "download/" + tag
    url = f"https://github.com/{REPO}/releases/{release}/{asset}"
    try:
        with urlopen(url, timeout=15) as response:
            data = response.read(limit + 1)
    except (URLError, TimeoutError):
        ref = tag or "main"
        mirror = f"https://raw.githubusercontent.com/{REPO}/{ref}/data/{asset}"
        with urlopen(mirror, timeout=30) as response:
            data = response.read(limit + 1)
    if len(data) > limit:
        raise ValueError("发布附件超过当前客户端支持的大小。")
    return data


def install(cache, manifest, fetch):
    tag = manifest["tag"]
    digest = manifest["sha256"]
    size = manifest["bytes"]
    if (manifest["format"] != 1 or not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,79}", tag)
            or not re.fullmatch(r"[0-9a-f]{64}", digest) or not 0 < size <= MAX_DB):
        raise ValueError("资料清单格式不受支持。")
    target = cache / (digest + ".sqlite3")
    if target.is_file() and target.stat().st_size == size:
        return target
    import io
    packed = fetch(tag, INDEX, MAX_DB)
    with gzip.GzipFile(fileobj=io.BytesIO(packed)) as stream:
        raw = stream.read(size + 1)
    if len(raw) != size or hashlib.sha256(raw).hexdigest() != digest:
        raise ValueError("资料大小或 SHA-256 校验失败。")
    with tempfile.NamedTemporaryFile(dir=cache, delete=False) as staged:
        tmp = Path(staged.name)
    try:
        tmp.write_bytes(raw)
        db = sqlite3.connect(tmp.as_uri() + "?mode=ro", uri=True)
        try:
            if db.execute("PRAGMA integrity_check").fetchone() != ("ok",):
                raise ValueError("数据库完整性检查失败。")
            db.execute("SELECT rowid,kind,title,scope,path,body FROM entries LIMIT 1").fetchone()
        finally:
            db.close()
        tmp.replace(target)
    finally:
        tmp.unlink(missing_ok=True)
    return target


def ensure_library(check_updates=True, *, cache=None, fetch=download, now=time.time):
    if cache is None:
        base = os.environ.get("LOCALAPPDATA") or os.environ.get("XDG_CACHE_HOME") or Path.home() / ".cache"
        cache = Path(base) / "kkwe-trigger-coach"
    cache.mkdir(exist_ok=True, parents=True)
    state = sqlite3.connect(cache / "versions.db", timeout=150)
    try:
        state.execute("BEGIN IMMEDIATE")
        state.execute("CREATE TABLE IF NOT EXISTS current (id INTEGER PRIMARY KEY, hash TEXT, checked REAL)")
        row = state.execute("SELECT hash,checked FROM current WHERE id=1").fetchone()
        old = cache / (row[0] + ".sqlite3") if row else None
        fallback = old is not None and old.is_file()
        if fallback and (not check_updates or 0 <= now() - row[1] < 86400):
            return old
        try:
            manifest = json.loads(fetch(None, MANIFEST, 8192))
            path = install(cache, manifest, fetch)
        except (OSError, RuntimeError, ValueError, EOFError, TypeError, KeyError, sqlite3.Error) as exc:
            if fallback:
                print(f"更新未完成，继续使用已有资料。{exc}", file=sys.stderr)
                return old
            raise RuntimeError(f"首次取库未成功。请确认可访问 {REPO} 的 Release，或使用完整离线包。{exc}") from exc
        state.execute("INSERT OR REPLACE INTO current VALUES(1,?,?)", (path.stem, now()))
        state.commit()
        return path
    finally:
        state.close()
