# EXAMPLE 2
def argument(a=6,b=78):
    print("the averagge is ",(a+b)/2)
argument()
argument(6,8)
argument(89)
argument(b=34)
argument(b=98,a=65)




# EXAMPLE 1

def average(a,b,c=1):
    print("the average of numbers is ",(a+b+c)/3)

average(12,67)

# EXAMPLE 3

def average(*numbers):
    print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum+i
    print("the average of numbers ",sum/len(numbers))
def main():
 average(46,84,68,74,36,64,65,98.90)
if __name__ == "__main__":
    main()

    #EXAMPLE 4

def name(**name):
    print(type(name))
    print("hello,",name["fname"],name["mname"],name["lname"] )
name(mname = "dinesh",lname="kolage",fname="aakruti")

#EXAMPLE 4 RETURN THE VALUES FROM FUNCTION

def average(*numbers):
    sum = 0
    for i in numbers:
        sum=sum+i
    return sum/len(numbers)

def main():
 s=average(64,87,43,64,96,54,78,73,25,46)
 print("the average is ",s)
if __name__ == "__main__":
    main()