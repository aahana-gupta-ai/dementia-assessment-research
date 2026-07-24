"""Render an explicitly synthetic Markdown report."""
def markdown_report(summary):
    def display(value):
        return 'not available' if value is None else f'{value:.4f}' if isinstance(value, float) else str(value)
    lines = ['# Synthetic demonstration report', '', 'Generated example data only. These are not clinical findings.', '', '| Metric | Value |', '| --- | --- |']
    for key in ['rows', 'participants', 'missing_rows', 'complete_pairs', 'original_mean', 'adapted_mean', 'mean_paired_difference']:
        lines.append(f'| {key} | {display(summary[key])} |')
    interval = summary['interval']
    if interval:
        lines.extend(['', f"95% percentile interval: {interval['lower']:.4f} to {interval['upper']:.4f}. Resampling unit: participant paired difference."])
    lines.extend(['', 'No hypothesis test or diagnostic conclusion is produced.'])
    return '\n'.join(lines)+'\n'
