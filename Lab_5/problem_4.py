# Sorted list
numbers = [10, 20, 30, 40, 50]

search = int(input("Enter value to search: "))

low = 0
high = len(numbers) - 1
found = False

while low <= high:
    mid = (low + high) // 2

    if numbers[mid] == search:
        found = True
        break
    elif search > numbers[mid]:
        low = mid + 1
    else:
        high = mid - 1

if found:
    print("Value found.")
else:
    print("Value not found.")