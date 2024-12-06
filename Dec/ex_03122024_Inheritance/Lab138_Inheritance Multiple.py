class A:
    def method(self):
        print("A method")

class B:
    def method(self):
        print("B method")


class c(B,A):
    pass

C=c()
C.method()


