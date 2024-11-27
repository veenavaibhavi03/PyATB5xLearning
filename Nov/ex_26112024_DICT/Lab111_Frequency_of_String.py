#find frequency of a letter in a string
string_input="Helloworld"
list_result=list(string_input)
print(list_result)
print(len(list_result))
a_dict={}
count=0
"""for i in list_result:
    count=list_result.count(i)
    print(i,count)"""

for i in string_input:
    a_dict[i]=a_dict.get(i,0)+1

print(a_dict)