[中文](depth-analysis.zh.md)

# From player experience to rules, numbers and assets

Fix the question and version. Follow one feature across layers using `finding_id → evidence → implication → validation` instead of producing unrelated summaries.

| Layer | Required depth | Checkable output |
|---|---|---|
| Gameplay states | Inputs, preconditions, valid/invalid actions, costs, rewards, feedback, recovery | Transition table, player path, failure/repeat/interruption cases |
| Code logic | Event → call → condition → state write → view/storage; errors, retries, idempotency, thread boundaries | Files/symbols/lines, call chain, data reads/writes; static calls are not executed calls |
| Algorithm | Inputs/outputs, traversal, randomness, constraints, invariants, complexity, boundaries | Pseudocode, examples and derivation; separate general n from the actual fixed size |
| Numerical design | Parameters/units/formulas, probabilities, curves, sources/sinks, caps, configuration overrides | Parameter dictionary, provenance, recalculation and sensitivity; distinguish rule, configured value and actual player distribution |
| Art/content | Base/variant/state, representation, specs, binding, animation, fonts/atlases, dependencies, duplicates, licensing | BOM, state matrix and composition; count files, logical resources and production tasks separately |
| Product/live ops | Onboarding, payment entry points, events, server/remote configuration, accessible scope | Observed entry points, unobserved scope and next test; client strings do not prove the whole commercial system |

## Record formats

- Algorithm: `input / output / preconditions / steps / invariants / edge_cases / complexity / source / verification_mode`.
- Numerical record: `parameter / value / unit / scope / source / formula / assumptions / calculated_result / unknowns`. A 0.9 chance of 2 and 0.1 chance of 4 gives expected generated value 2.2, not expected score, win rate or difficulty.
- Asset record: `id / family / base_or_variant / states / representation / dimensions_or_constraints / dependencies / source / license_or_reuse_status / production_implication`. Eleven CSS appearances are not eleven textures; three weights in three formats are not nine independently designed typefaces.
- Give important rules a normal and an edge/counterexample. Keep `source_inspected / formula_recomputed / target_executed` distinct.

## Execution and publication

REA receipts identify actual provider, target and input hashes. Save supplementary source analysis, formula checks and asset inventories separately; do not attribute them to an older tool receipt.

Before executing a target or harness, check provenance and side effects against the permitted scope. Static-only work uses source locations and independent calculations. Preserve failure and uncovered paths. Asset inventory does not transfer a license; our production needs original requirements and usable assets.

The pinned [2048 case](../case-studies/2048-open-source/deep-dive.md) covers move/merge logic, spawning, scoring, terminal conditions and CSS asset families, along with economic/server conclusions that cannot be established.
