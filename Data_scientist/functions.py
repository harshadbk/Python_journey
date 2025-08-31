# 1. What is a Function?
# A function in Python is a block of reusable code that performs a specific task. It helps in code reusability, modularity, and maintainability.

def greet():
    print("Hello, Welcome to Python!")

greet() 

def add_numbers(a, b):
    return a + b

result = add_numbers(5, 10)
print(result)  # Output: 15

# Function Parameters and Arguments

def greet(name):
    print(f"Hello, {name}!")

greet("Alice")  # Output: Hello, Alice!

# default argument 

def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()         # Output: Hello, Guest!
greet("John")   # Output: Hello, John!

# keyword arguments

def student_details(name, age):
    print(f"Name: {name}, Age: {age}")

student_details(age=20, name="Alex")  # Output: Name: Alex, Age: 20

# Variable-Length Arguments (*args and **kwargs)

def add(*numbers):
    return sum(numbers)

print(add(1, 2, 3, 4))  # Output: 10

# *args allows passing any number of arguments.

def display_info(**details):
    for key, value in details.items():
        print(f"{key}: {value}")

display_info(name="John", age=25, country="USA")
# Output:
# name: John
# age: 25
# country: USA

# retun statements

def multiply(a, b):
    return a * b

result = multiply(5, 4)
print(result)  # Output: 20

# recursive functions 

def factorial(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    return n * factorial(n - 1)

print(factorial(0))  # Output: 120

#7. Lambda (Anonymous) Functions

square = lambda x: x * x
print(square(5))  # Output: 25

# function scope 

# Local Variables → Defined inside a function, accessible only within it.

# Global Variables → Defined outside all functions, accessible everywhere.

# Nonlocal Variables → Used inside nested functions.

#  pass in functions

def future_function():
    pass  # Placeholder

print("This function does nothing yet.")

# nested functions

def outer_function():
    def inner_function():
        print("Hello from Inner Function!")
    inner_function()

outer_function()


# Functions as First-Class Citizens in Python
# In Python, functions are first-class citizens, meaning:

# They can be assigned to variables.

# They can be passed as arguments to other functions.

# They can be returned from other functions.

# This allows higher-order functions, functional programming, and decorators.

def greet(name):
    return f"Hello, {name}!"

say_hello = greet  # Assigning function to a variable
print(say_hello("Alice"))  # Output: Hello, Alice!
