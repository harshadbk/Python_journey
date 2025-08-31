cricket = ("jofra","ben","morgan","buttler","plunket","roy","hardik")
temp=list(cricket)
temp.append("williamson") # we perform different operation on tuple just like list by the using temp variable
temp.pop(2)
temp[1]="shakib"
cricket=tuple(temp)
print(cricket)
# concatenation of two tuple
team_1=("rasi","decock","miller","faf","bauma")
team_2=("pat","josh","warner","marsh","stark")
team_3 = team_1+team_2
print(team_3)

tup=(98,69,84,67,45,99,89,85,68,48,87,54,63,84)
res=tup.count(84) # count the given number are reapreted in given tuple
print("the given value is reapeted in ",res)

print(tup.index(84)) # output is 5
k=len(tup)

# TUPLE METHODS

tuple=(84,57,82,98,36,48,64,64,87,73,78,47,56,45,87,87,46,46,58,73,25,46,338,568,76)
print(tuple)
print(len(tuple))
print(tuple.count(64)) # this method return value repeate in given tuple and how manyb times
print(tuple.index(338)) # this return index of this value
list=list(tuple) # in such way we convert any tuple to respective set,list.
print(list)
