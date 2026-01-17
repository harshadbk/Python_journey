import numpy as np

arr = np.array([12,45,67,87,22,39,81,14])

# resarr = arr.reshape(4,2)
# print(resarr)

oddarr = arr[arr%2==0]
print(oddarr)

# mapping elements in array 

mapped_ele = arr+2
print(mapped_ele)

mylist = [12,34,21,90,62,80]
oddlist = list(filter(lambda x:x%2==0,mylist))
print(oddlist)