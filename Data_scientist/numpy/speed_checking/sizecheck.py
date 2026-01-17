import numpy as np
import sys as s

arr = np.arange(10000000)

print("memory used by Numpy :",s.getsizeof(arr))

mylist = [i for i in range(10000000)]
print("memory used by List :",s.getsizeof(mylist))