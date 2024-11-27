# function that returns the maximum value from a dictionary
# {"a":10,"b":20,"c":30}

"""myDict={"a":10,"b":20,"c":30}
myKeys=myDict.values()
print(max(myKeys))"""


def max_value_dictionary(dict):
    return max(dict.values())

print(max_value_dictionary({"a":10,"b":20,"c":30}))


myDict={"a":10,"b":20,"c":30}
myKeys=myDict.values()
print(sorted(myKeys))
print(sorted(myKeys,reverse=True))