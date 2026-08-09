import pandas as pd

# Load Titanic dataset
titanic = pd.read_csv("titanic.csv")

print("Original Dataset:")
print(titanic.head())

print("\nDataset Information:")
titanic.info()


# --------------------------------------------------
# 1. EMPTY CELLS
# --------------------------------------------------

print("\nMissing values before cleaning:")
print(titanic.isnull().sum())

# Fill missing Age values with mean Age
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())

# Fill missing Embarked values with most common value
titanic["Embarked"] = titanic["Embarked"].fillna(
    titanic["Embarked"].mode()[0]
)

# Fill missing Fare values with mean Fare
titanic["Fare"] = titanic["Fare"].fillna(
    titanic["Fare"].mean()
)

print("\nMissing values after cleaning:")
print(titanic.isnull().sum())


# --------------------------------------------------
# 2. WRONG FORMAT
# --------------------------------------------------

# Convert Age and Fare to numeric format
titanic["Age"] = pd.to_numeric(titanic["Age"], errors="coerce")
titanic["Fare"] = pd.to_numeric(titanic["Fare"], errors="coerce")

# Convert Sex and Embarked into category format
titanic["Sex"] = titanic["Sex"].astype("category")
titanic["Embarked"] = titanic["Embarked"].astype("category")

print("\nData types after format cleaning:")
print(titanic.dtypes)


# --------------------------------------------------
# 3. WRONG DATA
# --------------------------------------------------

# Age cannot be negative
titanic.loc[titanic["Age"] < 0, "Age"] = titanic["Age"].mean()

# Fare cannot be negative
titanic.loc[titanic["Fare"] < 0, "Fare"] = titanic["Fare"].mean()

print("\nWrong data cleaned.")


# --------------------------------------------------
# 4. DUPLICATES
# --------------------------------------------------

print("\nNumber of duplicate rows before cleaning:")
print(titanic.duplicated().sum())

# Remove duplicate rows
titanic = titanic.drop_duplicates()

print("\nNumber of duplicate rows after cleaning:")
print(titanic.duplicated().sum())


# --------------------------------------------------
# FINAL DATASET
# --------------------------------------------------

print("\nFinal cleaned Titanic dataset:")
print(titanic.head())

print("\nFinal dataset information:")
titanic.info()