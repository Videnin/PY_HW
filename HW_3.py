
# Програма має виконувати прості математичні дії (+, -, *, /).
# ористувачеві пропонується почерзі ввести числа та дію над цими числами, а програма, виходячи з дії,
# обчислює та друкує результат.

# Зробити перевірку на те, що при діленні дільник не дорівнює 0!

# ДЗ необхідно здати наступним чином:

# Посилання на файл ДЗ на GitHub:
# Або

# Додайте файл до відповіді на домашнє завдання в систему управління навчанням (ЛМС).


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


