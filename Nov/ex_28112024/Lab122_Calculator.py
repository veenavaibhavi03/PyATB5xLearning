class Calculator:

    def __init__(self):
        print("I am called")

    def add(self,a,b):
        print( a+b)

    def sub(self,a,b):
        print( a -b)

    def mul(self,a,b):
        print( a * b)

    def div(self,a,b):
        print(a/b)

        
calculator=Calculator()
a=int(input("enter value a "))
b=int(input("enter value b "))
calculator.add(a,b)
calculator.sub(a,b)
calculator.mul(a,b)
calculator.div(a,b)


