# Open-Source 2048 — Evidence-Backed Analysis

[中文](README.md) · [Public evidence receipt](public-receipt.json) · [Chinese dashboard](dashboard-zh.png)

[![Open-source 2048 analysis dashboard](dashboard-en.png)](dashboard-en.png)

**Target:** [gabrielecirulli/2048](https://github.com/gabrielecirulli/2048), commit [`478b6ec346e3787f589e4af751378d06ded4cbbc`](https://github.com/gabrielecirulli/2048/commit/478b6ec346e3787f589e4af751378d06ded4cbbc), MIT License.

**Method:** Run the pinned REA 6.3.0 JavaScript provider against a clean source export using inert static analysis. The target was not executed. No account, network service, DRM, or private material was touched.

## Recovered structure

| Module | Responsibility | Evidence location |
|---|---|---|
| `application.js` | Assemble input, view, and storage around a 4×4 grid | `js/application.js:2-3` |
| `game_manager.js` | Register events, restore state, move, merge, score, and detect the end | `js/game_manager.js:9-13, 35-58, 130-190` |
| `grid.js` / `tile.js` | Grid, cells, bounds, tiles, and serialization | `js/grid.js`, `js/tile.js` |
| `keyboard_input_manager.js` | Keyboard and touch input | `js/keyboard_input_manager.js` |
| `html_actuator.js` | Render grid, score, and state through `requestAnimationFrame` | `js/html_actuator.js` |
| `local_storage_manager.js` | Persist best score and game state with a storage fallback | `js/local_storage_manager.js` |

## Reviewable rules

- A spawned tile is 2 with 90% probability and 4 with 10%: `game_manager.js:69-75`.
- A tile merges only once per traversal through `!next.mergedFrom`: `game_manager.js:155-170`.
- Score increases by the merged tile value; reaching 2048 marks a win: `game_manager.js:166-174`.
- A new tile appears only after a successful move; the game ends when no empty cell or adjacent match remains: `game_manager.js:177-190, 238-267`.
- Grid, score, terminal state, and continuation state are serialized: `game_manager.js:79-109`.

## REA receipt

| Field | Value |
|---|---|
| REA | `rea-agents@6.3.0` · JavaScript provider v1 |
| Execution mode | Inert static parsing; `target_executed: false` |
| Scale | 10 JS modules · 23 nodes · 33 relationships |
| Evidence ID | `ev_064ecb8d503c613d03e8b8b482ff090906c0f020c749dedaa60b1d900fc42c5f` |
| Root artifact SHA-256 | `998b95deaa367512690884041ddba58a52e8c236559e0fcdc119cfc57071eea6` |
| Output SHA-256 | `47a7fd180a4e3e88867a9a500a103d01903168f76458a327ae08c88244838c12` |

See [`public-receipt.json`](public-receipt.json) for full fields and key input hashes. The public repository contains derived evidence only; the complete 5.8 MB REA record remains in a locally ignored directory.

## Limitations

Static relationships are architecture candidates, not proof of runtime order, frequency, or server behavior. Dynamic loading, reflection, obfuscation, and build-generated paths may be unresolved. This case validates the JavaScript provider; it does not prove APK, Unity, .NET, or native analysis.

The source and project name belong to their original author. This case validates the evidence chain and role workflow without copying or republishing the target source.
