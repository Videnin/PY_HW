def split_list(lst):
    middle = len(lst) // 2
    first_list = lst[:middle]
    second_list = lst[middle:]
    return [first_list, second_list]

examples = [
    [3, 3, 2, 3],
    [1],
    [],
    [13, 32, 42, 108, 811]
]

for lst in examples:
    split_lists = split_list(lst)
    print(split_lists)


