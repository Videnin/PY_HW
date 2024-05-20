def calculator():
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))

            if operation == '+':
                result = num1 + num2
            elif operation == '-':
                result = num1 - num2
            elif operation == '*':
                result = num1 * num2
            elif operation == '/':
                if num2 != 0:
                    result = num1 / num2
                else:
                    print("Cannot divide by zero!")
                    continue
            else:
                print("Invalid operation!")
                continue

            print(f"The result is: {result}")

        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        cont = input("Do you want to continue? (yes/y to continue): ").strip().lower()
        if cont != 'yes' and cont != 'y':
            break


calculator()
