---
name: game-reverse-analyst
description: Deconstruct game recordings, packages or projects into player loops, content structure, code and data flow, algorithms, numerical rules and an art asset BOM. Use available, authorized evidence and pinned REA static analysis when needed; preserve versions, provenance and coverage limits for competitor study and project assessment.
---

# Game Reverse Analyst

Explain what the competitor does, how its systems and content are structured, and what this implies for our own scope. Record competitor observations, recovered implementation and our design choices separately. Code is one source of evidence; it is not a prerequisite for understanding a game.

## Choose the evidence path

Establish target version, input type, research question and permitted scope. Recordings/screenshots support experience and art analysis. An available project can be read statically. Use REA when an implementation question and a suitable target justify it.

Read [REA integration and coverage](references/rea-integration.md). With compatible Node/npm, run `npm ci --ignore-scripts` in this repository, then:

```sh
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/merge-analysis
python scripts/rea_bridge.py inspect-artifact /path/to/game-package --out outputs/package-analysis
```

These commands inspect explicitly supplied local targets without executing the game. APK/.NET prerequisites are separate. Report missing dependencies instead of claiming successful decompilation. An already connected REA MCP can use its advertised schema without reinstalling or changing global configuration.

## Analyze five connected layers

Read [depth analysis](references/depth-analysis.md) when tracing implementation, numerical design or workload. Produce checkable records for each covered layer and identify missing evidence; module counts do not measure depth.

1. **Player experience:** loop, states, inputs, conditions, feedback, progression, economy and content cadence; cite the observed version and location.
2. **Architecture and logic:** entry points, modules, calls, data/storage, loading, engine/native boundaries and declared network interactions. Static URLs or requests do not prove server implementation.
3. **Algorithms and numerical design:** configuration/functions and use sites, applicable inputs, equations, unknown branches and validation methods. One recovered function does not reveal the full economy.
4. **Art and content BOM:** categories, families, base items/variants, states, specifications, bindings, duplicate files and composition. REA and format-specific tools such as UnityPy/AssetRipper complement one another where supported.
5. **Implications for our project:** useful structural ideas, our reusable assets, original work required, coverage gaps and next tests. Resource counts need production assumptions before becoming estimates.

Label claims `observed / recovered / inferred / unknown`, with evidence IDs, hashes and specific locations. Recovered output is not necessarily original complete source. An asset inventory does not establish reuse rights or person-days.

## Outputs and handoff

Use the [deconstruction package](references/deconstruction-package.md): scope, system/experience/asset views, BOM, evidence, limits, open tests and questions for production assessment. Keep raw REA output private; public examples must be original or independently shareable and suitably summarized.

## Failure paths and limits

Use authorized, legally available material and a known version. When the target or provider cannot support a claim, preserve the scope and gap rather than guessing.

- Failed installation, `check` or analysis: keep the error receipt and use an available recording, screenshot or project path with reduced coverage.
- Unsupported format/provider: state required tools and unverified coverage; a different command is not proof of success.
- Strings/imports/request clues only: label inference, not server implementation.
- Missing evidence ID/hash/location: keep the claim unverified and out of the production baseline.
- Existing output directory: create a new snapshot instead of overwriting the previous analysis.

Do not bypass access controls, DRM or payment, extract credentials, interfere with online services, copy competitor assets as our deliverables, equate file counts with effort, or infer universal target support from CLI startup.

The Production Manager turns our confirmed requirements into scope, estimates and work packages. Art Director uses observed families and visual principles to guide original standards and representative assets. Prototype suggestions remain proposals until adopted. See the [four-role workflow](docs/WORKFLOW.md).
