"""Run a synthetic dataset analysis: python3 -m analysis.cli FILE.csv."""
import argparse, json
from .io import read_records
from .summary import summarize
from .report import markdown_report

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('csv')
    parser.add_argument('--format', choices=['json','markdown'], default='json')
    parser.add_argument('--seed', type=int, default=42)
    parser.add_argument('--replicates', type=int, default=1000)
    args = parser.parse_args(argv)
    result = summarize(read_records(args.csv), args.replicates, args.seed)
    print(json.dumps(result, indent=2) if args.format=='json' else markdown_report(result), end='\n')
    return result

if __name__ == '__main__':
    main()
