# film_rating = int(input("Enter film rating: "))
# if 0 < film_rating < + 5:
#     if film_rating == 4 or film_rating == 5:
#         print("Film OK")
#     else:
#         print("Film govno")
# else:
#     print("Incorrect!")


def calculate(number1, number2, operator):
    if operator == '+':
        return number1 + number2
    elif operator == '-':
        return number1 - number2
    elif operator == '*':
        return number1 * number2
    elif operator == '/':
        if number2 != 0:
            return number1 / number2
        else:
            return "Error: Division by zero"
    else:
        return "Unsupported operation"


while True:
    number1 = float(input("Enter the first number: "))
    number2 = float(input("Enter the second number: "))
    operator = input("Enter the operation (+, -, *, /): ")

    result = calculate(number1, number2, operator)
    print("Result:", result)


