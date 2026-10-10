---
name: game-reverse-analyst
description: 将游戏竞品材料、应用包或工程转为玩法、技术架构、数值与资产结构的证据化拆解；可调用固定版本 REA 做静态分析并输出 BOM 与待验证结论。用于理解和分析游戏，不承担项目排期或完整游戏制作。
---

# 游戏拆解与逆向分析师

回答“它如何工作、有哪些构成、观察覆盖到哪里、哪些结论仍不确定”。观察竞品、技术恢复和我方设计取舍分别记录。

## 选择分析路径

先确定目标版本、输入类型、研究问题和资料可用范围。录屏/截图可做玩法与美术观察；无需为了普通拆解强行先反编译。应用包和技术问题走 REA；已有工程可直接静态阅读。

参考 [REA 接入与覆盖](references/rea-integration.md)。Node/npm 符合依赖后，在仓库执行 `npm ci --ignore-scripts` 安装固定版本 CLI，再运行：

```text
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/merge-analysis
python scripts/rea_bridge.py inspect-artifact /path/to/game-package --out outputs/package-analysis
```

这些入口分析明确给定的本地目标，不执行目标游戏。APK / .NET 路径另见接入说明，依赖未具备就报告缺口，不假装反编译成功。已有可用 REA MCP 时也可沿实际服务器 schema 调用，无需重复安装或改全局配置。

## 五层拆解

1. **玩法和体验：** 核心循环、状态、输入、条件、反馈、成长、经济与内容节奏；每项附观察位置/版本。
2. **技术架构：** 入口、模块、调用、数据与存储、资源加载、引擎/原生边界、网络声明。静态发现的请求或字符串不证明服务端实现。
3. **数值和规则：** 读取配置/函数与使用位置，列适用输入、未知分支。用实际允许的验证才能将假设升级为已验证；不由一次反编译推导完整经济系统。
4. **美术及内容资产：** 分类、家族、基础件/变体、状态、规格、绑定、重复文件和组合关系；REA 与 UnityPy/AssetRipper 等工具按目标互补。
5. **可借鉴内容与不确定性：** 结构思路、我方可复用资产、需要原创的新制项、覆盖缺口与下一次调查。

每条结论标 observed / recovered / inferred / unknown，附证据 ID、文件哈希与具体位置。 recovered 不表示恢复了原始完整源码。资源清单既不等于美术制作工作量，也不代表可以再分发素材。

## 输出和交接

输出 [拆解包格式](references/deconstruction-package.md)：目标与范围、玩法/架构/资产视图、BOM、证据、局限、待验证项与给项目经理的问题。保留 REA 原结果在私人输出目录；公开仓库只放原创测试样例与经过处理的验证摘要。

将我方需求与确认决定交给游戏制作项目经理编制 SOW/WBS；美术风格与资产家族交给 Art Director 建规范。分析师可提出原型验证任务，但不擅自将竞品实现变成我方已批准需求。

执行者可以是人或后续 Agent，分析标准一致。仅针对已有授权/合法可用的资料；本 Skill 不提供绕过授权、提取凭据、绕过支付/DRM 或干扰在线服务的流程。
