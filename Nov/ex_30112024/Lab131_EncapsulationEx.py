# Encapsulation
#Hide the data members(class variables,methods, instance variables)
#by using only methods

class Car:
    def __init__(self):
        self.password="vinay" # this is a public instance variable
        self.__password_secured="vinay123" # this is now a private instance variable


    def __change_password(self): # private function
        print(self.password)
        print(self.__password_secured)

    def change_password(self):
        print(self.__password_secured)
        print(self.password)

car1=Car()
car1.change_password() # only public variable can be accessed



