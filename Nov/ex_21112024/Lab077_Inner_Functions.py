def outer_function():
    var1 = 30 # this will act as a global to inner functions
    def inner_function1():
        var3=50
        def inner_function():
            print(var3)
        print(var1)
        inner_function()
    def inner_function2():
        print(var1)

    inner_function1()
    inner_function2()

outer_function()