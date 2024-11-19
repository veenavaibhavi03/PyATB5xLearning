# function which does not return anything
def fika():
    print("I like cinamon bun")

fika()

# funtion with 1 argument and doesnot return anything

def fika(item):
    print(f"I like this {item} for fika")

fika("vanillabun")

# function with Default arugument or positional aruguments-- it will take default value if we dont pass any argument
def number(a=9):
    a=a+10
    print(a)
number()
number(8)

def number(name1="a",name2="b"):
    print(f"{name1}, {name2}")

number()
number("havisha")
number("this","that")
number("harayani","")
number(name2="jovana")

# function with argument and return type we can also give default arguments

def sum(num1=78, num2=89):
    return  num1+num2

result=sum(78,96)
print(result)
print(sum())
print(sum(80,90))