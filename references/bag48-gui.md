# 8×6 背包 GUI 完整展开

依据2026-11-11测试实例的KKWE官方MCP回读生成，复用前核对当前实例。功能逻辑共10个触发器，另有1个测试场景触发器。11棵树共有284个GUI事件、条件和动作。自定义脚本为空。

鼠标和B键使用异步注册节点；发送者在本地用G48From/G48To组装请求，标签G48，正文为源格|目标格|物品句柄ID。接收回调通过实际发送玩家核对英雄归属和源物品。父键为英雄句柄ID，子键为1至48格号。

## 全部变量

|变量|类型|数组与索引|初值|
|---|---|---|---|
|G48HIndex|integer|否|0|
|G48HSlot|integer|否|0|
|G48Focus|frame|否|0|
|G48Button|frame|数组，1～48|0|
|G48Icon|frame|数组，1～48|0|
|G48PIndex|integer|否|0|
|G48PKey|integer|否|0|
|G48PItem|item|否|空|
|G48Texture|string|否|空|
|G48Selected|integer|否|0|
|G48Ready|boolean|否|FALSE|
|G48Hero|unit|数组，0～11|空|
|G48Items|hashtable|否|空|
|G48From|integer|否|0|
|G48To|integer|否|0|
|G48Pending|boolean|否|FALSE|
|G48SendItem|item|否|空|
|G48Open|boolean|否|FALSE|
|G48HeldSlot|integer|否|0|
|G48KeyHeld|boolean|否|FALSE|
|G48Panel|frame|否|0|
|G48DownX|integer|否|0|
|G48DownY|integer|否|0|
|G48ReleaseFrom|integer|否|0|
|G48DeltaX|integer|否|0|
|G48DeltaY|integer|否|0|
|G48Sender|player|否|空|
|G48SPlayer|integer|否|0|
|G48Data|string|否|空|
|G48Length|integer|否|0|
|G48SIndex|integer|否|0|
|G48First|integer|否|0|
|G48Second|integer|否|0|
|G48Source|integer|否|0|
|G48Target|integer|否|0|
|G48ItemID|integer|否|0|
|G48SHero|unit|否|空|
|G48SKey|integer|否|0|
|G48SItem|item|否|空|
|G48Other|item|否|空|
|G48UHero|unit|否|空|
|G48UItem|item|否|空|
|G48UPlayer|integer|否|0|
|G48UKey|integer|否|0|
|G48UIndex|integer|否|0|
|G48Free|integer|否|0|
|G48IIndex|integer|否|0|
|G48Col|integer|否|0|
|G48Row|integer|否|0|
|G48TestItem|item|否|空|

## 全部触发树

