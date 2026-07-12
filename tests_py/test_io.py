import unittest
from analysis.io import normalize_row
class ReadTests(unittest.TestCase):
    def row(self, **changes):
        return dict(participant_id='SYN-1', language='en', cohort='demo', condition='original', demo_error_count='0', is_synthetic='true', **changes)
    def test_missing_is_not_zero(self):
        row=self.row();self.assertEqual(normalize_row(row)['demo_error_count'],0)
        row['demo_error_count']='';self.assertIsNone(normalize_row(row)['demo_error_count'])
    def test_markers_and_bounds(self):
        row=self.row();row['is_synthetic']='false'
        with self.assertRaises(ValueError):normalize_row(row)
        row=self.row();row['demo_error_count']='41'
        with self.assertRaises(ValueError):normalize_row(row)
