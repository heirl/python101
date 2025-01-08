# A list in python have a ordered values and it may contain duplicates and its mutable
mylist = [1, 2, 3, 4, 5]
print(
    f"I'm of type {type(mylist)} and will be printed as a collection of elements {mylist}"
)

# A tuple in python have a ordered values and it may contain duplicates but its immutable
mytuple = (1, 2, 3, 4, 5)
print(
    f"\n I'm of type {type(mytuple)} and will be printed as a collection of elements {mytuple}"
)

try:
    print(
        f"\n If you try to change a tuple collection you will get the following error"
    )
    mytuple[2] = 0

except TypeError as e:
    print(f"\n {e}")


# String to List Conversion
mystring = "Im a List"
typecatstedlist = list(mystring)
print(f"{typecatstedlist}")

#Define a Set: A set allows a ordered sequence of data without duplicates
myset = {1,2,3,3,4,5,6,6,6}
print(f"\n I'm a set with the name myset and values {myset}and i don't allow duplicates in my collection")

#Convert a dictionary to List
mydictionary = {
    "name": "heirl",
    "hobby":"learning"
}
# A dictionary is a key value order pair collection which doesn't maintain the sequence
# A dictionary can be converted to a tuple or list using the items function/method on dictionary object
dict_to_tuple = tuple(mydictionary.items())
print(f"\n dict.items() will provide an iterable for the key value objects")
print(f"\n I'm a dictionary and my data type is {type(mydictionary)}")
print(dict_to_tuple)

#Convert a List to Dictionary
# They key value pairs should be defined as a individual list inside a parent list
updated_info_my_dict = [['name','Athen'],['pattern','time'],['day_part', 'morning']]
print(f"\n use the update method of dictionary object to add/modify the elements into the dictionary")
#Helpful link on dictionary update https://phoenixnap.com/kb/python-add-to-dictionary
mydictionary.update(dict(updated_info_my_dict))
print (mydictionary)

#Using inidividual lists to update a dictionary
#Use zip to create dictionary items from two lists. The first list contains keys, and the second contains the values.
my_keys = ["sleep", "wake"]
my_values = ['12:30a.m', '10:00a.m']
for key,value in zip(my_keys, my_values):
    mydictionary[key] = value
print(f"\n updated dictionary using zip method {mydictionary} #Note: The zip function matches elements from two lists by index, creating key-value pairs.")

print(f"\n Length is a function used to retrieve the length of the data and it will work on strings, lists,tuples, dictionaries")
print(f"\n Length of a dictionary will be categorized based on the keyporder pair '{len(mydictionary)}'")