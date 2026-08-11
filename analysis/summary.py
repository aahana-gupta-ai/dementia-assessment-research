"""Summarise synthetic observations and complete paired differences."""
from .stats import mean
from .pairs import paired_differences
from .bootstrap import bootstrap_interval

def summarize(records, replicates=1000, seed=42):
    differences = paired_differences(records)
    original = [r['demo_error_count'] for r in records if r['condition']=='original' and r['demo_error_count'] is not None]
    adapted = [r['demo_error_count'] for r in records if r['condition']=='adapted' and r['demo_error_count'] is not None]
    return {'is_synthetic': True, 'rows': len(records), 'participants': len({r['participant_id'] for r in records}), 'missing_rows': sum(r['demo_error_count'] is None for r in records), 'original_mean': mean(original), 'adapted_mean': mean(adapted), 'complete_pairs': len(differences), 'mean_paired_difference': mean(differences), 'interval': bootstrap_interval(differences, replicates, seed)}
