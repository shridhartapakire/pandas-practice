# Pandas Day 3 - Filtering & Selecting Data

import pandas as pd

# Load data
df = pd.read_csv("data.csv")

print("Full Data:\n", df)

# 1. Select column
print("\nNames column:\n", df["Name"])

# 2. Select multiple columns
print("\nName and Marks:\n", df[["Name", "Marks"]])

# 3. Filter rows (Marks > 85)
high_marks = df[df["Marks"] > 85]
print("\nMarks > 85:\n", high_marks)

# 4. Filter rows (Age == 20)
age_20 = df[df["Age"] == 20]
print("\nAge = 20:\n", age_20)

# 5. Multiple conditions
filtered = df[(df["Marks"] > 80) & (df["Age"] >= 20)]
print("\nMarks > 80 AND Age >= 20:\n", filtered)

# 6. Using loc
print("\nUsing loc (Name & Marks):\n", df.loc[:, ["Name", "Marks"]])