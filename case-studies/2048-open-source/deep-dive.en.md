# 2048: follow a merge rule into code, numbers and assets

[中文](deep-dive.md) · [Structure and original REA receipt](README.en.md) · [Analysis JSON](deep-dive.json) · [Asset BOM](asset-bom.csv) · [Formula receipt](verification.json)

> I am designing a sliding merge game. Why does this move not make an 8? What does the spawn probability mean? How many images does the art team actually need?

This pass reads the same pinned source, verifies file hashes and recomputes formulas. It retains the original REA static-analysis receipt. **The target game was not executed. These source-derived examples still need runtime tests.**

## Code logic: follow one input

`Input → terminal-state guard → direction and traversal → farthest empty cell → merge or slide → spawn only after movement → loss check → persist and render`

Traversal starts at the movement edge. Previous mergedFrom flags are cleared. An equal-value neighbor can merge only if it has no mergedFrom. The new tile records its parents, preventing a second merge in the same move. Its value is added to the score; a 2048 tile sets the win flag, with continuation controlled by state.

| Source-derived acceptance input | After left move, excluding spawn | Score delta | Boundary |
|---|---|---|---|
| 2, 2, 4, empty | 4, 4, empty, empty | +4 | New 4 must not immediately become 8 |
| 2, 2, 2, 2 | 4, 4, empty, empty | +8 | Two independent merges in direction order |
| No displacement | Unchanged | 0 | No extra random spawn |

Locations: game_manager.js:130–190,207–235. Generalizing to N×N, scanning N² cells with up to N steps per farthest-cell search gives a loose O(N³) bound. The actual board is fixed at 4×4. This is code analysis, not a benchmark.

## Numbers: probability does not establish difficulty

| Parameter or calculation | Result | Boundary |
|---|---|---|
| Spawn 2 / spawn 4 | 90% / 10% | Source threshold, game_manager.js:69–75 |
| Expected new tile value | 0.9×2 + 0.1×4 = **2.2** | Not expected score or win rate |
| At least one 4 in ten spawns | 1−0.9¹⁰ = **65.13%** | Assumes independent draws |
| Starting tiles | 2 | Values and positions are not fixed |

To ask how changing the 4 probability to 20% affects difficulty, first define a player policy and random seeds, then compare survival steps, win rates and score distributions across runs. This case contains no such runtime results.

## Art BOM: separate states, variants and files

| Family | What the source contains | Production implication |
|---|---|---|
| Tile component | Eleven value styles (2..2048), plus super; normal/new/merged states | CSS and text, not eleven textures |
| Layout and motion | Desktop tile width 106.25 CSS px; move 100 ms; appear/pop 200 ms after a 100 ms delay | Layout and animation parameters; mobile overrides remain separate |
| Clear Sans | Three weights × three formats = nine files | One font family, not nine designs |
| Platform metadata | Three touch/startup PNGs and one favicon.ico | Separate from gameplay art |

Evidence: style/main.scss:4–7,22,335–450 and html_actuator.js:60–83. deep-dive.json records SHA-256 per input. No target art is copied; inventory is neither a reuse license nor an effort estimate.

## Handoff

- Engineering/QA: test the merge, no-op, save and terminal-state boundaries; attach real execution receipts.
- Systems design: define player policy before probability experiments; retain seeds, sample size and distributions.
- Art director: specify a parameterized tile component, value styles and state animation; inspect mobile layout separately.
- PM: turn rules, parameters and asset specifications into versioned inputs and acceptance cases; competitor code is not our approved design baseline.

Reproduce input-hash checks and formula calculations without executing the source:

```sh
python scripts/check_2048_case.py --source /path/to/pinned-2048 --out outputs/2048-formulas
```

Pinned sources: [js/game_manager.js](https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/js/game_manager.js) · [js/grid.js](https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/js/grid.js) · [js/html_actuator.js](https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/js/html_actuator.js) · [style/main.scss](https://github.com/gabrielecirulli/2048/blob/478b6ec346e3787f589e4af751378d06ded4cbbc/style/main.scss)
