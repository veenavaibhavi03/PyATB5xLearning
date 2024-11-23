#write a program to calculate even and odd

"""def find_even_odd(num):
    if num%2==0:
        print("Even")
    else:
        print("odd")


find_even_odd(5)"""
num=int(input("Enter a number "))
check_even_odd=lambda num:"Even" if num%2==0 else "odd"
print(check_even_odd(num))