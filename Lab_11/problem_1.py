import numpy as np

# Create a NumPy array
arr = np.array([10, 5, 8, 2, 15, 3, 7])

# Value of K
K = 3

# Find K-smallest values
smallest = np.sort(arr)[:K]

print("K-smallest values:", smallest)