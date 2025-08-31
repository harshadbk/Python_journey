tup=(7)
print(tup)
print(type(tup)) # this gives type is int because we give cant give the commas after 7 '
tup=(7,)
print(tup)
print(type(tup))
tup=(69,68,69,85,64,98,66,56,45,64,86,94,59,46,"harshad","aakruti","pant","shreyas ayyer",True)
print(len(tup))
print(tup)
print(type(tup))

print(tup[0:9])

if 8 in tup:
    print("yes this number is present ")
else:
    print("no this number does not present ")

