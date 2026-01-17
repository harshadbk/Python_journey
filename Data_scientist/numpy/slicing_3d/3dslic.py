import numpy as np

my3dar = np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(my3dar,"\n")

new3d = np.arange(18).reshape(3,2,3)
print(new3d,"\n")

# print(new3d[1],"\n")
# print(new3d[::2])

# print(new3d[0,1,::])

# print(new3d[0::2])

# print(new3d[0::2 , 1])

print(new3d[::2,0,::2])