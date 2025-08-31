# using for loop

def palindrome(number):
    rno = 0
    for digit in str(number)[::-1]:
        rno = rno * 10 + int(digit)
    if(rno==number):
        print("this no is palindrone ")
    else:
        print("this no is not palindrome ")
palindrome(12321)


# using while loop

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



def is_palindrome(number):
    original_number = number
    reversed_number = 0

    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number = number // 10

    return original_number == reversed_number

# Example usage:
number = 12321  # Change this number to test different cases
if is_palindrome(number):
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")
