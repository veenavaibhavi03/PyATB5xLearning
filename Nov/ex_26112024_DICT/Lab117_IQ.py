# input_string="HelloWorold"
#a,e,i,o,u
#vowel=
count=0
input_str="Hello,world"
list_vowels="aeiou"
for i in input_str:
    if i in list_vowels:
        count=count+1
    else:
        pass

print(count)