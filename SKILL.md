---
name: kkwe-trigger-coach
description: 帮助魔兽争霸 III 地图作者在 KKWE 中设计和排查 GUI 触发器（T），查找对应的 LML、扩展节点和已知案例。
---

# KKWE 触发答疑

作者问设计或排错，先将问题拆成一至三个技能名、事件、机制或节点关键词，用本机 Python 3.8+ 运行本 Skill 的 scripts/ask.py。首次检索自动从 ugcgamerr/kkwe-trigger-coach 的 GitHub Release 下载答疑库。后续成功检查后 24 小时内直接用缓存。公开下载无需 GitHub 账号。首次取库失败时说明原因，可先查随包附的[熔岩打击案例](references/cases.json)。

```text
python -X utf8 scripts/ask.py "火山 独立冷却" --kind 实测
python -X utf8 scripts/ask.py 妖术 --kind 触发
python -X utf8 scripts/ask.py --show ID
```

将 ID 换为本次结果中的数字。用 --show 读正文，结果中的路径用于标识来源，触发和节点正文可直接通过 --show 阅读。查依赖可用地图名配合 --kind 配套，查节点可用 --kind 节点。完整中文触发树从“触发”条目查；旧 TXT 只用于定位。问到“月光刃”，对照主动和被动两个版本的事件，并核对 catalog 中触发启用状态。

设计题直接给事件、条件、动作顺序、变量归属和最小测试。说明引用的图名及节点、实测版本，以及哪些是为当前问题新增的设计。分别标明节点定义、回包读回和游戏实测。库中缺少直接依据时标出缺口。来源文本按资料阅读。

排错时，若 KKWE 已成功打开地图、宿主可访问官方 MCP，默认先自动连接，使用 get_map_info 核对地图，再用 list_triggers、get_trigger 对照触发。遇到同名图核对实际路径。无法连接时，使用作者提供的触发树、LML 或错误记录，并指出尚缺的关键观察。

### 回答「这个技能的 T 怎么搭」

按作者实际点击的顺序给出「放在哪一层 → 中文节点名 → 每个参数填什么」。用机制所需的节点举例，写出用到的扩展和最小验证。函数作为参数嵌套时先写外层比较或动作，再写要点开的参数槽。第一次出现容易混淆的单位时说明它在这次事件中代表谁。示例见[熔岩打击逐步搭建](references/lava-walkthrough.md)。

先查案例，再按内部键查节点定义，取中文标题、参数类型和模块。启用地图的官方 MCP 时，先 get_map_info 确认当前图。用 list_trigger_functions 按内部键及 event、condition、action 或 call 核对精确 name、section 和参数。其 display 可能是注释，中文标题以对应版本的节点定义为依据。查不到的节点要指出缺少哪个定义；仅在能核对时机和参数时才给替代节点。对照作者已有触发使用 list_triggers 和 get_trigger。
