import numpy as np

size_arr = np.array([[1,2,3]],dtype=int)

print(size_arr.size)

# item size 

print(size_arr.dtype)
print(size_arr.itemsize)

size_arr = size_arr.astype(float)
print(size_arr.dtype)
