def difference(*args):
    if not args:
        return 0
    max_value = max(args)
    min_value = min(args)
    return round(max_value - min_value, 2)
