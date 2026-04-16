'''
Program: Read CSV and plot scatter graphs using Matplotlib
'''

import pandas as pd
import matplotlib.pyplot as plt

# Read CSV
df = pd.read_csv("health_data.csv")

# Scatter plots
plt.scatter(df["weight"], df["height"])
plt.xlabel("Weight")
plt.ylabel("Height")
plt.title("Weight vs Height")
plt.show()

plt.scatter(df["age"], df["weight"])
plt.xlabel("Age")
plt.ylabel("Weight")
plt.title("Age vs Weight")
plt.show()

plt.scatter(df["height"], df["age"])
plt.xlabel("Height")
plt.ylabel("Age")
plt.title("Height vs Age")
plt.show()

plt.scatter(df["gender"], df["height"])
plt.xlabel("Gender")
plt.ylabel("Height")
plt.title("Gender vs Height")
plt.show()

plt.scatter(df["gender"], df["weight"])
plt.xlabel("Gender")
plt.ylabel("Weight")
plt.title("Gender vs Weight")
plt.show()
