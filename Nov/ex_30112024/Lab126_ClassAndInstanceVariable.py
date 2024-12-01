class Person:
    def __init__(self,name):
        self.Name_defined=name


    def walk(self):
        return self.Name_defined


person1=Person("vinay")
person2=Person("Laila")

print(person1.Name_defined)
print(person2.Name_defined)

print("person1:",person1.walk())
print("person2:",person2.walk())