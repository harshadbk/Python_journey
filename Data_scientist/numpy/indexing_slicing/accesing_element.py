import numpy as np

arr = np.array([10,20,30,40,50])

print(arr)
# accesing index
print(arr[0])
print(arr[::-1])
print(arr[3])

arr2 = np.array([[1,2,3,10],
                 [4,5,6,11],
                 [7,8,9,12]
                ])
print(arr2)

print(arr2[::2,::3])
print(arr2[::2])
print(arr2[::2 ,1::2])
print(arr2[0::2,2::])
print(arr2[1::,0:2])