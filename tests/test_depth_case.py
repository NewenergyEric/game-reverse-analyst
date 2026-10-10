import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('case_check',ROOT/'scripts/check_2048_case.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class DepthCaseTests(unittest.TestCase):
    def test_public_case_separates_calculation_from_execution(self):
        case=json.loads((ROOT/'case-studies/2048-open-source/deep-dive.json').read_text(encoding='utf-8'))
        receipt=json.loads((ROOT/'case-studies/2048-open-source/verification.json').read_text(encoding='utf-8'))
        self.assertFalse(case['target_executed'])
        self.assertFalse(receipt['runtime_behavior_verified'])
        self.assertAlmostEqual(receipt['calculations']['spawn_expected_tile_value'],2.2)
        self.assertEqual(receipt['inputs_verified'],len(case['inputs']))
        self.assertTrue(all(f['location'] and f['source_url'] for f in case['findings']))
    def test_changed_source_is_rejected_before_formula_reading(self):
        case=json.loads((ROOT/'case-studies/2048-open-source/deep-dive.json').read_text(encoding='utf-8'))
        with tempfile.TemporaryDirectory() as directory:
            path=Path(directory)/case['inputs'][0]['path'];path.parent.mkdir(parents=True)
            path.write_text('changed',encoding='utf-8')
            with self.assertRaisesRegex(ValueError,'Pinned input mismatch'): module.verify(Path(directory),case)

if __name__=='__main__': unittest.main()
