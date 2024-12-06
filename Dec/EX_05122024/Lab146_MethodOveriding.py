

class parent:

    def home(self):
        print("2BHK")


class son(parent):
    son_flat="3BHK"
    def home(self):
        print("3BHK")


s=son()
s.home()
"""f=Father()
f.car()"""