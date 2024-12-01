class PersonInformation:
    def __init__(self,name):
        self.__healthInformation="healthInfo"
        self.person_name=name

    def personification(self):
        print(f"{self.__healthInformation} should be private")
        print("name:",self.person_name)
        self.__healthinfo()

    def __healthinfo(self):
        print("This is a private function")

person1=PersonInformation("vinay")
person1.personification()