[中文](README.md)

# Game Reverse Analyst

### Understand the play. Trace the implementation.

**Move from “it seems to work this way” to “the evidence is here.”**

Give your agent footage, screenshots or legally usable packages and source. It maps gameplay, modules, rules and assets, then ties findings to a version, file location and evidence so designers, engineers and artists can continue the work.

<a href="assets/readme/hero-en.mp4"><picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=workflow-v3">
  <img src="assets/readme/hero-en.gif?v=workflow-v3" width="100%" alt="Start with footage, screenshots or authorized source. Map rules, modules and assets.">
</picture></a>

[24 seconds through one complete workflow · Watch MP4](assets/readme/hero-en.mp4) · [Transcript](assets/readme/transcript-en.md)

## Install, then ask your agent

Install in an Agent Skills-compatible tool, such as Codex, Claude Code or Cursor:

```sh
npx skills add https://github.com/NewenergyEric/game-reverse-analyst
```

Put the materials where your agent can read them, then describe the problem. Your agent handles file organization and commands.

### I want to understand the gameplay

> Use `$game-reverse-analyst`. Review this footage and these screenshots. Map the core loop, state changes and feedback. Cite each observation and list what the materials do not show.

**You get:** Gameplay and experience views, observation references and a list of missing materials. Gameplay observation can start directly from footage.

### I have authorized source and want the implementation

> Pin this legally usable 2048 source version. Find the input, merge, score, display and storage modules. Trace “a tile merges only once per move” to its source location.

**You get:** A system BOM, module responsibilities and rule locations. Suitable targets can use REA static analysis with retained evidence and receipts.

### I need to hand the findings to the team

> Prepare an analysis package: findings, evidence and remaining uncertainty. List the questions that design, engineering and art can continue. Keep our own design decisions separate.

**You get:** Role-oriented findings, an evidence index, coverage gaps and further validation questions.

## What the team receives

- **Five-layer analysis:** gameplay, architecture, rules and values, assets, useful structures and unknowns.
- **Evidence index:** findings tied to target version, file location and input hash.
- **Role handoff:** what the team can investigate next and what needs more material or validation.

## See a real analysis: the 2048 merge rule

The [open-source 2048 case](case-studies/2048-open-source/README.en.md) pins MIT-licensed commit `478b6ec`. REA 6.3.0 statically analyzed 10 JavaScript modules and recorded 23 nodes with 33 relationships.

A concrete finding explains how `!next.mergedFrom` prevents another merge in the same move. Locations, version and full hashes are in the [public receipt](case-studies/2048-open-source/public-receipt.json). The film illustrates a source rule; the target game was not executed.

[![See a real analysis: the 2048 merge rule](case-studies/2048-open-source/dashboard-en.png?v=workflow-v3)](case-studies/2048-open-source/dashboard-en.png)

## Work with the other roles

[Market Intelligence](https://github.com/NewenergyEric/game-market-intelligence) brings targets and questions. Analysis supplies structure and evidence. The [Production Manager](https://github.com/NewenergyEric/game-production-manager) organizes confirmed work. [Art Director](https://github.com/NewenergyEric/art-director-skill) develops art observations into original rules and samples.

<details>
<summary><strong>Requirements, technical docs and validation</strong></summary>

REA is pinned to 6.3.0; see package.json for Node requirements. Seven bridge tests cover invalid evidence, failures, timeouts, input hashes and output isolation.

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [Skill entry](SKILL.md) · [Validation and review](evals/)

```sh
npm ci --ignore-scripts
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/demo-analysis
```

[CI](https://github.com/NewenergyEric/game-reverse-analyst/actions) · [Motion source](motion/README.md)

</details>

<details>
<summary><strong>Capability boundaries and material use</strong></summary>

Footage observation, source reading and package analysis are selected for the question. Tool coverage depends on the target. The real case validates JavaScript; APK, Unity, .NET and native targets each require their own tools and evidence.

Analyze only legally usable material; do not bypass DRM, payments, credentials or access controls. Static relationships do not prove runtime or server behavior. An asset list is neither a workload estimate nor a redistribution license.

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
