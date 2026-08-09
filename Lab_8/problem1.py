import pandas as pd

calories = {
    "day1": 420,
    "day2": 380,
    "day3": 390
}

# Create Pandas Series
s = pd.Series(calories)

# Display the Series
print("Calories:")
print(s)

# Find the summation
total = s.sum()

print("Total calories:", total)