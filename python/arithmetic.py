def perform_operations():
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input. Please enter numeric values.")
        return
    print("Addition:", num1 + num2)
    print("Subtraction:", num1 - num2)
    print("Multiplication:", num1 * num2)
    print("Division (float):", num1 / num2)
    print("Floor Division:", num1 // num2)
    print("Modulo:", num1 % num2)
    print("Exponential:", num1 ** num2)
perform_operations()
