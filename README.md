[English](README.en.md)

# 游戏拆解与逆向分析师

### 看懂玩法，找到实现依据。

**从“看起来是这样”，走到“依据在这里”。**

把录屏、截图、合法可用的应用包或工程交给 Agent。它按问题拆解玩法、模块、规则和资产关系，把发现连到版本、文件位置与证据，让策划、程序和美术能继续研究。

<a href="assets/readme/hero-zh.mp4"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=workflow-v3">
  <img src="assets/readme/hero-zh.gif?v=workflow-v3" width="100%" alt="从录屏、截图或授权工程开始，拆清规则、模块和资产关系。">
</picture></a>

[24 秒，走完一次完整工作 · 播放 MP4](assets/readme/hero-zh.mp4) · [文字版](assets/readme/transcript-zh.md)

## 装好，然后直接说

在支持 Agent Skills 的工具中安装，例如 Codex、Claude Code 或 Cursor：

```sh
npx skills add https://github.com/NewenergyEric/game-reverse-analyst
```

把资料放进 Agent 能读取的文件夹，再说出要解决的问题。文件整理和命令由 Agent 处理。

### 先看玩法，不知道从哪里拆

> 使用 `$game-reverse-analyst`。这是游戏录屏和截图，先帮我梳理核心循环、状态变化和反馈。每条观察标明位置，把没有看见的部分列成问题。

**你会得到：** 玩法与体验视图、观察依据和待补材料。普通玩法观察可以直接从录屏开始。

### 我有授权工程，想追到实现

> 这是合法可用的 2048 工程。固定当前版本，找出输入、合并、计分、表现和存储模块，再把“一个方块一次只合并一次”追到源码位置。

**你会得到：** 系统 BOM、模块职责和规则位置；适合的目标由 REA 做静态分析，并保留分析证据与回执。

### 把拆解结果交给策划、程序和主美

> 整理一份拆解包：我们已发现什么、依据在哪里、还有什么不能确定。分别列出策划、程序和主美可以继续处理的问题，不替我们批准竞品方案。

**你会得到：** 按岗位可阅读的发现、证据索引、覆盖缺口与后续验证问题。

## 最后交给团队什么

- **五层拆解：** 玩法、架构、规则与数值、资产结构、可借鉴点与未知。
- **证据索引：** 发现关联目标版本、文件位置和输入哈希。
- **岗位交接：** 哪些内容可以继续研究，哪些需要更多材料或实际验证。

## 看一次真实拆解：2048 的合并规则

[2048 开源案例](case-studies/2048-open-source/README.md)固定到 MIT 授权的 commit `478b6ec`，用 REA 6.3.0 静态分析 10 个 JS 模块，记录 23 个节点和 33 条关系。

一个具体发现是 `!next.mergedFrom` 如何约束同次移动中的再次合并。规则位置、版本和完整哈希都在[公开回执](case-studies/2048-open-source/public-receipt.json)中。影片是源码规则示意，目标游戏没有被运行。

[![看一次真实拆解：2048 的合并规则](case-studies/2048-open-source/dashboard-zh.png?v=workflow-v3)](case-studies/2048-open-source/dashboard-zh.png)

## 和其他岗位一起用

[市场研究](https://github.com/NewenergyEric/game-market-intelligence)带来竞品与问题；分析师给结构与证据；[项目经理](https://github.com/NewenergyEric/game-production-manager)组织我方已确认工作；[Art Director](https://github.com/NewenergyEric/art-director-skill)将美术观察发展成我方规范与样板。

<details>
<summary><strong>安装要求、技术文档与验证</strong></summary>

REA 固定为 6.3.0；Node 要求见 package.json。Python 桥接层有 7 项测试，覆盖无效证据、失败回执、超时、输入哈希与输出隔离。

[人类详细说明](docs/HUMAN-GUIDE.md) · [Agent 调用说明](docs/AGENT-GUIDE.md) · [Skill 入口](SKILL.md) · [验证与审查](evals/)

```sh
npm ci --ignore-scripts
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/demo-analysis
```

[CI](https://github.com/NewenergyEric/game-reverse-analyst/actions) · [Motion source](motion/README.md)

</details>

<details>
<summary><strong>能力边界与资料使用</strong></summary>

录屏观察、工程静态阅读与应用包分析按问题选择，工具覆盖随目标变化。当前真实案例验证了 JavaScript 路径；APK、Unity、.NET 和原生程序需要各自的工具与证据。

仅分析合法可用的材料，不绕过 DRM、支付、凭据或访问控制。静态关系不证明运行时或服务端行为；素材清单不等于制作工时或再分发许可。

</details>

[MIT License](LICENSE) · 由 Eric 与 Agents 一起制作。
