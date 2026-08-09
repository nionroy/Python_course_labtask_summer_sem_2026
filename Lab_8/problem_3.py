import pandas as pd

# Load CSV file
titanic = pd.read_csv("titanic.csv")

# Display first 5 rows
print("First 5 rows:")
print(titanic.head())

# Display last 5 rows
print("\nLast 5 rows:")
print(titanic.tail())

# Display information about dataset
print("\nDataset Information:")
print(titanic.info())