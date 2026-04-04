# Pandas Day 2 - Reading CSV & Inspection

import pandas as pd

# 1. Read CSV file
df = pd.read_csv("data.csv")

# 2. View data
print("Full Data:\n", df)

# 3. First 3 rows
print("\nFirst 3 rows:\n", df.head(3))

# 4. Last rows
print("\nLast rows:\n", df.tail())

# 5. Info about dataset
print("\nInfo:")
print(df.info())

# 6. Summary statistics
print("\nStatistics:\n", df.describe())