class Home:
    def __init__(self):
        self.__child="child"
        self.Mother="mother"
        self.Father="father"

    def mother(self):
        print("I can access private variable",self.__child)
        print("I can access public variable",self.Mother)
        self.__Child()

    def __Child(self):
        print("I can only be access by mother and father methods")

    def  father(self):
        print("I can access private variable",self.__child)

home1=Home()
home1.father()
home1.mother()