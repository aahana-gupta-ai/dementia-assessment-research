"""Read synthetic CSV and keep missing measurements as None."""
import csv
from pathlib import Path

REQUIRED = {'participant_id', 'language', 'cohort', 'condition', 'demo_error_count', 'is_synthetic'}

def normalize_row(row):
    if not REQUIRED.issubset(row):
        raise ValueError('Missing required columns')
    if row['is_synthetic'] not in ('true', True) or not row['participant_id'].startswith('SYN-'):
        raise ValueError('Only explicitly synthetic records are accepted')
    if row['condition'] not in ('original', 'adapted'):
        raise ValueError('Unknown condition')
    value = row['demo_error_count']
    score = None if value in ('', None) else float(value)
    if score is not None and (not 0 <= score <= 40 or not score.is_integer()):
        raise ValueError('Demo error count must be an integer from 0 to 40')
    return {**row, 'demo_error_count': score, 'is_synthetic': True}

def read_records(path):
    with Path(path).open(encoding='utf-8', newline='') as handle:
        return [normalize_row(row) for row in csv.DictReader(handle)]
