#mutable means we can change value using assignment operators
my_dict={
    "name":"aman",
    "age" :34,
    "role":"SDET",
    "experience":4
}
print(my_dict["age"])
my_dict["age"]=45
print(my_dict["age"])
print(my_dict)

del my_dict["role"]
print(my_dict)

for key,value in my_dict.items():
    print(key,"->",value)

print("age" in my_dict)