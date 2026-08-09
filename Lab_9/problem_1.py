import pandas as pd
import matplotlib.pyplot as plt

# Load Titanic dataset
titanic = pd.read_csv("titanic.csv")

# Display dataset information
print("First 5 rows:")
print(titanic.head())

print("\nLast 5 rows:")
print(titanic.tail())

print("\nDataset Information:")
titanic.info()

# Fill missing Age values
titanic["Age"] = titanic["Age"].fillna(titanic["Age"].mean())


# --------------------------------------------------
# 1. LINE PLOT
# Age of passengers
# --------------------------------------------------

plt.figure()
plt.plot(titanic.index, titanic["Age"])
plt.title("Line Plot - Age of Passengers")
plt.xlabel("Passenger Index")
plt.ylabel("Age")
plt.show()


# --------------------------------------------------
# 2. SCATTER PLOT
# Age vs Fare
# --------------------------------------------------

plt.figure()
plt.scatter(titanic["Age"], titanic["Fare"])
plt.title("Scatter Plot - Age vs Fare")
plt.xlabel("Age")
plt.ylabel("Fare")
plt.show()


# --------------------------------------------------
# 3. BAR CHART
# Number of passengers in each class
# --------------------------------------------------

class_count = titanic["Pclass"].value_counts().sort_index()

plt.figure()
plt.bar(
    class_count.index.astype(str),
    class_count.values
)
plt.title("Bar Chart - Passengers per Class")
plt.xlabel("Passenger Class")
plt.ylabel("Number of Passengers")
plt.show()


# --------------------------------------------------
# 4. HISTOGRAM
# Age distribution
# --------------------------------------------------

plt.figure()
plt.hist(titanic["Age"], bins=10, edgecolor="black")
plt.title("Histogram - Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()


# --------------------------------------------------
# 5. PIE CHART
# Survived vs Not Survived
# --------------------------------------------------

survived_count = titanic["Survived"].value_counts().sort_index()

plt.figure()
plt.pie(
    survived_count.values,
    labels=["Not Survived", "Survived"],
    autopct="%1.1f%%"
)
plt.title("Pie Chart - Survival Rate")
plt.show()


# --------------------------------------------------
# 6. SUBPLOTS
# --------------------------------------------------

fig, ax = plt.subplots(2, 2, figsize=(10, 8))

# Line plot
ax[0, 0].plot(titanic.index, titanic["Age"])
ax[0, 0].set_title("Line Plot - Age")

# Scatter plot
ax[0, 1].scatter(titanic["Age"], titanic["Fare"])
ax[0, 1].set_title("Scatter Plot - Age vs Fare")

# Histogram
ax[1, 0].hist(titanic["Age"], bins=10, edgecolor="black")
ax[1, 0].set_title("Histogram - Age")

# Pie chart
ax[1, 1].pie(
    survived_count.values,
    labels=["Not Survived", "Survived"],
    autopct="%1.1f%%"
)
ax[1, 1].set_title("Pie Chart - Survival")

plt.tight_layout()
plt.show()