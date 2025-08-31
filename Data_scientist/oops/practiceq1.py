class Result:
    
    def __init__(self,name,m1,m2,m3):
        self.name=name
        self.m1=m1
        self.m2=m2
        self.m3=m3

    def average(self):
        avg = (self.m1+self.m2+self.m3) / 3
        return avg

r1 = Result("harshad",45,67,98)

print(r1.average())

r2 = Result("rohit",70,70,70)

print(r2.average())

r1.name = "pant"

print(r1.name)

print(r1.average())

