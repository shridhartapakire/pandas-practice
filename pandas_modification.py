# Pandas Day 4 - Adding, Updating, Deleting Columns

import pandas as pd

# Load data
df = pd.read_csv("data.csv")

print("Original Data:\n", df)

# 1. Add new column (Pass/Fail)
df["Status"] = df["Marks"] > 80
print("\nAdded Status column:\n", df)

# 2. Update column values (convert boolean to text)
df["Status"] = df["Status"].map({True: "Pass", False: "Fail"})
print("\nUpdated Status column:\n", df)

# 3. Add another column (Bonus Marks)
df["Bonus"] = df["Marks"] + 5
print("\nAdded Bonus column:\n", df)

# 4. Delete column
df = df.drop("Bonus", axis=1)
print("\nAfter deleting Bonus column:\n", df)

# 5. Rename column
df = df.rename(columns={"Marks": "Score"})
print("\nAfter renaming column:\n", df)   