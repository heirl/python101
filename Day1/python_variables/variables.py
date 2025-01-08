#Declaring a variable in Python
x=1
print(f"\n I'm a variable declard with the name x and my value is : {x}")
#Declaring multiple values in a single line
a,b,c=1,2,3
print(f"\n Declaring Multiple variables in a singe Lines as follows 'a,b,c=1,2,3' and the outpt for each variable is {a},{b},{c}")
#Declaring same value to different Variables
z=y=m="Orange"
print(f"\n Declaring same value to different Variables 'z=y=m=Orange' and the Output is {z,y,m}")
#Writing a mult-line comment using """"""
"""HI
I'm
a
multi-line comment"""

"Unpack a Collection If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking."
fruits = ["apple", "banana", "cherry"]
print("\n Unpack a collection")
fruit1, fruit2, fruit3 = fruits
print(f"\n Fruit: {fruit1}\tFruit: {fruit3}\tFruit: {fruit3}")

print("\n To modify a global variable declared outside the function we need to use global Keyword")
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("\n Python is " + x)
