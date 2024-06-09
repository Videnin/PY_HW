def generate_cube_numbers(limit):
    """Генератор кубов чисел от 2 до указанной величины."""
    num = 2
    while True:
        cube = num ** 3
        if cube >= limit:
            return
        yield cube
        num += 1
