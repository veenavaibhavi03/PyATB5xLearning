def mul_arguments(*args):
    # we can give multiple arguments; *args=list
    print(args)
    """for i in args:
        print(i)"""

print(mul_arguments("Hi"))
print(mul_arguments("Hi","hello"))
print(mul_arguments("H","I",8,90))
