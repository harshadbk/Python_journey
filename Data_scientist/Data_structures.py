# lists
my_list = [12,14,9,18,19,19,19,26,False]
my_list.append(78)
print(my_list)
my_list.extend([12,67])
print(my_list)

my_list.insert(2,13)
print(my_list)
print(my_list.remove(14))
print(my_list)

print(my_list.sort())
print(my_list.reverse())
print(my_list)

item = my_list.pop(5)
print(item)
print(my_list)

index = my_list.index(26)
print(index)

count_19 = my_list.count(19)
print(count_19)

copy_list = my_list.copy()

print(copy_list)

# built in functions

# 1) len

print(len(my_list))
print(max(my_list))
print(min(my_list))
print(sum(my_list))
print(sorted(my_list,reverse=False,key=None))

my_arr = list(range(0,12))

print(my_arr)

print(any(my_list))
print(all(my_list))

print(list(enumerate(my_list,start=0)))

# map function

odd_num = list(map(lambda num: num % 2 != 0, my_list))
print(odd_num)

# filter function

odd_num = list(filter(lambda num:num % 2 != 0, my_list))
print(my_list)
print(odd_num)

# tuples

"""
tuples are immutable sequences used to store 
collections of items.Since tuples cannot be changed after creation, their functionality is limited 
compared to lists. Below are various functions and methods available for tuples.
"""
print("\n\nTuples Demo")
t1 = (1,2,2,2,5,6,7,9,3,11,12)
print(t1)

print(len(t1))

print(max(t1))

print(min(t1))

print(sum(t1))

lst = [1,2,3,4,5]

t = tuple(lst)

print(type(t))

print(t1.count(2)) # output 3

fi = t1.index(2)
print(fi) # output 1

second_index = t1.index(2,fi+1)
print(second_index)

# Get All Occurrences of an Element

element = 2
indices = [i for i, val in enumerate(t1) if val == element]
print(indices)

# works same 

indices = []
for i, val in enumerate(t1):
    if val == element:
        indices.append(i)  # Store the index if value matches

print(indices)  # Output: [1, 2, 3]

# concatenation

print(t+t1)

print(t*3)

# member ship

print(12 in t1)
print(4 not in t)

# slicing

print(t1[1:4])  
print(t1[:3])  
print(t1[-3:])  

#tuple packing and unpackig

t = 10, 20, 30  # Tuple Packing
print(t)  # Output: (10, 20, 30)

a, b, c = (10, 20, 30)
print(a, b, c)  # Output: 10 20 30

# Tuple with for Loop

t = (1, 2, 3, 4, 5)
for i in t:
    print(i, end=" ")  # Output: 1 2 3 4 5

for i in my_list:
    print(i , end=" ")

print("\n\n\nStrings functions")

str = "buttler"

