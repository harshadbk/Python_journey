import pandas as pd
import numpy as np

# From a Dictionary

data = {
    'name':['q','w','e','r','t','y'],
    'city':['a','s','d','f','j','k'],
    'age':[12,23,31,25,18,21]
}

data_frame1 = pd.DataFrame(data)
print(data_frame1)

# from list to lists

data = [
    ['Amit', 25, 'Pune'],
    ['Sneha', 30, 'Mumbai'],
    ['Ravi', 22, 'Nashik']
]

df = pd.DataFrame(data, columns=['Name', 'Age', 'City'])
print(df)

# From a NumPy Array

numpy_array = np.array([[1,2,3],[4,5,6]])

numpy_dictionary = pd.DataFrame(numpy_array,columns=['col1','col2','col3'])

print(numpy_dictionary)

# reading from txt file 

df = pd.read_csv("lineoutput.csv", header=None)
print(df)

# Attributes of Dataframes

print(data_frame1.shape)
print(data_frame1.columns)
print(data_frame1.dtypes)
print(data_frame1.index)
print(data_frame1.tail(2))
print(data_frame1.head(2))
print(data_frame1.info())
print(data_frame1.describe())