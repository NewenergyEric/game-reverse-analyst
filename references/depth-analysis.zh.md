# 从体验追到规则、算法、数值和资产

先明确问题与版本。用同一 Feature 贯穿各层，保留 `finding_id → evidence → implication → validation`，避免每层写一份互不关联的概述。

| 层级 | 要追到的颗粒度 | 可复核输出 |
|---|---|---|
| 玩法状态 | 输入、前置条件、状态、合法/非法动作、资源扣除、奖励、反馈、恢复 | 状态迁移表、玩家路径、失败/重复/中断场景 |
| 代码逻辑 | 入口事件→调用→条件→状态写入→表现/存储；错误、重试、幂等、线程边界 | 文件/符号/行号、调用链、数据读写表；静态调用不等于已执行 |
| 算法 | 输入输出、遍历顺序、随机源、约束、不变量、复杂度、边界条件 | 伪代码、例子、复杂度推导；标明一般 n 与当前固定规模的差异 |
| 数值设计 | 参数、单位、公式、概率、成长曲线、产出/消耗、上限、配置覆盖 | 参数字典、来源、可复算推导与敏感性；区分代码规则、配置值、实际玩家分布 |
| 美术资产 | 基础件/变体/状态、生成方式、规格、绑定、动画、字体/图集、依赖、重复和许可 | 资产 BOM、状态矩阵与组合关系；文件数、逻辑资源数和制作任务数分别统计 |
| 产品与运营 | 新手引导、付费入口、活动、服务端/远程配置、可访问范围 | 观察到的入口、未覆盖项与验证计划；不能从客户端字符串推断完整商业逻辑 |

## 具体记录

- 算法记录：`input / output / preconditions / steps / invariants / edge_cases / complexity / source / verification_mode`。
- 数值记录：`parameter / value / unit / scope / source / formula / assumptions / calculated_result / unknowns`。示例：生成 2 的概率 0.9、生成 4 的概率 0.1，则单次期望值 2.2；这不是平均得分、胜率或难度结论。
- 资产记录：`id / family / base_or_variant / states / representation / dimensions_or_constraints / dependencies / source / license_or_reuse_status / production_implication`。CSS 生成的 11 个数值外观，不应报告成 11 张纹理；三种字体字重各有三个封装，不等于九套字体设计。
- 每个重要规则至少给一个正常例和一个边界/反例。标记 `source_inspected / formula_recomputed / target_executed`，不能互相代替。

## 执行与公开

REA 回执说明实际提供方、目标与输入哈希。补充人工源码分析、公式复算或资产清单时分别保存记录，不能把新增结论冒充旧回执直接输出。

运行目标或测试 harness 前检查材料来源及可执行副作用；仅有静态分析权限时用源码定位与独立公式复算。保存失败和未覆盖路径。资源清单不转移许可；我方生产需要自己的需求与合法资产。

固定版本 [2048 深度案例](../case-studies/2048-open-source/deep-dive.md)展示：移动与合并调用链、随机生成、计分、终止条件、CSS 资产家族，以及不能推导出的经济/服务端结论。
