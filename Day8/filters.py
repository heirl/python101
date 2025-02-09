#Syntax of function
#filter(func, iterable)
#The following points are to be noted regarding filter():

# Unlike map(), only one iterable is required.
# The func argument is required to return a boolean type. If it doesn't, filter simply returns the iterable passed to it. Also, as only one iterable is required, it's implicit that func must only take one argument.
# filter passes each element in the iterable through func and returns only the ones that evaluate to true. I mean, it's right there in the name -- a "filter".

#The filter method accepts only one iterable unlike map
#it's implicit that func must only take one argument.

dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")

palindromes = list(filter(lambda word: word == word[::-1], dromes))

print(palindromes)


#how to reverse a string in Python
dromes = ("demigod", "rewire", "madam", "freer", "anutforajaroftuna", "kiosk")
for word in dromes:
    word = word[::-1]
    print(word)