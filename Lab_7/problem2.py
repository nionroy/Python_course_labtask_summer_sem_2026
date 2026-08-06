try:
    # Take input from the user
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Check if the inputs are numbers
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs must be numerical.")

    # Convert to integers
    num1 = int(num1)
    num2 = int(num2)

    # Display the numbers
    print("First Number =", num1)
    print("Second Number =", num2)

except TypeError as e:
    print("Error:", e)