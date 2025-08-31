class car:
    def __init__(self,type):
        self.type=type

    @staticmethod
    def start():
        print("Car started ....")

    @staticmethod
    def stop():
        print("Car stopped ....")

class Toyotacar(car):
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)
        super().start()

car1 = Toyotacar("Fortuner","electric")

print(car1.name)
print(car1.type)