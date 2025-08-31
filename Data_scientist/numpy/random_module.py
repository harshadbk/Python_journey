import numpy as np

val = np.random.rand()
val = np.round(val)
print(val)

rand_array = np.random.rand(3)
print(rand_array * 10)

array_2d = np.random.rand(3,2,2,3)
array_2d = array_2d*11
print(np.round(array_2d))

# np.random.randn()

print(np.random.randn())        
print(np.random.randn(3))
print(np.random.randn(2, 2)) 

# 3. np.random.randint()

# np.random.randint(low, high, size)

print(np.random.randint(3,10))
print(np.random.randint(1,3,11))
print(np.random.randint(1,10,(3,3)))

# 4. np.random.seed()

np.random.seed(42)

print(np.round(np.random.rand(3),1))