try:
    # Create a list
    numbers = [10, 20, 30, 40, 50]

    # Take index from the user
    index = int(input("Enter the index: "))

    # Access the list element
    print("Element =", numbers[index])

except IndexError:
    print("Error: Index is out of range.")

except TypeError:
    print("Error: Index must be an integer.")

except ValueError:
    print("Error: Please enter a valid integer.")