class person:
    name = "anonymous"

    # def changeName(self,name):
    #     self.__class__.name=name

    @classmethod
    def changeName(cls,name):
        cls.name=name

p1 = person()
print(p1.name)
p1.changeName("rahul kumar")
print(p1.name)
print(person.name)