import numpy as np

# Create a NumPy array
arr = np.array([10, -5, 20, -8, 30, -2, 40])

# Replace negative values with 0
arr[arr < 0] = 0

print("Array after replacing negative values:")
print(arr)