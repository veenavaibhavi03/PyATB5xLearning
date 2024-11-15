#maximum of 3 numbers
#user input-num1,num2,num3->int
#o/p-> int or string with max number

num1=int(input("enter first number")) # 5
num2=int(input("enter second number")) #3
num3=int(input("enter three number"))  #2

#logic? if else-1 condition
if num1>num2 and num1>num3:
    print(f"{num1} is maximum number")
elif num2>num1 and num2>num3:
    print(f"{num2} is maximum number")
else:
    print(f"{num3} is maximum number")