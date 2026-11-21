from __future__ import annotations

import shutil
from pathlib import Path
import tempfile
import unittest

from check_sources import load_sources

DATA = Path(__file__).resolve().parents[1] / 'data'


class ExchangeTests(unittest.TestCase):
    def test_example_is_readable(self):
        tables = load_sources(DATA)
        self.assertTrue(all(tables.values()))
        self.assertTrue(all(float(r['effect']) == float(r['effect']) and float(r['se']) > 0 for r in tables['comparisons']))
        self.assertTrue(all(0 <= int(r['overlap_min']) <= int(r['overlap_max']) for r in tables['provenance']))
        self.assertTrue(any(r['overlap_min'] != r['overlap_max'] for r in tables['provenance']))

    def test_duplicate_identity_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            duplicate = Path(directory) / 'copies'
            shutil.copytree(DATA, duplicate)
            path = duplicate / 'comparisons.csv'
            rows = path.read_text(encoding='utf-8').splitlines()
            path.write_text('\n'.join(rows + [rows[1]]) + '\n', encoding='utf-8')
            with self.assertRaisesRegex(ValueError, '标识为空或重复'):
                load_sources(duplicate)
