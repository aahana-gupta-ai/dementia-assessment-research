import unittest
from analysis.summary import summarize
from analysis.report import markdown_report
class ReportTests(unittest.TestCase):
    def test_empty_output_is_explicit(self):
        report=markdown_report(summarize([]));self.assertIn('Synthetic demonstration',report);self.assertIn('not available',report);self.assertIn('not clinical findings',report)
