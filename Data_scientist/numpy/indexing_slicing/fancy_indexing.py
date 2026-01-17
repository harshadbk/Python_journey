import numpy as np

myarr = np.arange(18).reshape(6,3)

print(myarr)

print(myarr[[1,2,3]])

myarr[:,[1,2]] = [[ 2, 1],
 [5,4],
 [8,7],
 [11,10],
 [14,13],
 [17,16]]

print(myarr)



