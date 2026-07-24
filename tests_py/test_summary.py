import unittest
from pathlib import Path
from analysis.io import read_records
from analysis.summary import summarize
class SummaryTests(unittest.TestCase):
    def test_missingness_and_pair_count(self):
        root=Path(__file__).resolve().parents[1]
        result=summarize(read_records(root/'data/scenarios/missingness-en.csv'))
        self.assertEqual(result['rows'],40);self.assertEqual(result['missing_rows'],3);self.assertEqual(result['complete_pairs'],17)
