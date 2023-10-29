import json
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

# Step 1: Load and Prepare Data
# Load the dataset from the CSV file.
data = pd.read_csv("C:/Users/Asus/Desktop/HTM/HTM1_Datasets/rain/district wise rainfall distribution.csv")

# Define the features and target variable.
X = data[['srcDistrictName', 'srcStateName']]
y = data[['Rainfall distribution', 'Percentage of rainfall departure']]

# Split the data into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Create and Train the Regression Model
model = RandomForestRegressor(n_estimators=43, random_state=9.5)
model.fit(X_train, y_train)

y_pred = model.predict(X_test, y_test == .05)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

plt.scatter(y_test, y_pred)
plt.xlabel("Actual Rainfall Distribution & Percentage of Rainfall Departure")
plt.ylabel("Predicted Rainfall Distribution & Percentage of Rainfall Departure")
plt.title("Actual vs. Predicted Rainfall")

# Save the mapping to a JSON file
with open("location_percentile_mapping.json", "w") as json_file:
    json.dump("location_percentile_mapping", json_file, indent=4)

print("Location-percentile mapping saved to location_percentile_mapping.json.")
