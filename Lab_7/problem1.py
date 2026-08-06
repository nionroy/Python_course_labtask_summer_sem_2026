try:
    # Input two numbers
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    # Division
    result = num1 / num2

    print("Result =", result)

except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")