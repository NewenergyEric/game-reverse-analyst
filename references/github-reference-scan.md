# GitHub 同类参考与本仓库取舍

- [REA](https://github.com/morluto/rea)：证据化分析和多目标提供方是本岗位的直接参考；本仓库固定 CLI 版本，并保留原始结果与哈希。
- [Reverse](https://github.com/dotkaio/Reverse)：同时提供 Skill、CLI、Evidence bundle 和 snapshot；本仓库吸收“可复用分析快照”和证据状态，但不复制其未验证的目标覆盖。
- [FreeNAP/rea--](https://github.com/FreeNAP/rea--)：展示了 Agent 通过 MCP 调用 REA 并把结果带回调查流程；本仓库保留 CLI fallback，避免把某个宿主连接当成必要条件。
- [gamedev-ai-agents](https://github.com/ilezhnin/gamedev-ai-agents)：强调设计契约、阶段计划和 QA 分离；本岗位将拆解结果交给项目经理，而不是直接执行制作。

当前取舍：分析器负责“理解与证据”，不负责绕过保护、复制资产或把静态恢复结果包装成完整游戏制作能力。
