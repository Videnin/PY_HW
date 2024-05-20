import string
import keyword

def is_valid_variable_name(name):
    if name in keyword.kwlist:
        return False
    if name.count('_') > 1:
        return False
    if name[0].isdigit():
        return False
    for char in name:
        if char in string.ascii_uppercase or char in string.punctuation.replace('_', '') or char.isspace():
            return False
    return True

examples = [
    "_",               # True
    "__",              # False
    "___",             # False
    "x",               # True
    "get_value",       # True
    "get value",       # False
    "get!value",       # False
    "some_super_puper_value",  # True
    "Get_value",       # False
    "get_Value",       # False
    "getValue",        # False
    "3m",              # False
    "m3",              # True
    "assert",          # False
    "assert_exception" # True
]

for example in examples:
    print(f"{example}: {is_valid_variable_name(example)}")
