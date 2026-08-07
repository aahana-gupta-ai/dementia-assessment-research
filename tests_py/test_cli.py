import unittest, io
from pathlib import Path
from contextlib import redirect_stdout
from analysis.cli import main
class CLITests(unittest.TestCase):
    def test_cli_json(self):
        target=Path(__file__).resolve().parents[1]/'data/scenarios/balanced-en.csv'
        output=io.StringIO()
        with redirect_stdout(output):result=main([str(target),'--replicates','100'])
        self.assertTrue(result['is_synthetic']);self.assertIn('mean_paired_difference',output.getvalue())
