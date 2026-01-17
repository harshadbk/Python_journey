import numpy as np

arr = np.array([23,45,67,43,21,10,29,17])

arr2 = arr.reshape(4,2)
print(arr2)
newarr2 = np.insert(arr2,1,[5,6],axis=None)
print(newarr2)

# appending to array list

newarr = np.append(arr,[89])
print(newarr)

# concat the two list

arr2 = np.array([26,76,49])
new_arr = np.concatenate((arr2,arr))
print(new_arr)

# concat two 2d array

arr2d1 = np.array([[1,2],[3,4],[5,6]])
arr2d2 = np.array([[7,8],[9,10],[11,12]])
newarr2 = np.insert(arr2d1,1,[5,6],axis=0)
print(newarr2)
arr2d1[1,1] = 23
print(newarr2)

new2darr = np.concatenate((arr2d1,arr2d2),axis=0)
print(new2darr)

# deleting element from array

myarr = np.array([23,4,19,34,29,10])
print(myarr)
newarr = np.delete(myarr,0)
print(newarr)

# deleting 2d array

arr2d2 = np.array([[7,8],[9,10],[11,12]])
newmyarr = np.delete(arr2d2,1,axis=1)

print(newmyarr)
