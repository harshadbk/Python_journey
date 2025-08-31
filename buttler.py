num = int(input("enter teh n numebrs "))

numbers=[]

for i in range (num):
   i = int (input("enter the number "))
   numbers.append(i)

print(numbers)

for i in range(2,len(numbers)):
   print(numbers[i])

numbers[2]=23
print(numbers)
