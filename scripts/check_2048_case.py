#!/usr/bin/env python3
"""Verify the pinned 2048 case inputs and recompute documented formulas, without running the game."""
import argparse
import hashlib
import json
from pathlib import Path
import re

CASE = Path(__file__).resolve().parents[1] / 'case-studies/2048-open-source'


def verify(source, manifest):
    for item in manifest['inputs']:
        path = source / item['path']
        if hashlib.sha256(path.read_bytes()).hexdigest() != item['sha256']:
            raise ValueError('Pinned input mismatch: ' + item['path'])
    game = (source / 'js/game_manager.js').read_text(encoding='utf-8')
    style = (source / 'style/main.scss').read_text(encoding='utf-8')
    probability, low, high = map(float, re.search(r'Math.random\(\) < ([.\d]+) \? (\d+) : (\d+)', game).groups())
    field, spacing, cells = [float(re.search(r'\$' + key + r': ([\d.]+)', style).group(1)) for key in ['field-width', 'grid-spacing', 'grid-row-cells']]
    return {
        'case_id': manifest['case_id'], 'verification': 'pinned input hashes and formula recomputation',
        'target_executed': False, 'runtime_behavior_verified': False,
        'inputs_verified': len(manifest['inputs']),
        'calculations': {
            'spawn_expected_tile_value': probability * low + (1 - probability) * high,
            'at_least_one_4_in_10_spawns': 1 - probability ** 10,
            'desktop_tile_width_css_px': (field - spacing * (cells + 1)) / cells,
        },
        'assumptions': ['The ten spawn draws are independent with the source probability.', 'Expected tile value is not expected score or win probability.', 'Desktop Sass defaults; mobile overrides are separate.'],
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', type=Path, required=True)
    parser.add_argument('--out', type=Path, required=True)
    args = parser.parse_args()
    try:
        manifest = json.loads((CASE / 'deep-dive.json').read_text(encoding='utf-8'))
        result = verify(args.source, manifest)
        args.out.mkdir(parents=True, exist_ok=False)
        (args.out / 'verification.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
        print(json.dumps(result, indent=2))
        return 0
    except (OSError, ValueError, AttributeError) as exc:
        print(json.dumps({'error': str(exc)}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
