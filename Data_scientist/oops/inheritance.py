# simple inheritance

class A:
    var1 = "hello class A"

class B(A):
    var2 = "hello class B"

b1 = B()

print(b1.var1)
print(b1.var2)

# multiple

class A:
    var1 = "hello class A"

class B:
    var2 = "hello class B"

class C:
    var3 = "hello class C"

class D(A,B,C):
    var4 = "hello class D"

d1 = D()
print(d1.var1)
print(d1.var2)
print(d1.var3)
print(d1.var4)

# multilevel


class A:
    var1 = "hello class A"

class B(A):
    var2 = "hello class B"

class C(A):
    var3 = "hello class C"

b1 = B()
print(b1.var1)
c1 = C()
print(c1.var1)