```text
G48Setup
├─ 事件
│  ├─ 游戏计时(单次)（0.1）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ <1.24> 新建哈希表（）
│  ├─ 设置变量（G48Items，最后创建的哈希表（））
│  ├─ 设置变量（G48Panel，新建Frame [Tag]（BACKDROP，G48Panel，原生 - 游戏UI（），，0））
│  ├─ 设置绝对位置（G48Panel，左上，0.12，0.5）
│  ├─ 设置大小（G48Panel，0.304，0.232）
│  ├─ 设置贴图（G48Panel，UI\Widgets\EscMenu\Human\blank-background.blp，0）
│  ├─ 使用整数变量 (做多项动作)（G48IIndex，1，48）
│  │  ├─ 动作
│  │  │  ├─ 设置变量（G48Col，模（算术运算 Lv2（G48IIndex，WESTRING_ARITHMETICOPERATOR_SUBTRACT，1），8））
│  │  │  ├─ 设置变量（G48Row，除 < ÷ > [New!]（算术运算 Lv2（G48IIndex，WESTRING_ARITHMETICOPERATOR_SUBTRACT，1），8））
│  │  │  ├─ 设置变量（G48Button[G48IIndex]，新建Frame [Tag]（BUTTON，连接字符串 Lv2（G48Button，转换整数为字符串（G48IIndex）），G48Panel，，0））
│  │  │  ├─ 设置相对位置（G48Button[G48IIndex]，左上，G48Panel，左上，算术运算 Lv2（0.01，WESTRING_ARITHMETICOPERATOR_ADD，算术运算 Lv2（0.036，WESTRING_ARITHMETICOPERATOR_MULTIPLY，转换整数为实数（G48Col））），算术运算 Lv2（-0.01，WESTRING_ARITHMETICOPERATOR_SUBTRACT，算术运算 Lv2（0.036，WESTRING_ARITHMETICOPERATOR_MULTIPLY，转换整数为实数（G48Row））））
│  │  │  ├─ 设置大小（G48Button[G48IIndex]，0.032，0.032）
│  │  │  ├─ 设置变量（G48Icon[G48IIndex]，新建Frame [Tag]（BACKDROP，连接字符串 Lv2（G48Icon，转换整数为字符串（G48IIndex）），G48Button[G48IIndex]，，0））
│  │  │  ├─ 移动所有锚点到Frame（G48Icon[G48IIndex]，G48Button[G48IIndex]）
│  ├─ 显示/隐藏（G48Panel，FALSE）
│  ├─ 注册 - 异步注册玩家按键事件（本地玩家 [R]（），点击，B）
│  │  ├─ 动作
│  │  │  ├─ 运行触发(无视条件)（gg_trg_G48BDown）
│  ├─ 注册 - 异步注册玩家按键事件（本地玩家 [R]（），释放，B）
│  │  ├─ 动作
│  │  │  ├─ 运行触发(无视条件)（gg_trg_G48BUp）
│  ├─ 注册 - 异步注册玩家鼠标事件（本地玩家 [R]（），点击，鼠标右键）
│  │  ├─ 动作
│  │  │  ├─ 运行触发(无视条件)（gg_trg_G48RightDown）
│  ├─ 注册 - 异步注册玩家鼠标事件（本地玩家 [R]（），释放，鼠标右键）
│  │  ├─ 动作
│  │  │  ├─ 运行触发(无视条件)（gg_trg_G48RightUp）
│  ├─ 设置变量（G48Ready，TRUE）
│  ├─ 运行触发(无视条件)（gg_trg_G48Paint）
```

```text
G48Hit
├─ 事件
│  └─ （空）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 设置变量（G48HSlot，0）
│  ├─ 设置变量（G48Focus，鼠标所在的Frame控件指针（））
│  ├─ 使用整数变量 (做多项动作)（G48HIndex，1，48）
│  │  ├─ 动作
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（转换 Frame 为 整数（G48Focus），等于，转换 Frame 为 整数（G48Button[G48HIndex]））
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置变量（G48HSlot，G48HIndex）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  └─ （空）
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（转换 Frame 为 整数（G48Focus），等于，转换 Frame 为 整数（G48Icon[G48HIndex]））
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置变量（G48HSlot，G48HIndex）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  └─ （空）
```

```text
G48Paint
├─ 事件
│  ├─ 游戏计时(循环)（0.05）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Ready，等于，FALSE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48PKey，<1.24> 获取对象的h2i值 [C]（G48Hero[玩家ID - 1 [R]（本地玩家 [R]（））]））
│  ├─ 使用整数变量 (做多项动作)（G48PIndex，1，48）
│  │  ├─ 动作
│  │  │  ├─ 设置变量（G48PItem，<1.24> 从哈希表提取物品 [C]（G48Items，G48PKey，G48PIndex））
│  │  │  ├─ 设置变量（G48Texture，UI\Widgets\Console\Human\human-inventory-slotfiller.blp）
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 物品（G48PItem，不等于，无物品）
│  │  │  │  │  ├─ 整数（指定物品的类型（G48PItem），不等于，0）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置变量（G48Texture，物品数据 (字符串) [JAPI]（指定物品的类型（G48PItem），1））
│  │  │  │  ├─ Else－动作
│  │  │  │  │  └─ （空）
│  │  │  ├─ 设置贴图（G48Icon[G48PIndex]，G48Texture，0）
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（G48PIndex，等于，G48Selected）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置透明度(0-255)（G48Icon[G48PIndex]，140）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  ├─ 设置透明度(0-255)（G48Icon[G48PIndex]，255）
│  ├─ 设置变量（G48PItem，无物品）
```

