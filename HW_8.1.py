def add_one(digits):
    number = int(''.join(map(str, digits))) + 1
    result = list(map(int, str(number)))
    return result
