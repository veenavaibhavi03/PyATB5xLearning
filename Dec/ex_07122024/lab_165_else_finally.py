try:
    a = int(input("Enter num1"))
    b = int(input("enter num2"))
    c = a / b

except ZeroDivisionError as e:
    print(e)

except ValueError as e:
    print(e)

else:
    print("output is :",c)