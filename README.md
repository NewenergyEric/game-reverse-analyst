[English](README.en.md)

# 游戏拆解与逆向分析师

### 看懂玩法，找到实现依据。

从“它为什么这样运转”出发，连接玩法状态、代码与数据流、算法边界、数值参数、资产家族和表现层。录屏先回答可观察的问题；合法可用的工程或应用包再按覆盖能力深入。

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-zh.png?v=depth-v4">
  <img src="assets/readme/hero-zh.webp?v=depth-v4" width="100%" alt="沿着一条玩法规则，拆到代码、算法、数值与美术资产。">
</picture>

[播放完整介绍 · 24 秒 MP4](assets/readme/hero-zh.mp4) · [GIF](assets/readme/hero-zh.gif) · [文字版](assets/readme/transcript-zh.md)

## 装好，然后直接说

```sh
npx skills add https://github.com/NewenergyEric/game-reverse-analyst
```

在支持 Agent Skills 的工具中安装，例如 Codex、Claude Code、Cursor；将资料放进 Agent 能读取的位置，再描述问题。

### 追到代码和算法

> 这个 2048 为什么一次左移不能直接合成 8？给我调用路径、状态变化和可复核位置。

得到输入到存档的实现链、合并边界、源码版本与对应测试问题。

### 核对数值设计

> 新生 4 的概率改成 20%，会更难多少？先解释现有参数，告诉我哪些能算、哪些需要实验。

现有 90/10 概率与期望面值可复算；难度、胜率和分数分布需要玩家策略、种子与实际运行。

### 拆出美术和内容 BOM

> 11 种方块数值需要 11 张图吗？整理组件、状态、动效、字体与平台素材。

按 CSS 组件、数值变体、逻辑状态与文件分别计数，并提供原位置和制作影响。

## 看一个具体案例

**真实开源案例：2048，固定 commit 478b6ec。** 在已有 REA 6.3.0 静态回执之上，补充代码链、合并算法、生成概率、公式复算与资产 BOM；18 个输入文件的哈希已核验。

[完整分析与可下载底稿](case-studies/2048-open-source/deep-dive.md)

[![游戏拆解与逆向分析师](case-studies/2048-open-source/dashboard-zh.png?v=depth-v4)](case-studies/2048-open-source/dashboard-zh.png)

## 最后交给团队什么

- 代码、规则与数值 — `deep-dive.json`
- 美术资产与计数依据 — `asset-bom.csv`
- 输入哈希与公式复算 — `verification.json`

<details>
<summary>能力边界、说明书与验证</summary>

本案例没有运行目标游戏。源码推导、公式复算、运行验证分开标记。REA 的 JavaScript 案例不代表任意 APK、Unity 或原生游戏都已验证可拆解；录屏不能证明服务端算法。没有材料的数值、代码或资产层级保留未知。

核心工具使用 Python 3.10+ 标准库；动画源码是可选的 Remotion 工程。

[人类说明书](docs/HUMAN-GUIDE.md) · [Agent guide](docs/AGENT-GUIDE.md) · [SKILL.md](SKILL.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
