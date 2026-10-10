# Human Guide · Game Reverse Analyst

[中文](HUMAN-GUIDE.md)

## What this role solves

With explicit authority, it turns recordings, screenshots, packages, existing projects, or REA evidence into mechanics, architecture, rules, balance, and asset structure. It answers how a target works, what was observed, and what remains unknown. It does not turn protected competitor material into production assets.

## 30-second start

1. Name the target version, source, authority, scope, and main question.
2. Ask the agent to read `SKILL.md`, then choose the path:

   ```text
   npm ci --ignore-scripts
   python scripts/rea_bridge.py check
   python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/demo-analysis
   ```

3. Read the evidence index, coverage, and unknowns before the mechanics or architecture view.
4. Send our implementation scope to the production manager and art families or exemplars to the Art Director.

## What you provide

Target files or project, version, permitted depth, platform/engine clues, and a question list. When authority, target material, or a suitable provider is missing, stop at a scope statement instead of filling gaps by inference.

## What you receive

A five-layer analysis, evidence IDs, hashes and locations, BOM, limitations, validation questions, and handoff questions. The REA CLI is a static-analysis entry point; it does not run the game or promise complete source recovery.

Only analyze lawful material. Do not bypass DRM, payment, credentials, access control, or online services. Keep `observed`, `recovered`, `inferred`, and `unknown` distinct.
