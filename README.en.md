[中文](README.md)

# Game Reverse Analyst

### Understand the play. Trace the implementation.

Start with how the game works, then connect gameplay states, code and data flow, algorithm boundaries, numeric parameters, asset families and presentation. Footage supports observation; authorized source or packages enable deeper analysis where tools provide coverage.

<picture>
  <source media="(prefers-reduced-motion: reduce)" srcset="assets/readme/hero-en.png?v=depth-v4">
  <img src="assets/readme/hero-en.webp?v=depth-v4" width="100%" alt="Follow a gameplay rule into code, algorithms, numbers and art assets.">
</picture>

[Download the full 24-second introduction · MP4](assets/readme/hero-en.mp4?raw=true) · [GIF](assets/readme/hero-en.gif) · [Transcript](assets/readme/transcript-en.md)

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

[Human guide](docs/HUMAN-GUIDE.en.md) · [Agent guide](docs/AGENT-GUIDE.en.md) · [SKILL.md](SKILL.md) · [Tests and review](evals/) · [Motion source](motion/README.md)

```sh
python -m unittest discover -s tests -v
python scripts/check_presentation.py
```

</details>

[MIT License](LICENSE) · Made by Eric and Agents.
