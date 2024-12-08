import os

filename="sample.txt"
content="This is a sample file. well done "

with open(filename,"w") as file:
    file.write(content)

with open(filename,"r") as file:
    content2=file.read()
    print(content2)

#os.remove("sample.txt")
