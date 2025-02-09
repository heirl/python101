# In Python 2, the map() function returns a list. In Python 3, however, the function returns a map object which is a generator object. To get the result as a list, the built-in list() function can be called on the map object. i.e. list(map(func, *iterables))
# The number of arguments to func must be the number of iterables listed.

my_things = ['laptop','bag','waterbottle','headphone']
apatilaze_collection = list(map(str.upper, my_things))

print(apatilaze_collection)

circle_areas = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.00013]

result = list(map(round, circle_areas, range(1, 3)))

print(result)

#using a map function to return a tuple from 2 lists
my_list1=[1,2,3,4,5]
my_list2=['a','b','c','d','e']
my_tuple=list(map(lambda x, y:(x,y),my_list1,my_list2 ))
print(my_tuple)