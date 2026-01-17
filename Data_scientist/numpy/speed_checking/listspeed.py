import numpy as np

a = [i for i in range(10000000)]
b = [i for i in range(10000000,20000000)]

c = []

import time
itime = time.time()

for i in range(len(a)):
    c.append(a[i] + b[i])

print("Time required for computing in list:", round(time.time() - itime, 2))


a = np.arange(10000000)
b = np.arange(10000000, 20000000)

itime = time.time()
c = a + b

print("Time required for computing in NumPy:", round(time.time() - itime, 2))