```text
G48BDown
├─ 事件
│  └─ （空）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48KeyHeld，等于，TRUE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48KeyHeld，TRUE）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Open，等于，TRUE）
│  │  ├─ Then－动作
│  │  │  ├─ 设置变量（G48Open，FALSE）
│  │  ├─ Else－动作
│  │  │  ├─ 设置变量（G48Open，TRUE）
│  ├─ 设置变量（G48Selected，0）
│  ├─ 设置变量（G48HeldSlot，0）
│  ├─ 显示/隐藏（G48Panel，G48Open）
│  ├─ 运行触发(无视条件)（gg_trg_G48Paint）
```

```text
G48BUp
├─ 事件
│  └─ （空）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 设置变量（G48KeyHeld，FALSE）
```

```text
G48RightDown
├─ 事件
│  └─ （空）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Open，等于，FALSE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Pending，等于，TRUE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 运行触发(无视条件)（gg_trg_G48Hit）
│  ├─ 设置变量（G48HeldSlot，0）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48HSlot，等于，0）
│  │  ├─ Then－动作
│  │  │  ├─ 设置变量（G48Selected，0）
│  │  ├─ Else－动作
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（G48Selected，大于，0）
│  │  │  │  │  ├─ 整数（G48Selected，不等于，G48HSlot）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置变量（G48From，G48Selected）
│  │  │  │  │  ├─ 设置变量（G48To，G48HSlot）
│  │  │  │  │  ├─ 运行触发(无视条件)（gg_trg_G48Send）
│  │  │  │  │  ├─ 设置变量（G48Selected，0）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  ├─ 如果（所有条件成立）
│  │  │  │  │  │  ├─ If－条件
│  │  │  │  │  │  │  ├─ 物品（<1.24> 从哈希表提取物品 [C]（G48Items，<1.24> 获取对象的h2i值 [C]（G48Hero[玩家ID - 1 [R]（本地玩家 [R]（））]），G48HSlot），不等于，无物品）
│  │  │  │  │  │  ├─ Then－动作
│  │  │  │  │  │  │  ├─ 设置变量（G48Selected，G48HSlot）
│  │  │  │  │  │  │  ├─ 设置变量（G48HeldSlot，G48HSlot）
│  │  │  │  │  │  │  ├─ 设置变量（G48DownX，获取鼠标游戏窗口坐标X（））
│  │  │  │  │  │  │  ├─ 设置变量（G48DownY，获取鼠标游戏窗口坐标Y（））
│  │  │  │  │  │  ├─ Else－动作
│  │  │  │  │  │  │  └─ （空）
│  ├─ 运行触发(无视条件)（gg_trg_G48Paint）
```

