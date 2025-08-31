import numpy as np

# creating array

a = np.array([1,2,3,4])

b = np.array([[5,6,7,8],[9,10,11,12]])

print(a)

print(b)

# speacial arrays 

zero = np.zeros((2,3))

one = np.ones((3,3))

eyes_mat = np.eye(2)

full_mat = np.full((2,2),7)

print(zero)
print(one)
print(eyes_mat)
print(full_mat)

# ranges

my_range = np.arange(2,20,2)
print(my_range)

line = np.linspace(0,1,5)
print(line)

print(line[2])

line = line.astype(np.int32)
mytuple = tuple(line)
print(mytuple)

# Indexing

arr = np.array([[1,2,3],[4,5,6]])

print(arr)
print(arr[:,1])
print(arr[1,:])
print(arr[::2])

# attributes

print(arr.shape)
print(arr.ndim)
print(arr.size)
print(arr.dtype)

# reshaping

arr = arr.reshape((3,2))
print(arr)
print(arr.flatten())

print(arr.T)

# type conversion

a = np.array([1, 2, 3], dtype=np.float64)
a.astype(np.int32) 
print(a)
print(a.dtype)

# NumPy vectorized operation
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
print(a + b)