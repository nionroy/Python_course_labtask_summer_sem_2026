# Given list
numbers = [10, 20, 30, 20, 50]

# Loop through the list
for i in range(len(numbers)):
    if numbers[i] == 20:
        numbers[i] = 200

# Print updated list
print(numbers)