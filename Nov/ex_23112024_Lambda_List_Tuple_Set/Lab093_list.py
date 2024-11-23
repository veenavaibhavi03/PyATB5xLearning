#list-collection of items
# list allows duplicates
#multiple different data types are allowed
# it is stored with index 0-len-1
# syntax-[]
# list is mutable which means can be changed
# arrays cannot have same datatype

my_list=[1,2,3]
print(my_list)
my_list=["a",1,"c",89.9]
print(len(my_list))
print(my_list[0])
print(my_list[1])
print(my_list[2])
print(my_list[3])
my_list[3]=88.8
my_list[2]=1
print(my_list)

for i in my_list:
    print(i)

for i in range(1,7): # range itself is a list
    print(i,end=" ")