import os

try:
    full_path = os.getcwd()
    print(full_path)
    fullpath = os.getcwd() + "/example.txt"
    print(fullpath)
    file = open(fullpath)

except FileNotFoundError as e:
    print("File not found")
else:
    print("file opening")
finally:
    print("end of the program")