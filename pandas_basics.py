# Pandas Day 1 - Basics

import pandas as pd

# 1. Creating a Series
data = [10, 20, 30, 40]
series = pd.Series(data)
print("Series:\n", series)

# 2. Creating a DataFrame
data_dict = {
    "Name": ["John", "Alice", "Bob"],
    "Marks": [85, 90, 78]
}

df = pd.DataFrame(data_dict)
print("\nDataFrame:\n", df)

# 3. Basic info
print("\nShape:", df.shape)
print("\nColumns:", df.columns)

# 4. Accessing data
print("\nNames column:\n", df["Name"])
print("\nFirst row:\n", df.iloc[0])