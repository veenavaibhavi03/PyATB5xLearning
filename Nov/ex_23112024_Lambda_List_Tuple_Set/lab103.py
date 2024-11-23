#sorting a lists of tuples
tuples=[(2,"banana"),(1,"apple"),(3,"car")]
sorted_tuples=sorted(tuples,key=lambda x:x[0])
print(sorted_tuples)