```text
G48RightUp
├─ 事件
│  └─ （空）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 设置变量（G48ReleaseFrom，G48HeldSlot）
│  ├─ 设置变量（G48HeldSlot，0）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Open，等于，FALSE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Pending，等于，TRUE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48ReleaseFrom，等于，0）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 运行触发(无视条件)（gg_trg_G48Hit）
│  ├─ 设置变量（G48DeltaX，算术运算 Lv2（获取鼠标游戏窗口坐标X（），WESTRING_ARITHMETICOPERATOR_SUBTRACT，G48DownX））
│  ├─ 设置变量（G48DeltaY，算术运算 Lv2（获取鼠标游戏窗口坐标Y（），WESTRING_ARITHMETICOPERATOR_SUBTRACT，G48DownY））
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48HSlot，大于，0）
│  │  │  ├─ 整数（G48HSlot，不等于，G48ReleaseFrom）
│  │  ├─ Then－动作
│  │  │  ├─ 设置变量（G48From，G48ReleaseFrom）
│  │  │  ├─ 设置变量（G48To，G48HSlot）
│  │  │  ├─ 运行触发(无视条件)（gg_trg_G48Send）
│  │  │  ├─ 设置变量（G48Selected，0）
│  │  ├─ Else－动作
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（G48HSlot，等于，0）
│  │  │  │  │  ├─ 整数（算术运算 Lv2（算术运算 Lv2（G48DeltaX，WESTRING_ARITHMETICOPERATOR_MULTIPLY，G48DeltaX），WESTRING_ARITHMETICOPERATOR_ADD，算术运算 Lv2（G48DeltaY，WESTRING_ARITHMETICOPERATOR_MULTIPLY，G48DeltaY）），大于等于，36）
│  │  │  │  │  ├─ 布尔表达式（硬件 - 当前游戏窗口是否活动窗口（），等于，TRUE）
│  │  │  │  │  ├─ 布尔表达式（鼠标是否在游戏内（），等于，TRUE）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置变量（G48From，G48ReleaseFrom）
│  │  │  │  │  ├─ 设置变量（G48To，0）
│  │  │  │  │  ├─ 运行触发(无视条件)（gg_trg_G48Send）
│  │  │  │  │  ├─ 设置变量（G48Selected，0）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  └─ （空）
│  ├─ 运行触发(无视条件)（gg_trg_G48Paint）
```

```text
G48Send
├─ 事件
│  └─ （空）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Pending，等于，TRUE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48From，小于，1）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48From，大于，48）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48To，小于，0）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48To，大于，48）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48From，等于，G48To）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48SendItem，<1.24> 从哈希表提取物品 [C]（G48Items，<1.24> 获取对象的h2i值 [C]（G48Hero[玩家ID - 1 [R]（本地玩家 [R]（））]），G48From））
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 物品（G48SendItem，不等于，无物品）
│  │  │  ├─ 整数（指定物品的类型（G48SendItem），不等于，0）
│  │  ├─ Then－动作
│  │  │  ├─ 设置变量（G48Pending，TRUE）
│  │  │  ├─ 同步游戏数据（G48，连接字符串 Lv2（连接字符串 Lv2（连接字符串 Lv2（连接字符串 Lv2（转换整数为字符串（G48From），|），转换整数为字符串（G48To）），|），转换整数为字符串（<1.24> 获取对象的h2i值 [C]（G48SendItem））））
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48SendItem，无物品）
```

