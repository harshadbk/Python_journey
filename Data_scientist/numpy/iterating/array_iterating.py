import numpy as np

myarr = np.array([12,19,32,71,30])

for i in myarr:
    print(i, end=" ")
print("\n")

myarr2 = np.arange(24).reshape(4,6)

print(myarr2)

for i in myarr2:
    print(i)

# another way to print this is to first convert it into 1d array and print all elemets

for i in np.nditer(myarr2):
    print(i,end=" ")