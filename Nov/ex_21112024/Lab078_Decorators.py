def add_security(function):
    def wrapper():                             # decorators
        print("1.before the function is called")
        print("2. Add helmet , dashcash,gloves,knee guards,license")
        function()
        print("3.After function call")
        print("4.secure driving and park")
    return wrapper()

@add_security
def drive_Ola_scooter():
    print("OLA")

@add_security
def drive_Scooty():
    print("Normal function!!")
    print("I am driving a scooty")