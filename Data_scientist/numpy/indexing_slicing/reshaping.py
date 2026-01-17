import numpy as np

arr = np.array([12,45,67,87,22,39,81,14])

arr2d = arr.reshape(2,4) #if (2,3) data will get lost and we will get error
print(arr2d)

# now i will understnad you flatten method

flatted_array = arr2d.flatten() #retuurns copy 
print(flatted_array)

flatted_array = arr2d.ravel() # returns view it will change original array
print(flatted_array)
