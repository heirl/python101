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
mystring = "I'm a List"
typecatstedlist = list(mystring)
print(f"{typecatstedlist}")
