list_1=[12,87,1,2,3,65,23,23,23,90,21]
print(list_1)
list_1.append(98) # this method add any data at last of the string
print(list_1)
list_1.sort() # this method sort the list
print(list_1)
list_1.sort(reverse=True) # this method sort the list in decending order
print(list_1)
list_1.reverse()
print(list_1) # this method reverse the list
print(list_1.index(65)) # this will give the index of given value
# this return first ocurrence of the item
print(list_1.count(23)) # count the number in how many times they are repeate

print(list_1)
list_2 = list_1
list_2[0]=90
print(list_1)
# for those above reason we use copy function this dont change original list

list_3 = list_1.copy()
list_3[0]=78
print(list_1)
print(list_3)

list_1.insert(4,45) # insert the element in given position
print(list_1)

m=[876,908,234,986]
list_1.extend(m) # add m list at last to the list_1
print(list_1)
j=list_1+m
print(j)
list_1.remove(23) # remove the element in list
print(list_1)

op = int(input("enter the number")) # to remove any element from list we use this logic
kl=list_1[op]
list_1.remove(kl)
print(list_1)









