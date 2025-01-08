# syntax of a function
# def functionname(parameters):
def myfunction(user):
    print(f"Hi {user} I'm a function and  you can see my type below")


userinput = input("Please enter your name : ")
myfunction(userinput)
print(type(myfunction))

print(f"Calling a function with wrong number of parameters")


def func_two_params(param1, param2):
    print(f"I Have two parameters {param1},{param2}")


try:
    print(func_two_params("wrong"))
except TypeError as e:
    print(e)

# Arbitary arguments are represented with the * infront of the paramter name
def func_with_args(*varying_parameters):
    # An arbitary argument will return a tuple in the order of parameters the function called
    for i in varying_parameters:
        print(f"\n I'm a parmamter with the following value : {i}")


func_with_args(1, 2, 2, 3, 3, 3, 3)

# Keyword Arguments
# we can pass key-value pairs as a parmater to the function
def fun_keyword(first_parameter, second_paramter, third_paramter):
    print(f"\n In Keyword argument function the passing parmater order doesnt matter")
    print(
        f"first_parameter = I called as a {first_parameter} argument, second_parameter = I called as a {second_paramter} argument,third_parameter = I called as a {third_paramter} argument"
    )


fun_keyword(second_paramter=1, third_paramter=2, first_parameter=3)

# We can declare arbitary number of keyword arguments in functions using **
def fun_arbitary_keyword(**key_vales):
    print(type(key_vales))
    print(f"A arbitary keyword argument returns a dictionary {key_vales.items()}")


fun_arbitary_keyword(name="athan", age=29, character="socipoath")

# Default Paramter
def fun_default(country="India"):
    if country == "India":
        print(f"My Default country is {country}")
    else:
        print(f"User entered country {country}")


fun_default()
fun_default("China")

# Define a positional argument using \ in paramter field after the paramater declartion which allows only positional arguments as arguments
def fun_positional(x, /):
    print("I'm a positonal argument")


try:
    fun_positional(name="Athan")
except TypeError as e:
    print(f"{e} and here only one positional arguments is allowed")

# Define a keyword argument using * in paramter field after the paramater declartion which allows only positional arguments as arguments
def fun_only_keyword(*, name):
    print("I'm a positonal argument")


try:
    fun_only_keyword(10)
except TypeError as e:
    print(f"{e} and here only one Keyword arguments is allowed")
