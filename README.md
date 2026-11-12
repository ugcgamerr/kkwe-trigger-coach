# KKWE 触发答疑 Skill

帮助魔兽争霸 III 地图作者设计与排查可展开的 GUI 触发树。默认样例为 [8×6 背包完整 GUI 树](references/bag48-gui.md)，包含变量、初始化、按键、鼠标、移动互换、丢弃、同步校验及逐格绘制。

## 安装

下载 [轻量安装包](https://github.com/ugcgamerr/kkwe-trigger-coach/releases/latest/download/kkwe-trigger-coach-lite.zip)（[备用地址](https://raw.githubusercontent.com/ugcgamerr/kkwe-trigger-coach/main/data/kkwe-trigger-coach-lite.zip)），解压后把整个 kkwe-trigger-coach 目录放进 AI 客户端的 Skill 目录，重新加载。需要本机 Python 3.8+。

已有安装需更新规则和脚本，数据库的按需更新另行运行。

## 答题前连接当前地图

先在 KKWE 打开目标地图。AI 使用当前实例的实际官方 MCP 地址连接，并由 get_map_info 确认地图。确认成功后先扫描当前节点定义，再检索案例和给出触发树。

下面将端口和安装标识换为实际值。

```powershell
python -X utf8 scripts/scan_editor.py http://127.0.0.1:实际端口/mcp --profile 该KKWE安装的固定标识
python -X utf8 scripts/ask.py 背包 --kind 实测 --editor-url http://127.0.0.1:实际端口/mcp
python -X utf8 scripts/ask.py --show ID --editor-url http://127.0.0.1:实际端口/mcp
```

检索入口在每次搜索和读取正文前检查MCP握手及地图确认。连接失败时会提示原因并停止。资料库按需下载，成功检查后的24小时内复用缓存，下载内容经过SHA-256和数据库完整性检查。

## GUI 样例

随包提供 [全部原始触发树](assets/bag48-gui/trigger/catalog.lml)、[中文展开树](references/bag48-gui.md)和[验收记录](references/bag48-verification.json)。功能逻辑10个触发器，另有1个测试场景触发器，合计284个GUI节点。2026-11-11单机测试中，作者确认纹理、B开关、移动、互换和拖到地面丢弃正常。多人联机和满包边界等项目在验收记录中保留待测状态。

案例库还保留26张演示图的目录、20张图导出的282份触发和节点及接口资料，使用时核对当前实例的版本、扩展、变量与物编依赖。
