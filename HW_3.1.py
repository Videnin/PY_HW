def split_list(lst):
    middle = len(lst) // 2
    first_list = lst[:middle]
    second_list = lst[middle:]
    return [first_list, second_list]

examples = [
    [777, 7, 7, 777],
    [7],
    [],
    [777, 7, 7, 7, 7]
]

for lst in examples:
    split_lists = split_list(lst)
    print(split_lists)

