# 1. Add a scalar value to all elements
import numpy as np

arr = np.array([23,45,67,43,21,10,29,17])

newarr = arr+2
print(newarr)

# 2. Subtract a 1D array from each row of a 2D array

arr2d = arr.reshape(2,4)
print(arr2d)

myrow = np.array([2,3,4,5])

result = arr2d - myrow
print(result)

# 3. Multiply each column by a different scalar

newmul = np.array([2,3,4,5])
result = arr2d * newmul
print(result)

# 4. normalizing an array

result = ((arr-arr.min()) / (arr.max() - arr.min())).round(2)

print(result)

# 5. Add two broadcast-compatible arrays of different shapes

arr3d = np.array([[1],[2],[3]])
arr_flat = np.array([4,5,6])

result = arr3d + arr_flat
print(result)