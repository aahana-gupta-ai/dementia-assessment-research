"""Pair conditions by participant; duplicates and language conflicts fail."""
def paired_differences(records):
    grouped = {}
    for row in records:
        identifier = row['participant_id']
        participant = grouped.setdefault(identifier, {'language': row['language'], 'values': {}})
        if participant['language'] != row['language']:
            raise ValueError('Participant language changes across conditions')
        if row['condition'] in participant['values']:
            raise ValueError('Duplicate participant condition')
        participant['values'][row['condition']] = row['demo_error_count']
    differences = []
    for participant in grouped.values():
        original = participant['values'].get('original')
        adapted = participant['values'].get('adapted')
        if original is not None and adapted is not None:
            differences.append(adapted-original)
    return differences
