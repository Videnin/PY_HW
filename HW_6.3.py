def multiply_digits(number):
    result = 1
    while number > 0:
        digit = number % 10
        if digit == 0:
            return 0
        result *= digit
        number //= 10
    return result

user_input = int(input("Введите целое число: "))
while multiply_digits(user_input) > 9:
    user_input = multiply_digits(user_input)

print("Result:", user_input)
