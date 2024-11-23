

#local variables will have more preference than global variables when there is a same identifier
Public_Transport="bus"

def home_new():
    private_vehicle="bike"
    print(private_vehicle)
    Public_Transport="car"
    print(Public_Transport)

home_new()