#!/usr/bin/env python3
"""Run pinned REA static analyses and retain real receipts without target execution."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]
VERSION = '6.3.0'
COMMANDS = {'analyze-js': 'analyze-javascript-application', 'inspect-artifact': 'inspect-artifact',
            'inspect-apk': 'inspect-android-package', 'inspect-managed': 'inspect-managed-artifact'}


def runtime():
    node = shutil.which('node')
    package = ROOT / 'node_modules/rea-agents'
    metadata = package / 'package.json'
    if not node or not metadata.is_file():
        raise ValueError('Node or local REA missing. Install a supported Node, then run npm ci --ignore-scripts in this repository.')
    installed = json.loads(metadata.read_text(encoding='utf-8'))['version']
    if installed != VERSION:
        raise ValueError(f'Expected REA {VERSION}, found {installed}; use the committed lockfile.')
    script = package / 'scripts/rea.mjs'
    if not script.is_file(): raise ValueError('REA CLI script missing')
    return [node, str(script)]


def input_manifest(target):
    target = target.resolve(strict=True)
    if target.is_file(): paths = [target]
    else: paths = sorted(p for p in target.rglob('*') if p.is_file() and not p.is_symlink())
    result = []
    for p in paths:
        digest = hashlib.sha256()
        with p.open('rb') as file:
            for chunk in iter(lambda: file.read(1024 * 1024), b''): digest.update(chunk)
        result.append({'path': p.name if target.is_file() else p.relative_to(target).as_posix(),
                       'bytes': p.stat().st_size, 'sha256': digest.hexdigest()})
    return result


def envelope_failed(result):
    if not isinstance(result, dict): return False
    if result.get('isError') is True or result.get('success') is False: return True
    return bool(result.get('error')) and not result.get('data')


def evidence_index(result):
    if not isinstance(result, dict) or not isinstance(result.get('evidence_id'), str) or not isinstance(result.get('normalized_result'), dict):
        raise ValueError('REA output is not a canonical Evidence record')
    normalized = result['normalized_result']
    graph = normalized.get('graph', {})
    modules = []
    for node in graph.get('nodes', []):
        if node.get('kind') == 'javascript-module':
            for observation in node.get('observations', []):
                properties = observation.get('properties', {})
                if not isinstance(properties.get('path'), str):
                    continue
                modules.append({'path': properties.get('path'), 'exports': properties.get('export_names', []),
                                'evidence_location': observation.get('evidence', {}).get('location')})
    return {'evidence_id': result['evidence_id'], 'operation': result.get('operation'),
            'predicate_type': result.get('predicate_type'), 'provider': result.get('provider'),
            'modules': modules, 'graph_nodes': len(graph.get('nodes', [])), 'graph_edges': len(graph.get('edges', [])),
            'limitations': result.get('limitations', []), 'raw_evidence': 'rea-output.json'}


def analyze(mode, target, out, timeout=180):
    executable = runtime()
    target = target.resolve(strict=True)
    out = out.resolve()
    if target.is_dir() and (out == target or target in out.parents):
        raise ValueError('Output must be outside the analyzed tree')
    if out.exists(): raise ValueError('Output exists; choose a new run directory')
    manifest = input_manifest(target)
    argv = executable + [COMMANDS[mode], str(target), '--format', 'json']
    out.mkdir(parents=True, exist_ok=False)
    receipt = {'schema_version': '0.1', 'rea_version': VERSION, 'mode': mode,
               'started_at': datetime.now(timezone.utc).isoformat(), 'inputs': manifest,
               'target': str(target), 'status': 'running', 'target_executed': False}
    code = 1
    stdout = ''; stderr = ''
    try:
        completed = subprocess.run(argv, shell=False, capture_output=True, text=True, encoding='utf-8', errors='replace', timeout=timeout)
        stdout, stderr = completed.stdout, completed.stderr
        receipt['exit_code'] = completed.returncode
        try:
            parsed = json.loads(stdout)
            receipt['json_parsed'] = True
            receipt['top_level_keys'] = sorted(parsed) if isinstance(parsed, dict) else []
            failed = envelope_failed(parsed)
            if not failed:
                index = evidence_index(parsed)
                (out / 'analysis-index.json').write_text(json.dumps(index, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
        except (json.JSONDecodeError, ValueError) as exc:
            receipt['error'] = str(exc); failed = True
            if isinstance(exc, json.JSONDecodeError): receipt['json_parsed'] = False
        code = 0 if completed.returncode == 0 and not failed else 1
        receipt['status'] = 'succeeded' if code == 0 else 'failed'
    except subprocess.TimeoutExpired as exc:
        stdout = exc.stdout or ''; stderr = exc.stderr or ''
        if isinstance(stdout, bytes): stdout = stdout.decode('utf-8', errors='replace')
        if isinstance(stderr, bytes): stderr = stderr.decode('utf-8', errors='replace')
        receipt['status'] = 'timeout'; receipt['error'] = f'timeout after {timeout} seconds'
    except OSError as exc:
        receipt['status'] = 'failed'; receipt['error'] = str(exc)
    receipt['ended_at'] = datetime.now(timezone.utc).isoformat()
    receipt['interpretation'] = 'Tool result only; coverage and findings still require analyst review.'
    (out / 'rea-output.json').write_text(stdout, encoding='utf-8')
    (out / 'stderr.log').write_text(stderr, encoding='utf-8')
    receipt['output_sha256'] = hashlib.sha256(stdout.encode('utf-8')).hexdigest()
    (out / 'receipt.json').write_text(json.dumps(receipt, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
    return code, receipt


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest='mode', required=True)
    commands.add_parser('check')
    for mode in COMMANDS:
        p = commands.add_parser(mode); p.add_argument('target', type=Path)
        p.add_argument('--out', type=Path, required=True); p.add_argument('--timeout', type=int, default=180)
    args = parser.parse_args()
    try:
        if args.mode == 'check':
            result = subprocess.run(runtime() + ['--version'], shell=False, capture_output=True, text=True, encoding='utf-8', timeout=60)
            print(json.dumps({'ready': result.returncode == 0, 'version': result.stdout.strip(), 'scope': 'CLI only; providers, MCP and game targets are not verified'}, ensure_ascii=False))
            return 0 if result.returncode == 0 else 1
        if args.timeout < 1: raise ValueError('timeout must be positive')
        code, receipt = analyze(args.mode, args.target, args.out, args.timeout)
        print(json.dumps({'status': receipt['status'], 'output': str(args.out)}, ensure_ascii=False)); return code
    except (OSError, ValueError, KeyError, subprocess.TimeoutExpired) as exc:
        print(json.dumps({'status': 'blocked', 'error': str(exc)}, ensure_ascii=False)); return 1


if __name__ == '__main__':
    raise SystemExit(main())
