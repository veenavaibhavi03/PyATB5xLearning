dict1={"a":1,"b":2}
dict2={"c":3,"d":8,"e":9}
merged_dict=dict1 | dict2
print(merged_dict)
print(merged_dict.get("b"))
print(merged_dict.values())
print(merged_dict.keys())
print(merged_dict.pop("a",1))