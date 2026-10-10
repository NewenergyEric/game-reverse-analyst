# Game Reverse Analyst · Human guide

[中文](HUMAN-GUIDE.md)

Start with footage, screenshots or authorized source. Map rules, modules and assets.

## Bring your materials

Give your agent usable materials and the question you want answered.
Incomplete material is fine to start; missing inputs that affect the next step stay visible.

## I want to understand the gameplay

> Use `$game-reverse-analyst`. Review this footage and these screenshots. Map the core loop, state changes and feedback. Cite each observation and list what the materials do not show.

Gameplay and experience views, observation references and a list of missing materials. Gameplay observation can start directly from footage.

## I have authorized source and want the implementation

> Pin this legally usable 2048 source version. Find the input, merge, score, display and storage modules. Trace “a tile merges only once per move” to its source location.

A system BOM, module responsibilities and rule locations. Suitable targets can use REA static analysis with retained evidence and receipts.

## I need to hand the findings to the team

> Prepare an analysis package: findings, evidence and remaining uncertainty. List the questions that design, engineering and art can continue. Keep our own design decisions separate.

Role-oriented findings, an evidence index, coverage gaps and further validation questions.

## How to review

Footage observation, source reading and package analysis are selected for the question. Tool coverage depends on the target. The real case validates JavaScript; APK, Unity, .NET and native targets each require their own tools and evidence.

Analyze only legally usable material; do not bypass DRM, payments, credentials or access controls. Static relationships do not prove runtime or server behavior. An asset list is neither a workload estimate nor a redistribution license.

## Outputs and handoff

- **Five-layer analysis:** gameplay, architecture, rules and values, assets, useful structures and unknowns.
- **Evidence index:** findings tied to target version, file location and input hash.
- **Role handoff:** what the team can investigate next and what needs more material or validation.

[Market Intelligence](https://github.com/NewenergyEric/game-market-intelligence) brings targets and questions. Analysis supplies structure and evidence. The [Production Manager](https://github.com/NewenergyEric/game-production-manager) organizes confirmed work. [Art Director](https://github.com/NewenergyEric/art-director-skill) develops art observations into original rules and samples.

## Technical entry for your agent

REA is pinned to 6.3.0; see package.json for Node requirements. Seven bridge tests cover invalid evidence, failures, timeouts, input hashes and output isolation.

```sh
npm ci --ignore-scripts
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/demo-analysis
```
