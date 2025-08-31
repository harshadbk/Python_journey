# using for loop 

n = int(input("enter the number "))
fibs=[0,1]
if n<=1:
    print("fibonacci series is ",fibs[:n])

else:
    for i in range (2,n):
        next=fibs[i-1]+fibs[i-2]
        fibs.append(next)

print("the fibonacci sequence is ",fibs)

# using while loop

m = int(input("enter the number "))
fibs2=[0,1]
if m<=1:
    print("fibonacci series is ",fibs[:m])

else:
        i=2
        while i<m:
           next=fibs2[i-1]+fibs2[i-2]
           fibs2.append(next)
           i+=1

print("the fibonacci series is ",fibs2)