import numpy as np

arr2d = np.array([10,20,30,40,50,60])

print(arr2d)
print(arr2d[2::-1])
print(arr2d[0:arr2d.size:1])
print(arr2d[2:0:-1])

# fancy indexing

print(arr2d[[0,2,4,5]])
