"""write a program to find sum of 3 numbers taking input from the user
if the user doesnot enter any number user 100,200,300 as default value
"""


def sum_of_three_numbers(num1=100,num2=200,num3=300):
    sum=num1+ num2+num3
    return sum

print(sum_of_three_numbers())
num1=int(input("Enter num1"))
num2=int(input("Enter num2"))
num3=int(input("Enter num3"))
sum_result=sum_of_three_numbers(num1,num2,num3)
print(sum_result)


