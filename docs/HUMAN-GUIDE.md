# 游戏拆解与逆向分析师 · 使用说明

[English](HUMAN-GUIDE.en.md)

从录屏、截图或授权工程开始，拆清规则、模块和资产关系。

## 准备资料

给 Agent 合法可用的资料，说明最想弄清的问题。
资料不齐也可以开始；影响下一步的缺项会单列，不以猜测填充。

## 先看玩法，不知道从哪里拆

> 使用 `$game-reverse-analyst`。这是游戏录屏和截图，先帮我梳理核心循环、状态变化和反馈。每条观察标明位置，把没有看见的部分列成问题。

玩法与体验视图、观察依据和待补材料。普通玩法观察可以直接从录屏开始。

## 我有授权工程，想追到实现

> 这是合法可用的 2048 工程。固定当前版本，找出输入、合并、计分、表现和存储模块，再把“一个方块一次只合并一次”追到源码位置。

系统 BOM、模块职责和规则位置；适合的目标由 REA 做静态分析，并保留分析证据与回执。

## 把拆解结果交给策划、程序和主美

> 整理一份拆解包：我们已发现什么、依据在哪里、还有什么不能确定。分别列出策划、程序和主美可以继续处理的问题，不替我们批准竞品方案。

按岗位可阅读的发现、证据索引、覆盖缺口与后续验证问题。

## 如何复核

录屏观察、工程静态阅读与应用包分析按问题选择，工具覆盖随目标变化。当前真实案例验证了 JavaScript 路径；APK、Unity、.NET 和原生程序需要各自的工具与证据。

仅分析合法可用的材料，不绕过 DRM、支付、凭据或访问控制。静态关系不证明运行时或服务端行为；素材清单不等于制作工时或再分发许可。

## 输出与交接

- **五层拆解：** 玩法、架构、规则与数值、资产结构、可借鉴点与未知。
- **证据索引：** 发现关联目标版本、文件位置和输入哈希。
- **岗位交接：** 哪些内容可以继续研究，哪些需要更多材料或实际验证。

[市场研究](https://github.com/NewenergyEric/game-market-intelligence)带来竞品与问题；分析师给结构与证据；[项目经理](https://github.com/NewenergyEric/game-production-manager)组织我方已确认工作；[Art Director](https://github.com/NewenergyEric/art-director-skill)将美术观察发展成我方规范与样板。

## 给 Agent 的技术入口

REA 固定为 6.3.0；Node 要求见 package.json。Python 桥接层有 7 项测试，覆盖无效证据、失败回执、超时、输入哈希与输出隔离。

```sh
npm ci --ignore-scripts
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/demo-analysis
```
