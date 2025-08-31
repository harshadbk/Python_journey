# we find factorial by using recursion method
def factorial(n):
    ''' this function return us for printing factorial using recursion'''
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
print(factorial(5))
print(factorial.__doc__)

# FIBONACCI SEQUENCE IN PYTHON
def fibonacci(n):
    ''' this function return us for printing fibonacci sequence using recursion'''
    if(n==0 or n==1):
        return n
    else:
        return fibonacci(n-2)+fibonacci(n-1)

print(fibonacci(5))
print(fibonacci.__doc__)