"""
Lab: Diabetes Prediction using Decision Tree Classifier
Dataset: Diabetes Health Indicators (BRFSS 2015) - Kaggle
Steps:
  1. Load the dataset into a DataFrame
  2. Split the dataset into training and testing sets
  3. Apply feature scaling
  4. Load the Decision Tree model
  5. Train the model using fit()
  6. Make predictions for test data
  7. Evaluate the model and calculate accuracy
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
)

# -----------------------------------------------------------------
# Step 1: Load the dataset into a DataFrame
# -----------------------------------------------------------------
DATA_PATH = "C:\\Users\\niladri roy nion\\Desktop\\python LAB TASK\\Lab_12\\diabetes_012_health_indicators_BRFSS2015.csv"
df = pd.read_csv(DATA_PATH)

print("Shape of dataset:", df.shape)
print("\nFirst 5 rows:")
print(df.head())
print("\nClass distribution (Diabetes_012):")
print(df["Diabetes_012"].value_counts())

# Separate features (X) and target (y)
# Diabetes_012 -> 0 = no diabetes, 1 = prediabetes, 2 = diabetes
X = df.drop(columns=["Diabetes_012"])
y = df["Diabetes_012"]

# -----------------------------------------------------------------
# Step 2: Split the dataset into training and testing sets
# -----------------------------------------------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

print("\nTraining set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)

# -----------------------------------------------------------------
# Step 3: Apply feature scaling
# -----------------------------------------------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # fit on train only
X_test_scaled = scaler.transform(X_test)          # transform test using same scaler

# -----------------------------------------------------------------
# Step 4: Load the Decision Tree model
# -----------------------------------------------------------------
dt_model = DecisionTreeClassifier(
    criterion="gini",
    max_depth=10,       # limits depth to reduce overfitting
    random_state=42
)

# -----------------------------------------------------------------
# Step 5: Train the model using fit()
# -----------------------------------------------------------------
dt_model.fit(X_train_scaled, y_train)

# -----------------------------------------------------------------
# Step 6: Make predictions for test data
# -----------------------------------------------------------------
y_pred = dt_model.predict(X_test_scaled)

# -----------------------------------------------------------------
# Step 7: Evaluate the model and calculate accuracy
# -----------------------------------------------------------------
accuracy = accuracy_score(y_test, y_pred)
print(f"\nModel Accuracy: {accuracy * 100:.2f}%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# -----------------------------------------------------------------
# Feature importance (bonus - shows which features mattered most)
# -----------------------------------------------------------------
importances = pd.Series(dt_model.feature_importances_, index=X.columns)
importances = importances.sort_values(ascending=False)
print("\nTop 10 Most Important Features:")
print(importances.head(10))