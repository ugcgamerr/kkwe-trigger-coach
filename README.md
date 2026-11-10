# KKWE 触发答疑 Skill

为魔兽争霸 III 地图作者提供中文触发器设计与排错参考。可以问“月光刃做成普攻被动和主动施放时，事件入口各怎么选？”

## 安装

下载[轻量安装包](https://github.com/ugcgamerr/kkwe-trigger-coach/releases/latest/download/kkwe-trigger-coach-lite.zip)（[备用下载](https://raw.githubusercontent.com/ugcgamerr/kkwe-trigger-coach/main/data/kkwe-trigger-coach-lite.zip)），解压后将整个 kkwe-trigger-coach 文件夹放入 AI 客户端支持的 Skill 目录，重新加载。需要本机可用的 Python 3.8 或以上，以及首次使用时能访问 GitHub。

第一次检索会自动下载公开答疑库。成功检查后的 24 小时内复用缓存，之后在提问时检查更新。新版数据库通过 SHA-256 和数据库完整性校验后启用。已有缓存时断网也可以使用。

## 试用

在 Skill 目录执行以下命令。将 ID 换成上一步显示的条目编号，可查看完整触发正文。

```powershell
python -X utf8 scripts/ask.py 月光刃 --kind 触发
python -X utf8 scripts/ask.py --show ID
```

首版包含 26 张演示图的目录、20 张图导出的 282 份触发、节点及 JASS / KKAPI 文档，并附「熔岩打击」单机实测案例。条目标注了结构核对与游戏实测的范围。地图二进制文件由作者另行取得。
