
def palindrome(number):
    original_number=number
    rno = 0
    while  number>0:
        digit = number % 10
        rno = rno * 10 + digit
        number=number//10
    if(rno==original_number):
        print("no is palindrome ")
    else:
        print("no is not palindrome ")

palindrome(12321)

