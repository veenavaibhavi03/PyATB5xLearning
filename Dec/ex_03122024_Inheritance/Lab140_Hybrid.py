class A:
    def method(self):
        print("A method")

class B(A):
    def method1(self):
        print("B method")


class C(A):
    def method2(self):
        print("c method")


class D(B,C):
    def method3(self):
        print("D method")

d=D()
#d.method1()
d.method()
d.method3()
d.method1()
d.method2()