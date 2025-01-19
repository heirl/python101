# The "diamond problem" (also sometimes referred to as the "deadly diamond of death") is an ambiguity,
# that arises when a class inherits from two or more classes that have one common superclass.
class A:
    def display(self):
        print("Display method from class A")


class B(A):
    def display(self):
        print("Display method from class B")


class C(A):
    def display(self):
        print("Display method from class C")


class D(B, C):
    pass


d = D()
d.display()

"""Suppose we have classes A, B, C, and D. Class B  and C inherit from A  and D inherits from both B and C. 
This creates a "diamond" shape of inheritance, hence the "diamond problem". 
Let's suppose there's a method display() in class A, which is overridden in classes B and C."""

# Question :
# In this case, when you create an object of class D and call the display() method,
# which display() method should it use? The one in class B or the one in class C?

# Solution: It will call the display method of B because its declared before C as per the  method resolution order (MRO) algorithm

# we can check the method resolution order using the mro method which is inherited from the Object
print(D.mro())
