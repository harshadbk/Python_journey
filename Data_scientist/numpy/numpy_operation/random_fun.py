import numpy as np

arr = np.random.random((3,3)).round(2)
print(arr)

modarr = arr*100
print(modarr)
modarr = modarr.astype(int)

print(np.max(modarr))

print(np.max(modarr,axis=1))

myarr = np.array([1.2,3.4,5.1,2.0,9.2])
print(np.ceil(myarr))
print(np.floor(myarr))