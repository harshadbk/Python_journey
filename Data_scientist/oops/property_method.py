class student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
   
    @property
    def percentage(self):
        return str(round(((self.phy+self.chem+self.math)/3),2)) + "%"

stu1 = student(98,97,99)

#gives reference of method
print(stu1.percentage)

stu1.phy=87
print(stu1.percentage)