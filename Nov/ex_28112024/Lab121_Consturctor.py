#parameterized constructor
class Dog:
    # name="chow"
    name = None
    breed = None
    height = None
    # helps to set the values
    def __init__(self, name,breed,height):
        print("Constructor is called")
        self.name=name
        self.breed=breed
        self.height=height


    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep  -->"+ self.name)

# mow=Dog()
# rancho=Dog()
chow_ref = Dog("Pinku","mastiff",12)
chow_ref.sleep()
print(chow_ref.name)
print(id(chow_ref))

how_ref = Dog("Starry","Doberman",14)
how_ref.sleep()
print(how_ref.name)
print(id(how_ref))

Dog



