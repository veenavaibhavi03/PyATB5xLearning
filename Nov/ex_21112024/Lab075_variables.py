public_transport="bus"
print(public_transport)
def owner():
    private_vehicle="car"
    print(private_vehicle)
    print(public_transport)

def strange():
    print(public_transport)
    #print(private_vehicle) it cannot be accessed as it is local

owner()
strange()
