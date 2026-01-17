import numpy as np

s = np.array([1,2,3,np.nan,8,9,10])

print(np.isnan(s))
print(s[~np.isnan(s)])

l = [12,45,67,89,9,2,83]
numparr = np.array(l)
numparr = np.sort(l)
print(numparr)