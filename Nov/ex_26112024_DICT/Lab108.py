student_info1={
    "name":"radhika",
    "age" :9,
    "role":"student",
    "class":4,
    "address":{
        "home_address":"KA",
        "Office_address":"FA"
    }
}

student_info2={
    "name":"aman",
    "age" :10,
    "role":"student",
    "class":5,
    "address":{
        "home_address":"AM",
        "Office_address":"MA"
    }
}

student_info3={
    "name":"JOvana",
    "age" :11,
    "role":"student",
    "class":7,
    "address":{
        "home_address":"KOLKata",
        "Office_address":"Banglore"
    }
}

student_list=[student_info2,student_info1,student_info3]
print(student_list[1])
print(student_list[0])
#student_list[1].age=11
print(student_list[0]["name"])
print(student_list[0]["age"])
print(student_list[0]["role"])
print(student_list[0]["address"]["home_address"])
student_list[0]["address"]["home_address"]="IND"
print(student_list[0]["address"]["home_address"])
print(student_list[2]["address"]["Office_address"])
#OR
print(student_info3["address"]["Office_address"])