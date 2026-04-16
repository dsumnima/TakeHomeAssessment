'''
Program: Add BMI and Health_Status columns using Pandas
'''

import pandas as pd

# Read CSV
df = pd.read_csv("health_data.csv")

# Correct BMI calculation
df["BMI"] = df["weight"] / ((df["height"] / 100) ** 2)

# Function to assign health status
def get_status(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi <= 24.9:
        return "Healthy"
    elif 25 <= bmi <= 29.9:
        return "Overweight"
    elif 30 <= bmi <= 34.9:
        return "High Risk"
    else:
        return "Critical"   # fixed logic

# Apply function
df["Health_Status"] = df["BMI"].apply(get_status)

# Display result
print(df)