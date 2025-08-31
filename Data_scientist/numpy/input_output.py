import numpy as np

arr = np.loadtxt("data.txt")
print(arr)

#  2. np.savetxt() – Writing to a Text File

arr = np.array([[10, 20, 30],
                [40, 50, 60]])

np.savetxt("lineoutput.txt",arr,fmt='%d')
