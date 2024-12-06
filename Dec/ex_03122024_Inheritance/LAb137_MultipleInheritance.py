# MultipleInheritance is supported in Python but not in java
class Father:
    def home(self):
        print("Father's Home")
    def father_money(self):
        return 5

class Mother:
    def home(self):
        print("Mothers's Home")
    def mother_money(self):
        return 6

class son(Mother,Father):  # here Mother function is called while overiding class son(Father,son)====>> in this case Father will be called
    def son_money(self):
        son_money=self.mother_money()+self.father_money()
        print(son_money)

s=son()
s.son_money()
print(s.mother_money())
print(s.father_money())
s.home()