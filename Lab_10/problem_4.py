import numpy as np

# Create two NumPy arrays
arr1 = np.array([10, 20, 30, 40, 50])
arr2 = np.array([10, 25, 30, 45, 50])

# Find positions where elements match
positions = np.where(arr1 == arr2)

print("Matching positions:", positions[0])