```text
G48Sync
├─ 事件
│  ├─ 数据同步（G48，FALSE）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 设置变量（G48Sender，事件响应 - 获取同步数据的玩家（））
│  ├─ 设置变量（G48SPlayer，玩家ID - 1 [R]（G48Sender））
│  ├─ 设置变量（G48Data，事件响应 - 获取同步的数据（））
│  ├─ 设置变量（G48Length，字符串长度（G48Data））
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 玩家（G48Sender，等于，本地玩家 [R]（））
│  │  ├─ Then－动作
│  │  │  ├─ 设置变量（G48Pending，FALSE）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48SPlayer，小于，0）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48SPlayer，大于，11）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Length，大于，40）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48First，-1）
│  ├─ 设置变量（G48Second，-1）
│  ├─ 使用整数变量 (做多项动作)（G48SIndex，0，算术运算 Lv2（G48Length，WESTRING_ARITHMETICOPERATOR_SUBTRACT，1））
│  │  ├─ 动作
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 字符串（截取字符串 [R]（G48Data，G48SIndex，算术运算 Lv2（G48SIndex，WESTRING_ARITHMETICOPERATOR_ADD，1）），等于，|）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 如果（所有条件成立）
│  │  │  │  │  │  ├─ If－条件
│  │  │  │  │  │  │  ├─ 整数（G48First，等于，-1）
│  │  │  │  │  │  ├─ Then－动作
│  │  │  │  │  │  │  ├─ 设置变量（G48First，G48SIndex）
│  │  │  │  │  │  ├─ Else－动作
│  │  │  │  │  │  │  ├─ 如果（所有条件成立）
│  │  │  │  │  │  │  │  ├─ If－条件
│  │  │  │  │  │  │  │  │  ├─ 整数（G48Second，等于，-1）
│  │  │  │  │  │  │  │  ├─ Then－动作
│  │  │  │  │  │  │  │  │  ├─ 设置变量（G48Second，G48SIndex）
│  │  │  │  │  │  │  │  ├─ Else－动作
│  │  │  │  │  │  │  │  │  ├─ 跳过剩余动作（）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48First，小于，1）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Second，小于等于，算术运算 Lv2（G48First，WESTRING_ARITHMETICOPERATOR_ADD，1））
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Second，大于等于，算术运算 Lv2（G48Length，WESTRING_ARITHMETICOPERATOR_SUBTRACT，1））
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48Source，转换字符串为整数（截取字符串 [R]（G48Data，0，G48First）））
│  ├─ 设置变量（G48Target，转换字符串为整数（截取字符串 [R]（G48Data，算术运算 Lv2（G48First，WESTRING_ARITHMETICOPERATOR_ADD，1），G48Second）））
│  ├─ 设置变量（G48ItemID，转换字符串为整数（截取字符串 [R]（G48Data，算术运算 Lv2（G48Second，WESTRING_ARITHMETICOPERATOR_ADD，1），G48Length）））
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 字符串（G48Data，不等于，连接字符串 Lv2（连接字符串 Lv2（连接字符串 Lv2（连接字符串 Lv2（转换整数为字符串（G48Source），|），转换整数为字符串（G48Target）），|），转换整数为字符串（G48ItemID）））
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Source，小于，1）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Source，大于，48）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Target，小于，0）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Target，大于，48）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Source，等于，G48Target）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48SHero，G48Hero[G48SPlayer]）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 单位（G48SHero，等于，无单位）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 玩家（单位所有者（G48SHero），不等于，G48Sender）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 实数（属性 [R]（G48SHero，WESTRING_USTATE_LIFE），小于等于，0.405）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48SKey，<1.24> 获取对象的h2i值 [C]（G48SHero））
│  ├─ 设置变量（G48SItem，<1.24> 从哈希表提取物品 [C]（G48Items，G48SKey，G48Source））
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 物品（G48SItem，不等于，无物品）
│  │  │  ├─ 整数（指定物品的类型（G48SItem），不等于，0）
│  │  │  ├─ 整数（<1.24> 获取对象的h2i值 [C]（G48SItem），等于，G48ItemID）
│  │  ├─ Then－动作
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（G48Target，等于，0）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 清理哈希项存储的句柄 <new>（G48Items，G48SKey，G48Source）
│  │  │  │  │  ├─ 移动物品到坐标(立即)(指定坐标) [R]（G48SItem，单位所在X轴坐标 [R]（G48SHero），单位所在Y轴坐标 [R]（G48SHero））
│  │  │  │  │  ├─ 显示/隐藏 [R]（G48SItem，WESTRING_SHOWHIDE_SHOW）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  ├─ 设置变量（G48Other，<1.24> 从哈希表提取物品 [C]（G48Items，G48SKey，G48Target））
│  │  │  │  │  ├─ <1.24> 保存物品 [C]（G48Items，G48SKey，G48Target，G48SItem）
│  │  │  │  │  ├─ 如果（所有条件成立）
│  │  │  │  │  │  ├─ If－条件
│  │  │  │  │  │  │  ├─ 物品（G48Other，等于，无物品）
│  │  │  │  │  │  ├─ Then－动作
│  │  │  │  │  │  │  ├─ 清理哈希项存储的句柄 <new>（G48Items，G48SKey，G48Source）
│  │  │  │  │  │  ├─ Else－动作
│  │  │  │  │  │  │  ├─ <1.24> 保存物品 [C]（G48Items，G48SKey，G48Source，G48Other）
│  │  │  │  │  ├─ 设置变量（G48Other，无物品）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 运行触发(无视条件)（gg_trg_G48Paint）
│  ├─ 设置变量（G48SHero，无单位）
│  ├─ 设置变量（G48SItem，无物品）
```

