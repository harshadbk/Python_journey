class person:
    def __init__(self,name):
        self.name=name
        
    def sayhello(self):
        print(f"Hello dear {self.name}")

p1 = person("Harshad")

p1.sayhello()

del p1

p1.sayhello()
