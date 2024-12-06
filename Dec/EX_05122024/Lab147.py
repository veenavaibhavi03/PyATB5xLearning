# It is supported if some of the aruguments are optional
class ArithmeticOperations:
    def add(self, a, b):
        print(a + b)

    def add(self, a, b, c):
        print(a + b + c)

    def add(self, a, b, c=1, d=1):
        print(a + b + c + d)


ae = ArithmeticOperations()
ae.add(1, 2, )