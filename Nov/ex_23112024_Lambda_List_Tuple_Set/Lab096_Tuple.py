# Tuple is a collection of item
# it cannot be changed which means immutables
# duplicates are not removed
#syntax-()

my_tuple=(1,2,3,4)
print(my_tuple)
#my_tuple[3]=8  'tuple' object does not support item assignment

shopping_list=["bread","milk","cheese"]
shopping_list[2]="sugar"
print(shopping_list)


my_tuple=("tta.com","sdet.live")
#my_tuple[0]="www.google.com"
my_api_list=list(my_tuple)
print(my_api_list)

#REAL Case,
API_URLs=("https://sdet.live/python0x","https://awesomeqa.com")
print(API_URLs[1])
print(API_URLs[0])