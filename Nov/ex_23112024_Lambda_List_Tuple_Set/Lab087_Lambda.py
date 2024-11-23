#lambda
"""
instead of a function i can use a lamdba function
def power_a_num(num):
    return num**3

result_num=power_a_num(2)
print(result_num)"""

result_num=lambda num,n:num**n  # multiple aruguments but can be only 1 expression 
print(result_num(2,3))