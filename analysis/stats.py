"""Small transparent descriptive statistics without external dependencies."""
import math

def mean(values):
    if any(not isinstance(v, (int, float)) or not math.isfinite(v) for v in values):
        raise ValueError('Finite numbers required')
    return sum(values) / len(values) if values else None

def variance(values):
    m = mean(values)
    return sum((x-m)**2 for x in values) / (len(values)-1) if len(values)>1 else None

def quantile(values, p):
    if not 0 <= p <= 1:
        raise ValueError('Quantile probability must lie between zero and one')
    mean(values)
    if not values:
        return None
    ordered = sorted(values)
    pos = (len(values)-1)*p
    lo, hi = math.floor(pos), math.ceil(pos)
    return ordered[lo] + (ordered[hi]-ordered[lo])*(pos-lo)
