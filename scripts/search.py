"""Search the author's bundled reference material without external dependencies."""
import argparse
import sqlite3
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
KINDS = ("实测", "地图", "触发", "配套", "群问题", "节点", "KKAPI", "JASS", "资料", "旧文档")


def search(db, words, kind, limit):
    filters = ["kind = ?" if kind else "kind != '旧文档'"]
    params = [kind] if kind else []
    for word in words:
        filters.append("(instr(lower(title), lower(?)) > 0 OR instr(lower(body), lower(?)) > 0)")
        params.extend([word, word])
    title_score = " + ".join("(instr(lower(title), lower(?)) > 0)" for _ in words)
    sql = f"""SELECT rowid, kind, title, scope, path FROM entries
              WHERE {' AND '.join(filters)}
              ORDER BY ({title_score}) DESC,
                  CASE kind WHEN '实测' THEN 0 WHEN '地图' THEN 1 WHEN '触发' THEN 2 ELSE 3 END,
                  length(title), rowid LIMIT ?"""
    return db.execute(sql, [*params, *words, limit]).fetchall()


def main(database=None, kinds=KINDS):
    parser = argparse.ArgumentParser(description="按关键词查 KKWE 作者案例及原文件。多个词以空格分隔。")
    parser.add_argument("words", nargs="*")
    parser.add_argument("--kind", choices=kinds)
    parser.add_argument("--limit", type=int, default=8, choices=range(1, 101), metavar="1–100")
    parser.add_argument("--show", type=int, metavar="ID", help="查看本版索引中指定条目的全文")
    args = parser.parse_args()
    words = list(dict.fromkeys(w for arg in args.words for w in arg.split()))
    if not words and args.show is None:
        parser.error("请给出关键词或 --show ID")
    path = database() if database is not None else ROOT / "references" / "library.sqlite3"
    uri = path.as_uri() + "?mode=ro"
    db = sqlite3.connect(uri, uri=True)
    try:
        if args.show is not None:
            row = db.execute("SELECT kind,title,scope,path,body FROM entries WHERE rowid=?", (args.show,)).fetchone()
            if row is None:
                parser.exit(1, "该条目不存在。\n")
            print("\n".join(row))
        else:
            rows = search(db, words, args.kind, args.limit)
            for row_id, kind, title, scope, path in rows:
                print(f"[{row_id}] {kind} | {title} | {scope}\n    {path}")
            if not rows:
                print("未找到匹配条目。可改用技能名、事件或节点名再查。")
    finally:
        db.close()


if __name__ == "__main__":
    main()
