# Create a list
numbers = [12, 45, 7, 89, 23, 56]

# Assume the first number is both maximum and minimum
maximum = numbers[0]
minimum = numbers[0]

# Check every number
for i in numbers:
    if i > maximum:
        maximum = i

    if i < minimum:
        minimum = i

# Print the results
print("Maximum value =", maximum)
print("Minimum value =", minimum)