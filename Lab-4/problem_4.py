def distinct_list(lst):
    new_list = []

    for item in lst:
        if item not in new_list:
            new_list.append(item)

    return new_list

# Sample List
numbers = [1, 2, 3, 3, 3, 3, 4, 5]

print("Original List:", numbers)
print("Distinct List:", distinct_list(numbers))