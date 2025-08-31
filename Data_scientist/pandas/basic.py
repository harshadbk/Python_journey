import pandas as pd
import numpy as np

print("Hello pandas")

"""
Pandas is an open-source Python library used for data analysis and manipulation.
It provides high-performance, easy-to-use data structures and tools for working with structured (tables, time-series) data.
🔑 Key Features:
Built on top of NumPy
Handles tabular data (like SQL tables or Excel)
Supports:
Cleaning, filtering, transforming data
Aggregating and grouping
Reading from and writing to files (CSV, Excel, etc.)
Time series analysis
"""

# Series

data = pd.Series([1,2,3,4,5])
print(data)

data = data.astype(np.int32)
print(data)

# Dataframe

data = {
    'name':["HK","LK","SK","DK","NK"],
    'Age':[12,34,54,12,34]
}

df = pd.DataFrame(data)
print(df)

df = df.columns(["HK3","HK4"])

print(df)