import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest
from unittest.mock import patch

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('bridge',ROOT/'scripts/rea_bridge.py')
module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)

class BridgeTests(unittest.TestCase):
    def test_public_2048_receipt_is_static_and_versioned(self):
        receipt=json.loads((ROOT/'case-studies/2048-open-source/public-receipt.json').read_text(encoding='utf-8'))
        self.assertFalse(receipt['analysis']['target_executed'])
        self.assertEqual(receipt['analysis']['version'],'6.3.0')
        self.assertEqual(receipt['analysis']['graph_nodes'],23)
        self.assertEqual(receipt['target']['commit'],'478b6ec346e3787f589e4af751378d06ded4cbbc')
    def test_manifest_changes_with_input(self):
        with tempfile.TemporaryDirectory() as directory:
            target=Path(directory)/'a.js';target.write_text('export const n=1;',encoding='utf-8')
            first=module.input_manifest(target)
            target.write_text('export const n=2;',encoding='utf-8')
            self.assertNotEqual(first[0]['sha256'],module.input_manifest(target)[0]['sha256'])
    def test_output_cannot_contaminate_target(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(module,'runtime',return_value=['node','rea.mjs']):
            target=Path(directory)
            with self.assertRaises(ValueError): module.analyze('analyze-js',target,target/'out')
    def test_invalid_json_is_not_success(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(module,'runtime',return_value=['node','rea.mjs']), patch.object(module.subprocess,'run',return_value=subprocess.CompletedProcess([],0,'not JSON','')):
            target=Path(directory)/'source.js';target.write_text('export {};',encoding='utf-8')
            code,receipt=module.analyze('inspect-artifact',target,Path(directory)/'out')
            self.assertEqual(code,1);self.assertEqual(receipt['status'],'failed')
    def test_timeout_keeps_receipt(self):
        with tempfile.TemporaryDirectory() as directory, patch.object(module,'runtime',return_value=['node','rea.mjs']), patch.object(module.subprocess,'run',side_effect=subprocess.TimeoutExpired([],1)):
            target=Path(directory)/'source.js';target.write_text('export {};',encoding='utf-8')
            out=Path(directory)/'out';code,receipt=module.analyze('inspect-artifact',target,out,timeout=1)
            self.assertEqual(receipt['status'],'timeout');self.assertEqual(code,1)
            self.assertTrue((out/'receipt.json').is_file())
    def test_upstream_error_is_not_success(self):
        self.assertTrue(module.envelope_failed({'isError':True,'message':'provider unavailable'}))
        self.assertFalse(module.envelope_failed({'data':{'evidence':[]}}))
    def test_json_without_evidence_is_rejected(self):
        with self.assertRaises(ValueError): module.evidence_index({})

if __name__=='__main__': unittest.main()
