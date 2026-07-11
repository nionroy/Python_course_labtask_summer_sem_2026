# Given list
numbers = [10, 20, 30, 20, 50]

# Empty list to store unique values
new_list = []

# Check each number
for i in numbers:
    if i not in new_list:
        new_list.append(i)

# Print the new list
print("List after removing duplicates:")
print(new_list)