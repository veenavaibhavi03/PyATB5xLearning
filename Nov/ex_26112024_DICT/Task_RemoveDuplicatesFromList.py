"""my_list = [1, 2, 2, 3, 4, 4, 5]
Remove duplicates from a list using a set.
Output: [1, 2, 3, 4, 5]"""

def remove_duplicates(my_list):
    my_set=set(my_list)
    return my_set

resultSet=remove_duplicates([1, 2, 2, 3, 4, 4, 5])
print(resultSet)