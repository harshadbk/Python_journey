import pandas as pd
import numpy as np

data = [1,2,3,4,5]
data2 = [6,7,8,9,10]

my_series=(pd.Series(data))
myseries=pd.Series(data2)

my_series=my_series.astype(np.int32)

print(pd.Series(my_series))

# with Dictonary

data = {'a':1,'b':2,'c':3,'d':4,'e':5}

my_series2 = pd.Series(data)

print(my_series2)

# Indexing and Slicing

# print(my_series2[0])
print(my_series2.iloc[0])
print(my_series2['c'])
print(my_series2[0:2])
print(my_series2[['a','b']])

# 3. Series Operations

print(my_series2 + 2)
print(my_series + myseries)

# boolean operation

print((my_series2 > 2) & (my_series2 < 5))

#  Series with Dictionaries and Lists

new_data = {'a':11,'b':12,'c':13,'d':14,'e':15,'f':16}

print(pd.Series(new_data))

# with List

new_list = [21,22,23,24,25,26,27,None]
new_series = pd.Series(new_list,index=['z','x','x','y','w','k','m','o'])
print(new_series[0:4])

# Attributes

print(new_series.index)
print(new_series.values)
print(new_series.dtype)
print(new_series.head(3))
print(new_series.tail(3))
print(new_series.describe)
print(new_series.isnull())
print(new_series.dropna())