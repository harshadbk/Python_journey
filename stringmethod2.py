# STRINGS ARE IMMUTABLE IN PYTHON MEANS THEY CAN NOT CHANGE
a = "!!!!harshad!!!!!!!! !!!!!shubham harshad"
print(len(a))
print(a)
print(a.upper())
print(a.lower())
print(a.rstrip("!")) # rstrip means ignoring the charecter only skip last elment not in first
print(a.replace("harshad","aakruti"))
print(a.split(" ")) # splite into many marts when hw find space abd convert into list
print(type(a.split(" ")))
blogheading = "introduction to python"
print(blogheading.capitalize()) # to capatalised any strings

str1 ="welcome to the console!!!"
print(str1.center(50,"."))
print(len(str1))
print(len(str1.center(50,".")))
print(a.count("h")) #its count how many time specific word or letter or any special charecter repeat in string
print(str1.endswith("!!!")) #check anycharecter ends with this or not
print(type(str1.endswith("!!!")))
print(str1.endswith("to",4,10))

str2 = "my name is rohit sharma i am from nagpur and i am very interested in cricket "
print(str2.find("is"))
str3 = "welcometothegpmumbai"
print(str3.isalnum())
print(str3.islower())
print(str3.isupper())

str4 = "this is hardik pandya captain of gt"
print(str4.isprintable())
print(type(str4.isprintable()))

str4 = "    "
print(str4.isspace())

str4 = "this is my country "
print(str4.istitle())

str4 = "this is my country THE NAME IS AUSTRALIA"
print(str4.swapcase())

