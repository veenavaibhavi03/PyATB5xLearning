#single inheritance
class Father:
    flat="2BHK"
    def car(self):
        print("This is fathers car")


class son(Father):
    son_flat="3BHK"
    def suv(self):
        print("This is sons SUV")


Son=son()
Son.suv()
Son.car()

father=Father()
father.car()