# 2048 开源源码 · 证据化拆解

[继续看：代码、算法、数值与美术 BOM 深挖](deep-dive.md)

[English](README.en.md) · [公开证据回执](public-receipt.json) · [英文看板](dashboard-en.png)

[![2048 开源源码拆解看板](dashboard-zh.png)](dashboard-zh.png)

**目标：** [gabrielecirulli/2048](https://github.com/gabrielecirulli/2048)，commit [`478b6ec346e3787f589e4af751378d06ded4cbbc`](https://github.com/gabrielecirulli/2048/commit/478b6ec346e3787f589e4af751378d06ded4cbbc)，MIT License。

**方法：** 用锁定版本的 REA 6.3.0 对干净源码导出做惰性 JavaScript 静态分析。目标没有被执行；没有访问账户、网络服务、DRM 或私有材料。

## 得到的结构

| 模块 | 职责 | 证据位置 |
|---|---|---|
| `application.js` | 以 4×4 网格装配输入、表现层和本地存储 | `js/application.js:2-3` |
| `game_manager.js` | 事件注册、状态恢复、移动、合并、计分、结束判定 | `js/game_manager.js:9-13, 35-58, 130-190` |
| `grid.js` / `tile.js` | 网格、方块、空位、边界和序列化 | `js/grid.js`, `js/tile.js` |
| `keyboard_input_manager.js` | 键盘与触控输入 | `js/keyboard_input_manager.js` |
| `html_actuator.js` | 通过 `requestAnimationFrame` 渲染网格、分数和状态 | `js/html_actuator.js` |
| `local_storage_manager.js` | 保存最高分与局面，并提供本地存储回退 | `js/local_storage_manager.js` |

## 可复核规则

- 新方块有 90% 概率为 2、10% 概率为 4：`game_manager.js:69-75`。
- 一个方块在一次遍历里只合并一次：`game_manager.js:155-170` 的 `!next.mergedFrom`。
- 得分增加合并后的方块值，达到 2048 标记胜利：`game_manager.js:166-174`。
- 成功移动后才生成新方块；没有空位和相邻同值方块时结束：`game_manager.js:177-190, 238-267`。
- 局面、分数、结束和继续状态会被序列化：`game_manager.js:79-109`。

## REA 回执

| 字段 | 值 |
|---|---|
| REA | `rea-agents@6.3.0` · JavaScript provider v1 |
| 执行模式 | 静态、惰性解析；`target_executed: false` |
| 规模 | 10 个 JS 模块 · 23 个节点 · 33 条关系 |
| Evidence ID | `ev_064ecb8d503c613d03e8b8b482ff090906c0f020c749dedaa60b1d900fc42c5f` |
| Root artifact SHA-256 | `998b95deaa367512690884041ddba58a52e8c236559e0fcdc119cfc57071eea6` |
| Output SHA-256 | `47a7fd180a4e3e88867a9a500a103d01903168f76458a327ae08c88244838c12` |

完整字段和关键输入哈希见 [`public-receipt.json`](public-receipt.json)。公开仓库只保留派生证据，完整 5.8 MB REA 输出仍在本地忽略目录中。

## 局限

静态关系只能说明候选结构，不能证明运行时顺序、频率或服务端行为。动态加载、反射、混淆和构建阶段生成的路径可能没有被恢复。本案例验证的是 JavaScript provider，不证明 APK、Unity、.NET 或原生程序分析可用。

该项目源码及名称归原作者；这里的用途是验证证据链和岗位工作流，不复制或重新发布目标源码。
