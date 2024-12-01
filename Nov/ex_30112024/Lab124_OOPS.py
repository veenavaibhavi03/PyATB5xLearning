a=10

class Person:
    b=11 #instance variable--belongs to class

    def print_info(self):
        c=20 #local variable can be accessed directly
        print(self.b) # instance variable should accessed using self
        print(c)
        """ a=20  # local variable has high preference than the global variable
               print(a)"""
        global a
        a=20
        print(a)





object_reference=Person()
object_reference.print_info()




