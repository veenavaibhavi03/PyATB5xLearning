#take an input and create a class in python
class person:
    def __init__(self):
        print("I am called ")
        self.name=input("Enter a name\n")
        self.id = int(input("Enter a id\n"))
        self.occupation = input("Enter a occupation\n")
        self.phone = input("Enter a phone\n")

    def information(self):
        print("name of the person :"+self.name)
        print(f"{self.name}  id:",self.id)
        print(f"{self.name} occupation :" + self.occupation)
        print(f"{self.name} phone number:" + self.phone)


P1=person()
P1.information()
