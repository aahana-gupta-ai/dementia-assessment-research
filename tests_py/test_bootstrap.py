import unittest
from analysis.bootstrap import bootstrap_interval
class BootstrapTests(unittest.TestCase):
    def test_reproducible_and_constant(self):
        self.assertEqual(bootstrap_interval([1,2,3],seed=2),bootstrap_interval([1,2,3],seed=2))
        interval=bootstrap_interval([-3,-3,-3]);self.assertEqual(interval['lower'],-3);self.assertEqual(interval['upper'],-3)
    def test_empty(self):
        self.assertIsNone(bootstrap_interval([]))
