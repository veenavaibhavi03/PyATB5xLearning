#from Dec.ex_03122024_Inheritance.Lab134_singleInheritance import father


class GrandFather:
    diamonds="Diamonds"
    def house_Grandfather(self):
        print("Grandfathers house")

class Father(GrandFather):
    gold="Gold"
    def House_father(self):
        print("This is fathers house")


class Son(Father):
    silver="silver"
    def House_Son(self):
        print("This is sons house")



son=Son()
son.house_Grandfather()
son.House_father()
son.House_Son()

fater=Father()
fater.house_Grandfather()
fater.House_father()
#fater.House_Son()

GF=GrandFather()
GF.house_Grandfather()
