# We can declare variables of different data types in Python without declaring its in the initilization
x = 1
print(f"I'm a type of {type(x)} and my type is guessed by the interperter")
y = 20.0
print(f"I'm a type of {type(y)} and my type is guessed by the interperter")
stringtype = "I'm a String"
print(f"I'm a type of {type(stringtype)} and my type is guessed by the interperter")

# Explicit Data Type Definition
z = int("4")
print(f"I Declared as a string but typecasted to {type(z)}")
n = float(3)
print(f"I Declared as a int but typecasted to {type(n)} and my value is {n}")

# Generating a Random number using random function in python
import random

random_number = complex(random.randrange(2.0, 10.0))
print(f"I'm a random number {random_number}")

# None Type of Python
a = None
print(type(a))

# Boolean Type of python
b = True
print(f"\n The Boolean value is {b} and type is {type(b)}")
c = False
print(f"\n The Boolean value is {c} and type is {type(c)}")


# Range Type in Python
x = range(1, 6, 3)  # starting, ending value, stepup value

# display x:
for y in x:
    print(y)

# display the data type of x:
print(f"{type(x)} is range")
