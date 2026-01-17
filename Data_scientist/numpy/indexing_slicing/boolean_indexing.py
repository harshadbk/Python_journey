import numpy as np

myarr = np.arange(24).reshape(6,4)

print(myarr)

print(myarr[myarr>12])
print(myarr > 12)
print(myarr[myarr%2==0])