import numpy as np
temp = [12,67.34,18,23,34,39,29]

total = 0

for t in temp:
    total += t

avg = round(total/len(temp),2)

print(avg)

# using numpy

temp = np.array([12,67.34,18,23,34,39,29])

avg = round(np.mean(temp),2)
print(avg)