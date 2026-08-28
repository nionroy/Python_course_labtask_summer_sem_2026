import numpy as np

# Create a NumPy array
arr = np.array([10, 20, 30, 40, 50, 30])

# Value to search
value = 30

# Find the positions of the value
positions = np.where(arr == value)

print("Array:", arr)
print("Positions of", value, ":", positions[0])