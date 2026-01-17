import numpy as np

arr1 = np.array([[2,3],[4,5],[6,7],[16,17]])

print(np.hsplit(arr1,2))
print(np.vsplit(arr1,2))

print(arr1.ravel())
print(arr1.flatten())