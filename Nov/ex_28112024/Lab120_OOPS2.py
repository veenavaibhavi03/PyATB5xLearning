#constructor
class Dog:
    # name="chow"
    name = None
    breed = None
    height = None
    def __init__(self):
        print("I am called")

    def bark(self):
        print("Barking")

    def sleep(self):
        print("Sleep")


chow_ref = Dog()
print(chow_ref.name)

# mow=Dog()
# rancho=Dog()