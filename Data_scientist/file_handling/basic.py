import os

file1 = open("sample.txt", "w")
file1.write("my name is harshad")
file1.close()

file1 = open("sample.txt", "r")
print(file1.read())
file1.close()

file1 = open("sample.txt", "a")
file1.write(" i am from COEP pune")
file1.close()

file1 = open("sample.txt", "r")
print(file1.read())
file1.close()

os.remove("sample.txt")
print("File removed successfully.")

if os.path.exists("sample.txt"):
    os.remove("sample.txt")
    print("File removed successfully.")
else:
    print("File does not exist.")
