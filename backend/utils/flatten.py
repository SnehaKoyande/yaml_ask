def flatten_dict(d, parent_key='', sep='.'):
    items = []
    if isinstance(d, list):
        for i, v in enumerate(d):
            items.extend(flatten_dict(v, f"{parent_key}[{i}]", sep=sep).items())
    elif isinstance(d, dict):
        for k, v in d.items():
            new_key = f"{parent_key}{sep}{k}" if parent_key else k
            items.extend(flatten_dict(v, new_key, sep=sep).items())
    else:
        items.append((parent_key, d))
    return dict(items)
