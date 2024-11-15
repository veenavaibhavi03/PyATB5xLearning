# Program to find the max between two numbers

num1=float(input("Enter first number:"))
num2=float(input("Enter second number:"))
#print(f"{num1} is maximum number" if num1>num2 else f"{num2} is maximum number")
if num1>=num2:
    print(f"{num1} is maximum number")
else:
    print(f"{num2} is maximum number")

