# REA 集成：固定版本与实际覆盖

本仓库依赖 npm `rea-agents@6.3.0`，来源为 [morluto/rea](https://github.com/morluto/rea)。版本核对日期 2026-10-10；不把 stars、版本总数或“今天仍在更新”写成产品保证。

## 可直接使用的本地 CLI

Node 要求以 `package.json` 为准。`npm ci --ignore-scripts` 在当前仓库安装依赖，不修改 Agent 全局配置。Python wrapper 用 argv 调用本地 Node CLI，不执行字符串拼接的 shell 命令。

```text
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/run-001
python scripts/rea_bridge.py inspect-artifact /path/to/file --out outputs/run-002
python scripts/rea_bridge.py inspect-apk /path/to/game.apk --out outputs/run-003
python scripts/rea_bridge.py inspect-managed /path/to/game.dll --out outputs/run-004
```

输出目录必须不存在，避免覆盖前一轮证据。目录含 REA JSON、日志、执行回执和轻量索引；CLI 出错、超时和无法解析分别记录。成功只证明该工具返回了相应结果，尚需分析师解释覆盖范围。

| 路径 | 工具/前提 | 可证明什么 | 不能据此保证什么 |
|---|---|---|---|
| JavaScript/Electron | REA 静态应用分析 | 可读取模块、关系与证据位置 | 所有动态行为、后端或完整游戏逻辑 |
| APK | REA Android 工具，JADX/JDK 依当前版本检查 | Manifest、类与可反编译方法等 | 混淆/加固包一定可分析；全部原始资产 |
| .NET 程序集 | REA managed 静态工具 | 元数据、成员、CIL/原生边界 | 原始 C# 项目、完整 Unity 制作工程 |
| 原生二进制 | 已配置的 Ghidra/Hopper/IDA 与相应支持环境 | 伪码、汇编、符号、引用 | 原始完整源码或未知服务器规则 |
| 资源清点 | inspect-artifact，按实际格式接 UnityPy/AssetRipper | 物理文件及部分语义信息 | 一键获得完整美术 BOM、原创归属或制作成本 |
| 运行时/网络 | 精确目标、场景与允许的工具能力 | 本次实际观察到的行为 | 未观察路径；不得自动扩大到账号或线上服务 |

本轮实测结果见 [验证摘要](../evals/verification.md)。只在测试发生后更新该摘要，不把 upstream 能力表写成本机通过记录。

## MCP 是另一种入口

已经连接则使用当前服务器广告的工具和输入结构。需要新连接时可先运行 upstream 的 `setup --client codex --dry-run --json` 获取明确改动范围，再按用户授权安装；全局配置修改和可选原生引擎不是使用本仓库 CLI 的前置条件。[官方安装文档](https://rea.tools/get-started/)

附件里的“HADX”应为 JADX。“无源码 = 无资产”也不准确：某些包中能观察资源，但覆盖范围和可用权利需分别确认。不要从技术可读取推导可发布，亦不复述未经核验的笼统商店或法律结论。

REA 分析进程在本地，若 Agent 将证据提供给模型，仍适用宿主的数据处理方式；不能据“本地工具”宣称整个链路绝不外发。
