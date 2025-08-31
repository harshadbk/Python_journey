import pandas
list_1=[12,78,12,"dinesh",87.98,34,87,12,432,59,134]
print(list_1)
print(type(list_1))
print(list_1[0])
print(list_1[1])
print(list_1[2])
print(list_1[3])
print(list_1[4])
# print(list_1[5])
# print(list_1[6])     ERROR BECAUSE OF THE LIST AND INDEX OUT OF THE RANGE

# NEGATIVE MARKING
print(list_1[-1:])
print(list_1[-1:2])# PRINT NOTHING BECAUSE THERE IS NO SENSE IN ABOVE EXAMPLE FOR PRINTING
print(list_1[3])
print(list_1[-2])
print(list_1[len(list_1)-2])
print(list_1[5-2])

print("check weather given elements are present in list of not ")

if 78 in list_1:
    print("yes")
else:
    print("no")

if "dn" in "dinesh":
    print("yes") # same thing apply for strings in python
else:
    print("no")

# jump index in python

print(list_1)
print(list_1[0:len(list_1)])
print(list_1[0:len(list_1):3])

# comprehension python list

list_2=[i for i in range(11)]
print(list_2)
list_2=[i*i for i in range(11)]
print(list_2)
list_2=[i*i for i in range(11) if i%2==0]
print(list_2)


