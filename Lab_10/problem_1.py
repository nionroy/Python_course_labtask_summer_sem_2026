import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6])

print("Original array:")
print(arr)

# Change the shape from 1D to 2D
new_arr = arr.reshape(2, 3)

print("\nReshaped array:")
print(new_arr)