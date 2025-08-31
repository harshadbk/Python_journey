import numpy as np

my_array = np.array([0.0, 0.25, 0.5, 0.75, 1.0])

arr = np.array([1,2,3,4,5,6])

reshaped = arr.reshape((2,3))

print(reshaped)

reshaped2 = arr.reshape((-1,3))

print(reshaped2)

print(reshaped.ndim)

# sliceing

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

new_arr = arr.reshape((5,2))

print(new_arr)

print(arr[1:3])   # [20 30]
print(arr[:2])    # [10 20]
print(arr[::3])   # [10 30]

#  2D Slicing

arr2d = np.array([[1, 2, 7], [3, 4, 8], [5, 6, 9]])
print(arr2d)
print(arr2d.ndim)
print(arr2d[1])      
print(arr2d[1, 0])
print(arr2d[:, 1]) 

# flatten array

print(arr2d.flatten())
print(arr2d.ravel())

print(arr2d)

arr2d[0,1] = 10

print(arr2d)

#  4. Concatenation / Joining Arrays

a = np.array([1, 2])
b = np.array([3, 4])
joined = np.concatenate((a, b))
print(joined)  # [1 2 3 4]

# 2D Arrays:

a = np.array([[1, 2]])
b = np.array([[3, 4]])
v = np.vstack((a, b))     
h = np.hstack((a, b))
print(v)
print(h)

# 5. Splitting Arrays

splitted_array = np.split(arr,5)

print(splitted_array) # [array([10, 20]), array([30, 40]), array([50, 60]), array([70, 80]), array([ 90, 100])]

print(splitted_array[0]) # [10 20]

uneven_split = np.array_split(arr,3)
print(uneven_split)
print(uneven_split[0])

# 6. Tiling and Repeating

arr = np.array([1, 2])
print(np.tile(arr, 3))    # [1 2 1 2 1 2]
print(np.repeat(arr, 3))  # [1 1 1 2 2 2]

# 7. Transposing (for 2D+)

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.T)

# 8. Deleting Elements

arr = np.array([1, 2, 3, 4])
print(np.delete(arr, 1))

arr2d = np.array([[1, 2], [3, 4]])
print(np.delete(arr2d, 0, axis=0))
print(np.delete(arr2d, 1, axis=1))

#  9. Inserting Elements

arr = np.array([1, 2, 3])
print(np.insert(arr, 1, 99))

# 10. 3D Array

array_3d = np.array([
    [[1, 2, 3],
     [4, 5, 6]],
    
    [[7, 8, 9],
     [10, 11, 12]]
])

print(array_3d)

print(np.ndim(array_3d))

# 11. 4D Array

array_4d = np.array([
    [
       [[1,2],[2,3]],
       [[4,5],[6,7]]
    ],
    [
       [[8,9],[10,11]],
       [[12,13],[14,15]]
    ]
])

print(array_4d)
print(array_4d.shape)

print(array_4d[0,1,1,1])

# 12. 5d 

array_5d = np.arange(1,33)

arr_5d = array_5d.reshape((2,2,2,2,2))

print(arr_5d)
print(np.ndim(arr_5d))

print(arr_5d[1,0,1,1,0])