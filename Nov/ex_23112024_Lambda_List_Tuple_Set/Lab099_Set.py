# SET
# collection of unique items
# duplicates are removed
# no order maintained
from Nov.ex_21112024.Lab082_Decors import decorator2

set_of_items={1,2,3,4,5,5,6,6,7,7,8,"a","a"}
print(set_of_items)


# list can be converted to set
list1=[23.5,"b",78]
set1=set(list1)
print(set1)

tuple_t=("TheTestingAcademy","for","if","if","for")
print(tuple_t)
print(set(tuple_t))