[中文](README.md)

[**Game Dev Skills**](https://github.com/NewenergyEric/NewenergyEric/blob/main/GAME-DEV-SKILLS.en.md) · [Market research](https://github.com/NewenergyEric/game-market-intelligence/blob/main/README.en.md) · [Reverse analysis](https://github.com/NewenergyEric/game-reverse-analyst/blob/main/README.en.md) · [Production planning](https://github.com/NewenergyEric/game-production-manager/blob/main/README.en.md) · [Art direction](https://github.com/NewenergyEric/art-director-skill/blob/main/README.en.md)

# Game Reverse Analyst

### Understand the play. Trace the implementation.

Start with how the game works, then connect gameplay states, code and data flow, algorithm boundaries, numeric parameters, asset families and presentation. Footage supports observation; authorized source or packages enable deeper analysis where tools provide coverage.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=depth-v4">
  <img src="assets/readme/hero-en.webp?v=depth-v4" width="100%" alt="Follow a gameplay rule into code, algorithms, numbers and art assets.">
</picture>

[Download the full 24-second introduction · MP4](assets/readme/hero-en.mp4?raw=true) · [GIF](assets/readme/hero-en.gif) · [Transcript](assets/readme/transcript-en.md)

## Why this exists

**Recognizing a mechanic is only the start of understanding its workload.**

A merge can involve states, probabilities, persistence, animation and asset variants. Trace observations to inspectable evidence to separate what is established from what still needs material or experiments. That is the basis for discussing implementation cost.

This is the analysis role in Game Dev Skills. Take a research target and turn its rules and systems into material a production manager can scope and an art director can learn from. Solo creators switch hats; teams hand off the evidence.

## Install, then ask your agent

```sh
npx skills add https://github.com/NewenergyEric/game-reverse-analyst
```

Install in an Agent Skills-compatible tool such as Codex, Claude Code or Cursor. Put your materials where the agent can read them, then describe the question.

### Trace code and algorithms

> Why can this 2048 left move not immediately make an 8? Show the call path, state changes and source locations.

Receive the input-to-save chain, merge boundaries, pinned source version and specific test questions.

### Inspect numeric design

> Would a 20% spawn chance for 4 make the game harder? Explain current parameters and what needs an experiment.

The 90/10 probability and expected tile value can be recalculated. Difficulty and win/score distributions require a player policy, seeds and real runs.

### Build an art and content BOM

> Do eleven tile values need eleven images? Separate components, states, motion, fonts and platform metadata.

Count CSS components, value variants, logical states and files separately, with source locations and production implications.

## See a concrete case

**Real open-source case: 2048 at commit 478b6ec.** Extends the existing REA 6.3.0 static receipt with code flow, merge algorithm, spawn probabilities, formula calculations and an asset BOM. Hashes verified for 18 input files.

[Full analysis and downloadable records](case-studies/2048-open-source/deep-dive.en.md)

[![Game Reverse Analyst](case-studies/2048-open-source/dashboard-en.png?v=depth-v4)](case-studies/2048-open-source/dashboard-en.png)

## What the team receives

- Code, rules and numbers — `deep-dive.json`
- Art assets and counting basis — `asset-bom.csv`
- Input hashes and calculations — `verification.json`

<details>
<summary>Boundaries, guides and validation</summary>

The target game was not executed. Source inference, formula calculation and runtime verification are separate. A JavaScript case does not establish support for every APK, Unity or native game. Footage cannot prove server algorithms; unsupported layers remain unknown.

Core helpers use Python 3.10+ and the standard library. Remotion is optional presentation tooling.

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [SKILL.md](SKILL.en.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.

## Tell me where the handoff breaks

After trying one task, share the goal, public inputs, actual output and what was still missing.

[Share feedback or a case](https://github.com/NewenergyEric/game-reverse-analyst/issues/new?template=use-case.yml)

## Four roles. One game worth making.

For a solo creator these are four hats; for a team they are connected responsibilities. Explore what is worth making, what competitors do, the resources it requires, and the original art that defines it.

[How the roles exchange evidence, scope and visual assets](docs/WORKFLOW.en.md) · [Explore all four roles](https://github.com/NewenergyEric/NewenergyEric/blob/main/GAME-DEV-SKILLS.en.md)

| Your question | Start here | Carry forward |
|---|---|---|
| What is worth making? | [Market research](https://github.com/NewenergyEric/game-market-intelligence/blob/main/README.en.md) | Options, sources and validation gaps |
| How does it work? | [Reverse analysis](https://github.com/NewenergyEric/game-reverse-analyst/blob/main/README.en.md) | Rules, implementation evidence and asset BOM |
| Can we scope and deliver it? | [Production planning](https://github.com/NewenergyEric/game-production-manager/blob/main/README.en.md) | SOW, work packages, dependencies and acceptance |
| What defines the art? | [Art direction](https://github.com/NewenergyEric/art-director-skill/blob/main/README.en.md) | Shared rules, representative samples and project pack |

**Solo creator:** start with the question blocking you and switch roles as needed. **Team:** hand off actual reports, BOMs, work packages and art rules, keeping sources, versions and open decisions visible.

This is a collaboration method; it does not include an orchestrator that automatically runs four agents in sequence.

![Market intelligence → competitor analysis → production assessment → original art direction; prototype and cost feedback revise earlier decisions.](assets/readme/workflow-en.png)
