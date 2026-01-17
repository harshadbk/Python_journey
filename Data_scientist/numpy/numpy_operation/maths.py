import numpy as np

arr = np.array([10,20,30])

print(arr)
print(arr + 10)
print(arr * 5)
print(arr ** 2)

# some maths property

arr2 = np.array([12,13,14,17,18,20,25])

print("Sum of Array ",np.sum(arr2))
print("Mean of Array ",np.mean(arr2))
print("Min value in Array ",np.min(arr2))
print("Max value in Array ",np.max(arr2))
print("Std deviation in Array ",np.std(arr2))
print("Variation in Array ",np.var(arr2))


# standard maths formula for calculating ml accuracy
# sigmoid
def sigmoid(arr):
    return 1/(1+np.exp(-(arr)))

arr = np.arange(100)
print(sigmoid(arr).round(2))

# mean squared error

actual = np.random.randint(1,50,25)
predicted = np.random.randint(1,50,25)

def mse(actual,predicted):
    return np.mean((actual-predicted)**2)

print(mse(actual,predicted))