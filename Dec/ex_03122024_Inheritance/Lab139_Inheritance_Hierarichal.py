#Hirearical Inheritance-1 Parent, Multiple child

class Father:
    def flat_father(self):
        print("This is fathers house")

class child1(Father):
    def flat_child1(self):
        print("This is child-1 house")

class child2(Father):
    def flat_child2(self):
        print("This is child-2 house")

class child3(Father):
    def flat_child3(self):
        print("This is child-3 house")

c1=child1()
c1.flat_child1()
c1.flat_father()

c2=child2()
c2.flat_father()
c2.flat_child2()
#c2.flat_child1()

c3=child3()
c3.flat_child3()
c3.flat_father()