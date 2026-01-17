import numpy as np

# conversion form tuple to array

my_tuple = (1,2,3,4,5,6,7,8,9,10)

my_array = np.array(my_tuple)

print(my_array)

# Arithmetic Operations
# NumPy supports element-wise operations.

print(my_array + 1) # [ 2  3  4  5  6  7  8  9 10 11]
print(my_array * 2)
print(my_array) # do not changes actual array

print(my_array / 2)

# Mathematical Functions

print(np.sin(my_array))
print(np.sqrt(my_array))
print(np.exp(my_array))
print(np.log(my_array+1))

# Comparison & Boolean Operations

print(my_array > 1)
print(my_array == 3)
print(my_array[my_array>3])

# Aggregate Functions

print(my_array.sum())
print(my_array.mean())
print(my_array.min())
print(my_array.max())
print(my_array.std())

# Reshaping (if needed)

print(my_array.reshape((2,5)))

# Indexing & Slicing

print(my_array[0])        # First element
print(my_array[-1])       # Last element
print(my_array[1:4])      # Middle 3 elements

# Broadcasting Example

arr2 = np.array([10])
print(my_array + arr2)

# copy and view

copy_array = my_array.copy()
view_array = my_array.view()

copy_array[1] = 11
view_array[0] = 12

print("Actual Array",my_array)
print("copy array",copy_array)
print("View array",view_array)

# Vectorized Conditions (Where)

# np.where(condition, value_if_true, value_if_false)

print(my_array)
result = np.where((my_array > 3) & (my_array < 9) , "Better","Not better")
print(result)

# replacing negative no

my_array2 = np.array([1,2,-3,-4,7,-1,10])

filtered = np.where(my_array2 < 0 , 0 , my_array2)
print(filtered)

condt = my_array2 > 0

index_fetch = np.where(condt == False)[0]

print(index_fetch)



# dot product

s1 = np.arange(12).reshape(3,4)
s2 = np.arange(12,24).reshape(4,3)

print(s1)
print(s2)

dotproduct = np.dot(s1,s2)
print(dotproduct)