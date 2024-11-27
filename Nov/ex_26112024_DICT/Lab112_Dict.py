# to check which key is missing
from Nov.ex_26112024_DICT.Lab106 import my_dict

dict_1={"a":1,"b":2}
dict_2={"a":3,"b":8,"c":9}

missing_keys=set(dict_2.keys()) - set(dict_1.keys())
print(missing_keys)

