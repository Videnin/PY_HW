def move_last_to_first(lst):
    if len(lst) > 1:
        last_element = lst.pop()
        lst.insert(0, last_element)
    return lst

# Examples
examples = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]

for lst in examples:
    modified_list = move_last_to_first(lst)
    print(modified_list)


