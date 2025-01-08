# A lambda is a function without a name and we refered it as Anonyomus function
# Declaring a lambda and assigining it to a variable
a = lambda x: x + 1
# To call the lambda we need to call the variable with the parameters
print(a(2))

# The power of lambda is better shown when you use them as an anonymous function inside another function.
def myfunc(n):
    return lambda a: a * n


mydoubler = myfunc(2)
print(mydoubler(10))
