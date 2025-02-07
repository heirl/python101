#List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
basket = [ fruit for fruit in fruits if fruit !="banana"]
print(basket)

#without a condition in list comprhension
numbers = [1,2,3,4,5]
multiple_with_3 = [number*3 for number in numbers]
print(multiple_with_3)

#Writing a condition in the expression of List Comprehension
divide_with_2 = [number if number%2 == 0 else 0 for number in multiple_with_3]
print(divide_with_2)
