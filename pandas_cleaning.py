# Pandas Day 6 - Handling Missing Data & Practice

import pandas as pd
import numpy as np

# Create dataset with missing values
data = {
    "Name": ["John", "Alice", "Bob", "David", "Emma"],
    "Age": [20, 21, None, 22, None],
    "Marks": [85, None, 78, 88, 95]
}

df = pd.DataFrame(data)

print("Original Data:\n", df)

# 1. Check missing values
print("\nMissing Values:\n", df.isnull())

# 2. Count missing values
print("\nMissing Count:\n", df.isnull().sum())

# 3. Fill missing values
df["Age"].fillna(df["Age"].mean(), inplace=True)
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

print("\nAfter Filling Missing Values:\n", df)

# 4. Drop missing values (example)
df_dropped = df.dropna()
print("\nAfter Dropping Missing Values:\n", df_dropped)

# 5. Final summary
print("\nSummary:\n", df.describe())