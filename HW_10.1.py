def sequence_generator(func, start, n):
    current = start
    for _ in range(n):
        yield current
        current = func(current)
