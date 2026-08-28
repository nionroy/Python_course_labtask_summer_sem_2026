import numpy as np

# Create two NumPy arrays
arr1 = np.array([10, 20, 30, 40])
arr2 = np.array([2, 4, 6, 8])

# Summation
summation = np.sum(arr1) + np.sum(arr2)

# Product
product = np.prod(arr1) * np.prod(arr2)

# Difference
difference = np.diff(arr1) - np.diff(arr2)

# Display results
print("Summation:", summation)
print("Product:", product)
print("Difference:", difference)