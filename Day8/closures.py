def outer_function(outer_variable):
    def inner_function(inner_variable):
        print(outer_variable)  # Access outer_variable
        print(inner_variable)  # Access inner_variable
    return inner_function

my_closure = outer_function("Hello!")  # outer_function executed, closure "remembers" the scope
print(my_closure)
#my_closure("World!")  # inner_function called


#The outer function returns the inner function, which "remembers" and has access to the outer function's variables, even after the outer function has finished execution.
#Persistent State Example: Counter
def counter():
    count = 0  # Variable to store the count value
    
    def increment():
        nonlocal count  # This allows modifying the variable from the outer function
        count += 1
        return count
    
    return increment  # Return the closure

# Create the counter function
my_counter = counter()

# Call the closure multiple times
print(my_counter())  # Output: 1
print(my_counter())  # Output: 2
print(my_counter())  # Output: 3s
