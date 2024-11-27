# dictionary to list
from Nov.ex_09112024_Literals_Variables.Lab023_Strings import value

keys=["name","role","experience"]
values=["Aman","Tester",5]

information=dict(zip(keys,values))
print(information)

keys=["name","role","experience"]
values=["Aman","Tester"]

information=dict(zip(keys,values))
print(information)
