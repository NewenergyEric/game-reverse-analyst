[中文](HUMAN-GUIDE.zh.md)

# Game Reverse Analyst · Human guide

Start with how the game works, then connect gameplay states, code and data flow, algorithm boundaries, numeric parameters, asset families and presentation. Footage supports observation; authorized source or packages enable deeper analysis where tools provide coverage.

## Trace code and algorithms

> Why can this 2048 left move not immediately make an 8? Show the call path, state changes and source locations.

Receive the input-to-save chain, merge boundaries, pinned source version and specific test questions.

## Inspect numeric design

> Would a 20% spawn chance for 4 make the game harder? Explain current parameters and what needs an experiment.

The 90/10 probability and expected tile value can be recalculated. Difficulty and win/score distributions require a player policy, seeds and real runs.

## Build an art and content BOM

> Do eleven tile values need eleven images? Separate components, states, motion, fonts and platform metadata.

Count CSS components, value variants, logical states and files separately, with source locations and production implications.

## Review and handoff

The target game was not executed. Source inference, formula calculation and runtime verification are separate. A JavaScript case does not establish support for every APK, Unity or native game. Footage cannot prove server algorithms; unsupported layers remain unknown.

[Reproducible case](../case-studies/2048-open-source/deep-dive.md)

[Agent guide](AGENT-GUIDE.md)
