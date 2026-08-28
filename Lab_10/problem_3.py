import numpy as np

# Create a NumPy array
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Filter even numbers
even_numbers = arr[arr % 2 == 0]

print("Even numbers:", even_numbers)