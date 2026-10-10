[中文](rea-integration.zh.md)

# REA integration: pinned version and verified coverage

This repository pins npm `rea-agents@6.3.0` from [morluto/rea](https://github.com/morluto/rea), checked on 2026-10-10. Popularity and upstream activity are not product guarantees.

## Local CLI

Use the Node requirement in `package.json`. `npm ci --ignore-scripts` installs locally without changing agent-wide configuration. The Python wrapper invokes the local Node CLI with an argument vector, not a shell command string.

```sh
python scripts/rea_bridge.py check
python scripts/rea_bridge.py analyze-js examples/merge-fixture --out outputs/run-001
python scripts/rea_bridge.py inspect-artifact /path/to/file --out outputs/run-002
python scripts/rea_bridge.py inspect-apk /path/to/game.apk --out outputs/run-003
python scripts/rea_bridge.py inspect-managed /path/to/game.dll --out outputs/run-004
```

The output directory must be new. It contains REA JSON, logs, execution receipt and a small index. Record CLI errors, timeouts and parse failures separately. A successful invocation still needs interpretation of coverage.

| Path | Prerequisites | Can establish | Does not establish |
|---|---|---|---|
| JavaScript/Electron | REA static application analysis | Readable modules, relations, evidence locations | All dynamic behavior, backend or complete game logic |
| APK | REA Android tools; current JADX/JDK requirements | Manifest, classes and recoverable methods | Universal obfuscated/protected-package support or all original assets |
| .NET | REA managed static tools | Metadata, members, CIL/native boundaries | Original C# project or complete Unity source project |
| Native binaries | Configured Ghidra/Hopper/IDA and supported environment | Pseudocode, assembly, symbols, references | Original full source or unknown server rules |
| Asset inventory | inspect-artifact; UnityPy/AssetRipper where format supports | Physical files and some semantic information | Complete art BOM, ownership or production cost automatically |
| Runtime/network | Specific permitted target, scenario and tools | Behavior actually observed | Unobserved paths or authority to expand into accounts/live services |

See [verification](../evals/verification.md) for actual test receipts. Do not turn upstream capability lists into local passing results.

## MCP as an alternate entry

If already connected, use the current server's advertised tools/schema. For a requested new connection, upstream `setup --client codex --dry-run --json` can describe the proposed changes before authorized installation. Global configuration and native engines are not prerequisites for this local CLI. See [official setup](https://rea.tools/get-started/).

JADX is the Android tool name. Lack of source does not imply lack of observable assets; accessibility and reuse rights are separate. A local analysis process does not guarantee the entire agent/model data path stays local.
