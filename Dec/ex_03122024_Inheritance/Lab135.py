class parent:
    gold="2kg"

    def bhk2(self):
        print("This is parent house")


class child(parent):
    diamond="diamond"

    def bhk3(self):
        print("this is child house")



Child=child()
print(Child.gold)
Child.bhk2()
print(Child.gold)

