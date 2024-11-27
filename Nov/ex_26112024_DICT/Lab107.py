from tkinter.font import names

student_info={
    "name":"radhika",
    "age" :9,
    "role":"student",
    "class":4
}

print(student_info["name"])
print(student_info["age"])
print(student_info["role"])
print(student_info["class"])
student_info["age"]=13
print(student_info)

for key,value in student_info.items():
    print(key,value)

student_info1=dict(name="vinay",age=9, role="student", grade=4 )
print(student_info1)

#dictionary with dictionary

student_info={
    "name":"radhika",
    "age" :9,
    "role":"student",
    "class":4,
    "address":{
        "home_address":"KA",
        "Office_address":"FA"
    }
}