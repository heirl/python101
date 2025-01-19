# Multilevel Inheritance
# When a child class becomes a parent class for another child, it's called multilevel inheritance.
class GrandParent:
    def func1(self):
        print("This function is in grandparent class.")


class Parent(GrandParent):
    def func2(self):
        print("This function is in parent class.")


class Child(Parent):
    def func3(self):
        print("This function is in child class.")


# create an object of the child class
child = Child()
child.func1()  # calling function of grandparent class
child.func2()  # calling function of parent class
child.func3()  # calling function of child class
