import numpy as np

arr1 = np.array([[2,3],[4,5],[6,7],[16,17]])
arr2 = np.array([[8,9],[10,11],[12,13],[14,15]])

arr3 = np.vstack((arr1,arr2))
print(arr3)

arr4 = np.hstack((arr1,arr2))
print(arr4)
