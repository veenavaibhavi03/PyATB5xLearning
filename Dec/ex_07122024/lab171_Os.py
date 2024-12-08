import os

try:
    full_path = os.getcwd()
    print(full_path)
    p = open("/Users/bvsvi/PycharmProjects/PyATB5xLearning/Dec/ex_07122024/lab171_Os.py")
except FileNotFoundError as e:
    print("File not found")
else:
    print("file opening")
finally:
    print("end of the program")

# file.close() # to close the file inputstream
