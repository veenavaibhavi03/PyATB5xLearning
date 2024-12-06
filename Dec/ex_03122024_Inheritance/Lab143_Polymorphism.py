# Conventional method overloading is not supported

class ArithmeticOperations:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

    def add(self, a, b, c, d):
        print(a + b + c + d)


ae = ArithmeticOperations()
ae.add(1, 2, )
"""ae.add(1,2,3)
ae.add(1,2,3,4)
"""
