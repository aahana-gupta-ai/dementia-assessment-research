"""New synthetic-data demonstration package, with no original patient records."""
from .io import read_records
from .summary import summarize
__all__ = ['read_records', 'summarize']
