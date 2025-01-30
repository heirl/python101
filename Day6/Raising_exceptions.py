#The raise statement allows the programmer to force a specified exception to occur. For example:
#raise NameError('HiThere')
#The sole argument to raise indicates the exception to be raised. 
#This must be either an exception instance or an exception class (a class that derives from BaseException, such as Exception or one of its subclasses). 
#If an exception class is passed, it will be implicitly instantiated by calling its constructor with no arguments:
#The finally clause will be executed after the try except
def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")
#divide("1","2")

#Enriching Exceptions with Notes
try:
    raise TypeError('bad type')
except Exception as e:
    e.add_note('Add some information')
    print(e)
    #raise

#raising Multiple Exception in one except statement
try:
    raise TypeError
    raise NameError
    raise ValueError
#Only the First exception will be caught
except (TypeError,NameError,ValueError) as e:
    print(type(e))
finally:
    print("hehe")

"""There are situations where it is necessary to report several exceptions that have occurred. 
This is often the case in concurrency frameworks, when several tasks may have failed in parallel, 
but there are also other use cases where it is desirable to continue execution and collect multiple errors rather than raise the first exception."""
def f():
    excs = [TypeError('error 1'),NameError('error2'),ValueError('error 3')]
    raise ExceptionGroup('there were problems', excs)
f()