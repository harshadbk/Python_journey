import os

content = """we are learning File I/O
using Java.i like programming in java
"""

with open("practice.txt", "w") as file:
    file.write(content)

with open("practice.txt", "r") as file:
    data = file.read()

data_replaced = data.replace("Java", "Python").replace("java", "python")

with open("practice.txt", "w") as file:
    file.write(data_replaced)

if "learning" in data_replaced:
    print("The word 'learning' exists in the file.")
else:
    print("The word 'learning' does not exist in the file.")

print("\nUpdated content of practice.txt:")
print(data_replaced)

# problem 2

def find_learning_line(filename):
    try:
        file = open(filename, "r")
        for i, line in enumerate(file, start=1):
            if "learning" in line:
                return i
        return -1
    except FileNotFoundError:
        print("File not found.")
        return -1

line_number = find_learning_line("practice.txt")
print("The word 'learning' is found on line:", line_number)

# problem 3

def count_even_numbers(filename):
    try:
        with open(filename, "r") as file:
            content = file.read()
            numbers = content.split(",")
            even_count = 0
            for num in numbers:
                if num.strip().isdigit() and int(num.strip()) % 2 == 0:
                    even_count += 1
            return even_count
    except FileNotFoundError:
        print("File not found.")
        return -1

# Test the function
even_count = count_even_numbers("numbers.txt")
if even_count != -1:
    print("Count of even numbers:", even_count)
