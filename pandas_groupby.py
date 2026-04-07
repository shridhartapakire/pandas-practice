# Pandas Day 5 - GroupBy & Aggregation

import pandas as pd

# Load data
df = pd.read_csv("data.csv")

print("Original Data:\n", df)

# 1. Group by Age and calculate mean marks
grouped_mean = df.groupby("Age")["Marks"].mean()
print("\nAverage Marks by Age:\n", grouped_mean)

# 2. Group by Age and calculate sum
grouped_sum = df.groupby("Age")["Marks"].sum()
print("\nTotal Marks by Age:\n", grouped_sum)

# 3. Multiple aggregations
grouped_multi = df.groupby("Age")["Marks"].agg(["mean", "max", "min"])
print("\nMultiple Aggregations:\n", grouped_multi)

# 4. Count values
count = df.groupby("Age")["Name"].count()
print("\nCount of Students by Age:\n", count)