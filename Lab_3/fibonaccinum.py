num = int (input("enter a number: "))
if num < 0:
    print("please enter a positive number")
else:
    # Generate Fibonacci sequence up to the entered number
    a, b = 0, 1
    while a <= num:
        print(a, end=" ")
        a, b = b, a + b