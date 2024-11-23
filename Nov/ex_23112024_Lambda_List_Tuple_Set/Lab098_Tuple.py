# we cannot append a tuple
cities=("London","Paris","Los Angeles","Tokyo")
print("London"in cities)
print("Bombay" in cities)

t=(9,8,4,8)
t_list=list(t)
t_list.append(6)
print(t_list)
t_tuple=tuple(t_list)
#t_tuple.sort()
print(t_tuple)