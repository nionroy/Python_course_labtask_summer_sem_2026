import pandas as pd

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the complete DataFrame
print("Complete DataFrame:")
print(df)

# Select rows 0 and 2 using loc
print("\nRows 0 and 2:")
print(df.loc[[0, 2]])