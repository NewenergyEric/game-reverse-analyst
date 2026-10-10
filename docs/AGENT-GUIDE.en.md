# Agent Guide · game-reverse-analyst

[中文](AGENT-GUIDE.md)

## Read order

Read `SKILL.md`, then `references/rea-integration.md` and `references/deconstruction-package.md` for the target. Install the pinned npm dependency only for REA work. Do not change global MCP configuration.

## Standard workflow

1. State target, version, authority, question, and excluded scope.
2. Select observation, REA, source review, or a combined path and record why.
3. Preserve raw results, hashes, environment, and command receipt privately; publish only shareable derived evidence.
4. Label each finding `observed`, `recovered`, `inferred`, or `unknown` and bind it to evidence.
5. Deliver the five-layer view, BOM, limitations, validation needs, and production/Art Director questions.

## Failure branches

- REA install, check, or target analysis fails: retain the error receipt and move to a lower-coverage observation/source path.
- Target type unsupported: state the missing provider; do not substitute an unrelated command.
- Only strings or request clues exist: label the conclusion `inferred`, never server implementation.
- Authority or provenance missing: stop deeper analysis and report the compliance gap.
- Evidence cannot be located: keep the finding `unknown` and out of the production baseline.

At minimum include target and scope, five-layer analysis, BOM, evidence index, limitations, next validation, and handoff questions. Never bypass controls, copy competitor assets into production, present static recovery as complete source, or claim universal reverse-engineering coverage.
