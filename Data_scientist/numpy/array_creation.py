import numpy as np

one_d_array = np.array([[1,2,3],
                        [4,5,6],
                        [7,8,9],
                        ])

print(one_d_array)

# creating using 0s numpy array

zeroarray = np.zeros(3)
print(zeroarray)
zeroarray = np.zeros((2,3))  # this types of array mostly uses for future value predictions
print(zeroarray)

# creating using 1s numpy array

onesarray = np.ones(8)
print(onesarray)
onesarray = np.ones((3,6))
print(onesarray)

# for storing default topic

defarray = np.full((3,4),9)
print(defarray)

defarray[2,3] = 34
print(defarray)

# storing ranges in numpy

rangearr = np.arange(1,10,2)
print(rangearr)
print(len(rangearr))
print("Shape:",rangearr.shape)
print("Size:",rangearr.size)
print("Number of Dims:",rangearr.ndim)

# identity matrix 

ident_mat = np.eye(4)
print(ident_mat)