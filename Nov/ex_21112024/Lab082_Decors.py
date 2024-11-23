def decorator1(func):
    def wrapper1():
        print("starting decorator1")
        func()
    return wrapper1


def decorator2(func1):
    def wrapper2():
        print("ending  decorator2")
        func1()
    return wrapper2

@decorator1
@decorator2
def say_hello():
    print("Hello")

say_hello()
