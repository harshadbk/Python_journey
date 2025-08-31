# using for loop

n = int(input("enter the number "))
fact = 1

for i in range(1,n+1):
    fact*=i

print("factorial is ",fact)

# using while loop

m = int(input("enter the number "))
i = 1
fact = 1
while i<=m:
     fact*=i
     i+=1
print("the factorial is ",fact)