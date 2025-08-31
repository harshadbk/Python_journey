print(1+3)

print("Harshad","khatale")

print([1,2,3]+[4,5,6])

# Dunder function
# operation overloading

class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def shownumber(self):
        print(self.real,"i +",self.img,"j")

    def add(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

    def __add__(self,num2):
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)

num1 = Complex(12,3)
num1.shownumber()

num2 = Complex(6,9)
num2.shownumber()

num3 = num1.add(num2)
num3.shownumber()

num3 = num1 + num2
num3.shownumber()

# practice questions

class circle:
    def __init__(self,radius):
        self.radius=radius

    def Area(self):
        print("The area of circle",(22/7)*(self.radius*self.radius))

    def perimeter(self):
        print("The perimetre of circle is",(2*22)/7*self.radius)

c1 = circle(21)

c1.Area()
c1.perimeter()

