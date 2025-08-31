class Student:

    @staticmethod
    def sayhello():
        print("Hellow student")

    # class attribute
    college_name = "COEP technological university"

    # constructor
    def __init__(self,name,age):
        print("New students added into database...")
        self.name=name #object attributes
        self.age=age

    #method
    def welcome(self):
        print(f"Welcome student {self.name}")
    def get_marks(self):
        return self.age

s1 = Student("Harshad",17)

s1.welcome()
print(s1.get_marks())

s1.sayhello()

