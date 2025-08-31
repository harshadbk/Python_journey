import pandas as pd

csv_data = pd.read_csv("lineoutput.csv", header=0, skiprows=[1, 2],nrows=4, na_values=["NA", "Not Available", "Missing"])

dframe = pd.DataFrame(csv_data)

print(dframe)
print(csv_data.head(2))
print(csv_data.tail(3))
