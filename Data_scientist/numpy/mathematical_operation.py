import numpy as np

my_array = np.array([0.0, 0.25, 0.5, 0.75, 1.0])

# 1) Basic Arithmetic Operations

print(my_array + 2)     # Add 2 to each
print(my_array - 1)     # Subtract 1 from each
print(my_array * 4)     # Multiply each by 4
print(my_array / 0.5)   # Divide each by 0.5
print(my_array ** 2)    # Square each value

# 2) Aggregate Operations (Single Output)

print("Sum:", my_array.sum())
print("Mean:", my_array.mean())
print("Min:", my_array.min())
print("Max:", my_array.max())
print("Product:", my_array.prod())    # All elements multiplied
print("Standard Deviation:", my_array.std())
print("Variance:", my_array.var())

# 3. Trigonometric Functions

print("sin:", np.sin(my_array))
print("cos:", np.cos(my_array))
print("tan:", np.tan(my_array))

# 4. Exponential and Logarithmic Functions

print("exp:", np.exp(my_array))      # e^x
print("log:", np.log(my_array + 1))  # log(x + 1) to avoid log(0)

# 5. Rounding Operations

print(np.round(my_array))
print(np.floor(my_array))
print(np.ceil(my_array))

# 6. Absolute and Sign

arr = np.array([-1, 0, 1])
print("Absolute:", np.abs(arr))
print("Sign:", np.sign(arr))

#  7. Cumulative Operations

sec_array = np.array([1,2,3,4,5,6])

cumalative_sum = np.cumsum(sec_array)
cumalative_prod = np.cumprod(sec_array)

print(cumalative_sum)
print(cumalative_prod)

# 8. Modulus, Clip, Power

print(np.mod(sec_array,3))
print(np.clip(sec_array,0.1,0.3))
print(np.power(sec_array,3))