import string

def get_chars_between(input_str):
    start_char, end_char = input_str.split('-')
    all_letters = string.ascii_letters
    start_index = all_letters.index(start_char)
    end_index = all_letters.index(end_char)
    return all_letters[start_index:end_index + 1]

input_str = input("2 буквы через -: ")
result = get_chars_between(input_str)
print(result)
