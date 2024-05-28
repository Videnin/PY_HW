def common_elements():
    multiples_of_3 = {x for x in range(3, 301, 3)}
    multiples_of_5 = {x for x in range(5, 501, 5)}
    common_set = multiples_of_3.intersection(multiples_of_5)

    return common_set
