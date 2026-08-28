import numpy as np

# Create a NumPy array
arr = np.array([[1, 2, 3],
                [4, 5, 6],
                [7, 8, 9]])

# Sum of each column
column_sum = np.sum(arr, axis=0)

# Sum of each row
row_sum = np.sum(arr, axis=1)

print("Array:")
print(arr)

print("Sum of each column:", column_sum)
print("Sum of each row:", row_sum)