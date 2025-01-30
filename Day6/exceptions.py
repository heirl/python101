# The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention).
# Standard exception names are built-in identifiers (not reserved keywords)
# The rest of the line provides detail based on the type of exception and what caused it.

# which asks the user for input until a valid integer has been entered,
# but allows the user to interrupt the program (using Control-C or whatever the operating system supports);
while True:
    try:
        number = int(input("Enter a valid number:"))
        # The number will only be printed if its a valid value else the print statement will be skipped and
        # except block code is executed
        print(number)
        break
    except ValueError as e:
        print("Oops thats a wrong type please enter an integer")

# The unhandled exceptions will result in error check for below code
# while True:
#     try:
#         number = int(input("Enter a valid number:"))
#         # The number will only be printed if its a valid value else the print statement will be skipped and
#         # except block code is executed
#         print(number)
#         break
#     # Here we are not handling VAlueerror which will Stop the code execution
#     except TypeError as e:
#         print("Oops thats a wrong type lease enter an integer")
#

## Multiple except statements
while True:
    try:
        number = int(input("Enter a valid number for the multiple exceptions code:"))
        # The number will only be printed if its a valid value else the print statement will be skipped and
        # except block code is executed
        print(number)
        break
    # Here we are not handling VAlueerror which will Stop the code execution
    except TypeError as e:
        print(e)
    except ValueError as e:
        print("Oops thats a wrong type lease enter an integer")


# Exception Inheritance Code
class B(Exception):
    pass


class C(B):
    pass


class D(C):
    pass


# Here the exceptions are raised based upon the matches
for cls in [B, C, D]:
    try:
        raise cls()
    except D:
        print("D")
    except C:
        print("C")
    except B:
        print("B")
# Reversing the exception order the matching exception will be raised first ! Note C and D are derived from the B
# The below try catch will always raise an exception related to B as it is the parent class of C and D
for cls in [B, C, D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")


#Custom Exception
class MyException(Exception):
    name="MyException"

# Making custom exceptions
try:
    raise MyException("ohoooooo")
except MyException as me:
    print(me)

#Exceptions
try:
    raise MyException('spam','eggs')
except Exception as inst:
    print(type(inst))
    print(inst)
"""BaseException is the common base class of all exceptions. 
One of its subclasses, Exception, is the base class of all the non-fatal exceptions. Exceptions which are not subclasses of Exception are not typically handled, 
because they are used to indicate that the program should terminate. 
They include SystemExit which is raised by sys.exit() and KeyboardInterrupt which is raised when a user wishes to interrupt the program."""