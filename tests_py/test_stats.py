import unittest
from analysis.stats import mean, variance, quantile
class StatsTests(unittest.TestCase):
    def test_known_statistics(self):
        self.assertEqual(mean([1,2,3]),2);self.assertEqual(variance([1,2,3]),1);self.assertEqual(quantile([1,3],.5),2)
    def test_empty_and_invalid(self):
        self.assertIsNone(mean([]));self.assertIsNone(variance([1]))
        with self.assertRaises(ValueError):mean([float('nan')])
