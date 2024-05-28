def second_index(string: str, target: str) -> int:
    first_index = string.find(target)
    if first_index != -1:
        second_index = string.find(target, first_index + 1)
        if second_index != -1:
            return second_index
    return None
