
# comments and multiline string

text = '''This is a 
multi-line string 
in Python.'''
print(text)

my_data = '''
hello my dear how are you 
and may i please ask you
'''

print(my_data)
"""
this is an operation 
"""

'''
This is a multiline comment.
Python will ignore it because it is not assigned to a variable.
It is useful for documentation or temporarily disabling code.
'''
print("Hello, World!")

# operators

# aritmetic operators

a = 10
b = 3
print(a + b)   # 13
print(a - b)   # 7
print(a * b)   # 30
print(a / b)   # 3.3333
print(a // b)  # 3
print(a % b)   # 1
print(a ** b)  # 1000

# comparison operator

x = 5
y = 10
print(x == y)  # False
print(x != y)  # True
print(x > y)   # False
print(x < y)   # True
print(x >= 5)  # True
print(x <= 3)  # False

#identity operators

x = [1, 2, 3]
y = x
z = [1, 2, 3]

print(x is y)  # True (same object)
print(x is z)  # False (different objects with same values)
print(x is not z)  # True


# membersip operators

lst = [1, 2, 3, 4, 5]
print(3 in lst)  # True
print(10 not in lst)  # True


# ternary operator

age = 20

mess = "Adult" if age>18 else "kid"

print(mess)


# data types

# 1) numeric

x = 10
y = -5
print(type(x))  # Output: <class 'int'>

# functions
print(abs(-10))
print(pow(2,3))
print(int("100"))

# 2) float

pi = 3.14
print(type(pi))

print(round(3.14159, 2))  # Round to 2 decimal places: 3.14
print(float("10.5"))  # Convert string to float: 10.5


# 3) string 

s = "Hello, Python!"
print(type(s))  # Output: <class 'str'>

print(len(s))  # String length
print(s.upper())  # Convert to uppercase
print(s.lower())  # Convert to lowercase
print(s.replace("Hello", "Hi"))  # Replace text
print(s.split(","))  # Split string into list

# 4) List

my_list = [1, 2, 3, "apple", 4.5]
print(type(my_list))  # Output: <class 'list'>

my_list.append(6)  # Add item
my_list.remove(2)  # Remove item
print(my_list)
print(my_list.pop())  # Remove and return last item
print(my_list.index("apple"))  # Find index of item
print(sorted([5, 1, 3, 2]))  # Sort list

l2 = [23,5,4,12,76]

print(sorted(l2))

# 5) tuples

my_tuple = (1, 2,2, 3, "banana")
print(type(my_tuple))  # Output: <class 'tuple'>

print(my_tuple[2])

print(my_tuple.count(2))  # Count occurrences of 2
print(my_tuple.index("banana"))  # Find index of "banana"

# 6) sets

my_set = {1, 2, 3, 3, 4}
print(type(my_set))  # Output: <class 'set'>
print(my_set)  # Output: {1, 2, 3, 4} (duplicates removed)

my_set.add(5)  # Add item
my_set.remove(2)  # Remove item
print(my_set.union({6, 7}))  # Combine sets
print(my_set.intersection({3, 4 ,7}))  # Common elements

# 7) dictionary

my_dict = {"name": "Alice", "age": 25 , 12:34}
print(type(my_dict))  # Output: <class 'dict'>

print(my_dict)
print(my_dict.keys())  # Get all keys
print(my_dict.values())  # Get all values
print(my_dict.get("name"))  # Get value by key
my_dict.update({"city": "New York"})  # Add new key-value


# booleaen type

x = True
y = False
print(type(x))  # Output: <class 'bool'>

print(bool(0))  # Output: False
print(bool(10))  # Output: True
print(bool(""))  # Output: False (empty string)


# binary types 

b = b"Hello"  # Bytes
ba = bytearray(5)  # Bytearray
mv = memoryview(b)  # Memoryview

print(bytes("hello", "utf-8"))  # Convert string to bytes
print(ba[0])  # Access bytearray element
print(mv[0])  # Access memoryview element

print(id(x))