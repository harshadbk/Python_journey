# for i in range(12):
#     if(i==10):
#         break
#     print("5 X",i+1," = ",5*(i+1))
#
# print("we are exit from the loop ")

for i in range (12):
    if(i==10):
        print("continue the iteration and skipp this iteration ")
        continue
    print("5 X ",i,"=",5*i)

i =0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

print("this is ending of our do while loop ")