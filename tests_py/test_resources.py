import unittest
from pathlib import Path
from analysis.io import read_records
from analysis.summary import summarize
class ResourceTests(unittest.TestCase):
    def test_all_synthetic_scenarios(self):
        root=Path(__file__).resolve().parents[1]/'data/scenarios'
        files=list(root.glob('*.csv'));self.assertEqual(len(files),36)
        for file in files:
            rows=read_records(file);result=summarize(rows,100)
            self.assertTrue(all(r['is_synthetic'] for r in rows));self.assertGreater(result['complete_pairs'],0)
