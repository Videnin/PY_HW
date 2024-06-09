def is_even(number):
    """ проверка парности """
    binary_representation = bin(number)
    return binary_representation[-1] == '0'
