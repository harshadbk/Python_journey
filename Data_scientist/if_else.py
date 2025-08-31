# x = int(input("Enter the number :"))
x = 12

if(x>5 and x <= 9):
    print("X is greater than 5")
elif(x>=10):
    print("X is greater than or equal to 10")
else:
    print("X is small than 5")

# match case

def match_num(x):
    match x:
         case int(n) if n<10 and n>=0:
            print("N is less than 10")
         case int(n) if n<20 and n>=10:
            print("N is less than 20 or greater than 10")
         case _:
            print("Nothing")

match_num(89)

# ternery operator

age = 19
result = "Adult" if age >= 18 else "Minor"
print(result)  # Output: Adult

# using pass in if else

age = 20

if age >= 18:
    pass  # Placeholder for future code
else:
    print("You are not eligible to vote.")

# switch case

day = 3

match day:
    case 1:
        print("Sunday")
    case 2:
        print("monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("saturday")
    case _:
        print("Invalid")

num1 = int(input("Enter the num1"))
num2 = int(input("Enter the num2"))

operation = input("Operation")

match operation:
      case '+':
           print(f"The addition of 2 number is {num1+num2}")
      case '-':
            print(f"the substraction of 2 number is {num1-num2}")
      case '*':
            print(f"the Multiplication of 2 number is {num1*num2}")
      case '/':
            print(f"the division of 2 number is {num1/num2}")
      case '//':
            print(f"the floor division of 2 number is {num1//num2}")   
      case '%':
            print(f"the reminder of 2 number is {num1/num2}") 
      case _:
            print("Invalid operation")



