import numpy as np

my_array = np.array([10,20,30,40,50,60])

mask = ((my_array > 10) & (my_array < 50))

print(mask)

print(my_array[mask])

# Fancy Indexing (Indexing with lists or arrays)

indices = [2,3,4]
print(my_array[indices])

# on multidimentional array

matrix = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(matrix)
print(matrix[1,2])
print(matrix[[0,2],[1,2]]) #[2 9]

# Other Useful Boolean/Conditional Tools

print(np.any(my_array > 39)) # np.any(condition) → Returns True if any element is True.
print(np.all(my_array < 20)) # np.all(condition) → Returns True if all elements are True.

arr = np.array([10, 20, 30, 40, 50])
condition = arr > 25
false_positions = np.where(condition == False)[0]
print("Positions where condition is False:", false_positions)
