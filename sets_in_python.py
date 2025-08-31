s1 = {1,2,3,4,5,6,7}
s2 = {4,5,12,43,56}

if 7 in s1:
    print("7 is present")
else:
    print("7 is not present")



print(s1.union(s2)) # to perform union operations on set
s1.update(s2) # for updating the value in s1 to add value in s2
print(s1,s2)  # for printing both the sets in without touching 
s3=s1.intersection(s2) # to performing intersection operation on sets
print(s3)
s2.update(s3)
print(s2)

s5= s2.symmetric_difference(s1)
print(s5)

s1.difference(s2)
print(s1)


ipl={"harshad","pant","rahul","rohit","bairstow"}
cricket={"root","hardik","buttler","russel","powell","rahul"}
desi=ipl.difference(cricket)
print(desi)

print(ipl.isdisjoint(cricket)) # check if 2 sets are not intersects 
print(ipl.issuperset(cricket)) # check if all values are present in main set
print(ipl.issubset(cricket)) # check for subset

srh={"markram","samad","bhuvneshwar","klassen"}
ipl.update(srh)
print(ipl)
ipl.add("shreyash")
print(ipl)

ipl.discard("pant")
print(ipl)

print(ipl)
popvalue=ipl.pop()
print(popvalue)
popvalue=ipl.pop()
print(popvalue)

del(ipl)
# print(ipl)

cricket.clear()
print(cricket)

