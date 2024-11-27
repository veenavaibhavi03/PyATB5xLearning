def add_numbers(*args):
    total =0.00
    for item in args:
        total = total + item
    return total

print(add_numbers())                   #Passing nothing
print(add_numbers(10))                 #Passing only one value
print(add_numbers(10,100,1000))  #Passing 3 item and adding all of them
nums = [1,2,3,4]
print(type(nums))
print(type(add_numbers(*nums)))