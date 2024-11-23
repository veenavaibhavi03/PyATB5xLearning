import math

"""def give_me_power(num):
    return math.pow(num,2)

res_pow=give_me_power(2)
print(give_me_power(2))"""
#OR We can shrink this to lambda always return a function

op2=lambda :math.pow(int(input("enter n")),2)
print(op2())