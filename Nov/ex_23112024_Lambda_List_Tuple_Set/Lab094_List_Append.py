my_list=["a",1,"c",89.9]
print(len(my_list))
print("elemnet a 0 index",my_list[0])
print("elemnet a 0 index",my_list[1])
print("elemnet a 0 index",my_list[2])

#append()=Append an object to the end of the list. It takes arguments
my_list.append(4)
#my_list.append(5)
print(my_list)

#extend-> Adds a new list . it takes list
my_list.extend([8])
print(my_list)

#insert()->it inserts a particular value in the respective index
my_list.insert(2,"vijay")
print(my_list)

my_list[4]="f"  # it actually replaces the value
print(my_list)

my_list.remove(4) # it removes a value
print(my_list)

my_duplicate_list=my_list
my_list.append(5)
print(my_list)
print(my_duplicate_list)

f_list=[10,5,6,1]
f_list.sort()
print(f_list)

