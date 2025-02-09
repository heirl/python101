#We need to import educe from functools
from functools import reduce
name = ["N"," ","S"," ","N"," ","V", " ","A"]
def add_name(first, second):
    return first+second
result= reduce(add_name,name)
print(result)


#The reduce function is used to perform an operation on all items of the iterable to give a result