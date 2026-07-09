"""Percentile bootstrap of participant-level paired differences."""
import random
from .stats import mean, quantile

def bootstrap_interval(values, replicates=1000, seed=42):
    if not isinstance(replicates, int) or replicates < 100 or replicates > 100000:
        raise ValueError('Use 100 to 100000 replicates')
    if not values:
        return None
    mean(values)
    generator = random.Random(seed)
    estimates = [mean([generator.choice(values) for _ in values]) for _ in range(replicates)]
    return {'lower': quantile(estimates, .025), 'upper': quantile(estimates, .975), 'replicates': replicates, 'seed': seed, 'method': 'paired-percentile-bootstrap'}
