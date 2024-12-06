#methodOverriding
class Father:
    flat="2BHK"
    def car(self):
        print("father has suzki car")


class son(Father):
    son_flat="3BHK"
    def car(self):
        print("Son has SUV")


s=son()
s.car()
"""f=Father()
f.car()"""