# first function in this programm for finding the mean of any two numbers
def calculatemean(a,b):
  mean = (a*b)/(a+b)
  print(mean)

# second function in this program for finding out smaller or greter in this two number
def comparison(a,b):
    if(a>b):
        print("first number is greater ")
    else:
        print("second number is greater ")
# starting from the program

a = 9
b = 12
calculatemean(a,b)
comparison(a,b)
# gmean = (a*b)/(a+b)
# print(gmean)
c = 19
d = 12
calculatemean(c,d)
comparison(c,d)
# gmean2 = (c*d) / (c+d)
# print(gmean2)