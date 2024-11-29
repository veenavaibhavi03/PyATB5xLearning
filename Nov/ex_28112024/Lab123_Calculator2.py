class Calculator:

    def __init__(self,a,b):
        print("I am called")
        self.a=a
        self.b=b
        """self.add(a, b)
        self.sub(a, b)
        self.mul(a, b)
        self.div(a, b)
"""
    def add(self, a, b):
        print(self.a + self.b)

    def sub(self, a, b):
        print(self.a - self.b)

    def mul(self, a, b):
        print(self.a * self.b)

    def div(self, a, b):
        print(self.a /self.b)


a = int(input("enter value a "))
b = int(input("enter value b "))
calculator = Calculator(a,b)
calculator.add(a, b)
calculator.sub(a, b)
calculator.mul(a, b)
calculator.div(a, b)


