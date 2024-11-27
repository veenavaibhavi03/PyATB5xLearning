MyDict={"a":10,"b":20,"c":30,"d":20,"e":40,"f":10}
result_dict={}
result_set=set()
for k,v in MyDict.items():
    if v not in result_set:
        result_dict[k]=v
        result_set.add(v)
print(result_set)