```text
G48Pickup
├─ 事件
│  ├─ 任意单位事件（获得物品）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（G48Ready，等于，FALSE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48UHero，触发单位（））
│  ├─ 设置变量（G48UItem，被操作物品（））
│  ├─ 设置变量（G48UPlayer，玩家ID - 1 [R]（单位所有者（G48UHero）））
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48UPlayer，大于，11）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 布尔表达式（单位类别检查（G48UHero，WESTRING_UNITTYPE_HERO），等于，FALSE）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 物品分类（指定物品的分类（G48UItem），等于，WESTRING_ITEMTYPE_POWERUP）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 单位（G48Hero[G48UPlayer]，等于，无单位）
│  │  ├─ Then－动作
│  │  │  ├─ 设置变量（G48Hero[G48UPlayer]，G48UHero）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 单位（G48Hero[G48UPlayer]，不等于，G48UHero）
│  │  ├─ Then－动作
│  │  │  ├─ 跳过剩余动作（）
│  │  ├─ Else－动作
│  │  │  └─ （空）
│  ├─ 设置变量（G48UKey，<1.24> 获取对象的h2i值 [C]（G48UHero））
│  ├─ 设置变量（G48Free，0）
│  ├─ 使用整数变量 (做多项动作)（G48UIndex，1，48）
│  │  ├─ 动作
│  │  │  ├─ 如果（所有条件成立）
│  │  │  │  ├─ If－条件
│  │  │  │  │  ├─ 整数（G48Free，等于，0）
│  │  │  │  │  ├─ 物品（<1.24> 从哈希表提取物品 [C]（G48Items，G48UKey，G48UIndex），等于，无物品）
│  │  │  │  ├─ Then－动作
│  │  │  │  │  ├─ 设置变量（G48Free，G48UIndex）
│  │  │  │  ├─ Else－动作
│  │  │  │  │  └─ （空）
│  ├─ 丢弃物品(指定物品)（G48UItem，G48UHero）
│  ├─ 如果（所有条件成立）
│  │  ├─ If－条件
│  │  │  ├─ 整数（G48Free，大于，0）
│  │  ├─ Then－动作
│  │  │  ├─ <1.24> 保存物品 [C]（G48Items，G48UKey，G48Free，G48UItem）
│  │  │  ├─ 显示/隐藏 [R]（G48UItem，WESTRING_SHOWHIDE_HIDE）
│  │  ├─ Else－动作
│  │  │  ├─ 移动物品到坐标(立即)(指定坐标) [R]（G48UItem，单位所在X轴坐标 [R]（G48UHero），单位所在Y轴坐标 [R]（G48UHero））
│  │  │  ├─ 显示/隐藏 [R]（G48UItem，WESTRING_SHOWHIDE_SHOW）
│  ├─ 运行触发(无视条件)（gg_trg_G48Paint）
│  ├─ 设置变量（G48UHero，无单位）
│  ├─ 设置变量（G48UItem，无物品）
```

```text
G48Fixture
├─ 事件
│  ├─ 游戏计时(单次)（0.3）
├─ 条件
│  └─ （空）
├─ 动作
│  ├─ 设置变量（G48Hero[0]，新建单位(指定坐标) [R]（玩家1（红色），Hpal，0，0，270））
│  ├─ 设置变量（G48TestItem，新建物品 [R]（rat6，180，0））
│  ├─ 设置变量（G48TestItem，新建物品 [R]（rat9，240，0））
│  ├─ 设置变量（G48TestItem，新建物品 [R]（phea，300，0））
│  ├─ 平移镜头(指定玩家)(限时)（玩家1（红色），坐标点（0，0），0）
│  ├─ 选择单位(指定玩家)（G48Hero[0]，玩家1（红色））
│  ├─ 对玩家显示文本消息(指定时间) [R]（玩家1（红色），0，0，60，TRIGSTR_004）
```

本轮用户确认纹理、B开关、移动、互换和拖到地面丢弃正常。多人联机、满48格后的第49件、次数保留和聊天输入冲突尚待验证。
