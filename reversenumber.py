#using for loop

def reverse(number):
    rev=0
    for digit in str(number)[::-1]:
        rev=rev*10+int(digit)

    return rev

number=12345
num=reverse(number)
print(num)


#using while loop

def reverse(number):
    rno=0
    while number>0:
        digit=number%10
        rno=rno*10+digit
        number=number//10
    return rno

number = 12345
no=reverse(number)
print(no)

    








     