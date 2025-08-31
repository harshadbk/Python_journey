class person:
    # Private class attribute
    __name = "harshad"

    def __init__(self, age):
        self.age = age
        
   # private function
    def __showage(self):
        print(f"The age of {person.__name} is {self.age}")

    def info(self):
        self.__showage()

p1 = person(23)
# p1.showage()

p1.info()



