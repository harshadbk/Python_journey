import numpy as np

arr = np.array([12,34,56],dtype=bool)
print(arr)
print(arr.dtype)

# linspace

newarr =np.linspace(-1,1,10).round(2)
print(newarr)

# identity

numarr = np.identity(7)
print(numarr)