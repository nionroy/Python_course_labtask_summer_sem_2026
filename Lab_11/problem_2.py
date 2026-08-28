import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 20, 40, 20, 50, 20])

# Item to search
item = 20

# nth repetition
n = 3

# Find all positions of the item
positions = np.where(arr == item)[0]

# Find the index of nth repetition
index = positions[n - 1]

print("Index of", n, "rd repetition of", item, ":", index)