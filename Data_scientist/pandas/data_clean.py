import pandas as pd

df = pd.read_csv("lineoutput.csv",header=0)

dataframe = pd.DataFrame(df)

print(dataframe.columns)

print(dataframe.isnull())

dataframe[a] = dataframe[a].fillna(0,inplace=True)

print(dataframe)
