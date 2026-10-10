# Agent 使用说明 · game-reverse-analyst

[English](AGENT-GUIDE.md)

## 入口与读取顺序

先读 `SKILL.md`，再按目标读取 `references/rea-integration.md` 和 `references/deconstruction-package.md`。只有使用 REA 时才安装锁定的 npm 依赖；不要改全局 MCP 配置。

## 标准工作流

1. 写清目标、版本、授权、问题和不分析的范围。
2. 选择观察、REA、已有工程或混合路径，记录为何选择。
3. 运行工具并保存原始结果、哈希、环境和命令回执；公开仓库只放原创样例摘要。
4. 将结论标记 `observed / recovered / inferred / unknown`，每条绑定证据。
5. 输出五层拆解、BOM、局限、待验证项和给项目经理/Art Director 的问题。

## 失败分支

- 如果 `npm ci` 或 REA `check` 失败 → 保留错误回执，转为录屏/源码静态阅读，明确覆盖下降。
- 如果目标不是支持的类型 → 不强行换命令；报告“不支持的目标类型”和所需提供方。
- 如果分析结果只有字符串或请求线索 → 标为 `inferred`，不能写成服务端真实实现。
- 如果文件缺少授权或来源不明 → 停止深度分析，只给范围与合规缺口。
- 如果证据无法定位 → 该结论保持 `unknown`，不进入我方制作基线。

## 输出契约

最少包含目标与范围、五层视图、BOM、证据索引、限制、下一步验证和交接问题。原始输出放在使用者的私有目录；公开仓库只保留可分享的样例与统计摘要。

## 不要做

不要把静态发现写成完整源码；不要把竞品资产直接复制为我方生产内容；不要绕过 DRM、支付、凭据或在线服务；不要把 REA 能启动写成任何商业游戏都能完整逆向。

## 深度案例入口

[Protocol](../references/depth-analysis.zh.md) · [Case](../case-studies/2048-open-source/deep-dive.zh.md)

```sh
python scripts/check_2048_case.py --source /path/to/pinned-2048 --out outputs/2048-formulas
```
