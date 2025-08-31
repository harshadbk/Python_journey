class Student:
    name = "Harshad"

s1 = Student()
print(s1.name)

# constructors in python

class Car:

    # default constructor
    def __init__(self):
        pass
        
    # parameterized constructors
    def __init__(self,name,price):
        self.name=name
        self.price=price
        print("Adding new car in storehouse")

c1 = Car("Thar",19)
print(f"name:{c1.name} and Price:{c1.price}")

c2 = Car("John deer",7)
print(f"{c2.name} and Price:{c2.price}")

