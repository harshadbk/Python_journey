import numpy as np

str_arr = np.array(["100","200","300","400","500","600"])

print(str_arr.dtype)
int_type = str_arr.astype(int)
print(int_type.dtype)

int_type[0] = 900
print(int_type)
str_arr = int_type.astype(str)
print(str_arr.dtype)
print(str_arr)
