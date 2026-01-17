import numpy as np

# 1.Create a 1D NumPy array of integers from 10 to 50.
arr10to50 = np.arange(10,51)
print(arr10to50)

# 2.Create a 2D array of shape (3, 4) filled with zeros.
setzeros = np.zeros((2,3))
print(setzeros)

# 3.Create an array of 10 evenly spaced values between 0 and 1.
linespace_arr = np.linspace(0,1,10).round(2)
print(linespace_arr)

# 4.Convert a Python list of lists into a NumPy array and print its shape and dtype.

lofl = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

numparray = np.array(lofl)
print(numparray)
print(numparray.size)
print(numparray.shape)

# 5. Create an identity matrix of size 5×5.

idetm = np.eye(4)
print(idetm)

# 6. Reshape a 1D array of size 12 into a 3×4 matrix

myr = np.arange(12)
print(myr)
resarr = myr.reshape(3,4)
print(resarr)

# 7.Flatten a 2D NumPy array into a 1D array

flatten_arr = resarr.flatten()
print(flatten_arr)

# 8. Find number of elements, dimensions, and shape
print("\nQuestions No 8\n")
print(flatten_arr.size)
print(flatten_arr.ndim)
print(flatten_arr.shape)

# 9. Change a 2D array from shape (4, 3) to (2, 6)
print("\nQuestions No 9\n")
my2darr = np.arange(12).reshape(4,3)
print(my2darr)

changedir = my2darr.reshape(2,6)
print(changedir)

# 10. Add a new axis to convert a 1D array into a column vector
print("\nQuestions No 10\n")

arr_1d = np.array([1, 2, 3, 4])
print(arr_1d)
column_vector = arr_1d[:, np.newaxis]
print(column_vector)
