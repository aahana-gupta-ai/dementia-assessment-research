import unittest
from analysis.pairs import paired_differences
class PairTests(unittest.TestCase):
    def test_complete_pairs_only(self):
        rows=[dict(participant_id='SYN-1',language='en',condition='original',demo_error_count=0),dict(participant_id='SYN-1',language='en',condition='adapted',demo_error_count=2),dict(participant_id='SYN-2',language='en',condition='original',demo_error_count=None)]
        self.assertEqual(paired_differences(rows),[2])
    def test_duplicate_fails(self):
        row=dict(participant_id='SYN-1',language='en',condition='original',demo_error_count=1)
        with self.assertRaises(ValueError):paired_differences([row,row])
