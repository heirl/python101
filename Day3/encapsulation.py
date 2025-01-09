class Person:
    def __init__(self, name, quality, state):
        # public member
        self.name = name
        # private member
        # not accessible outside of a class
        # self.__quality = quality
        self.set_quality(quality)
        # Protected member
        self._state = state

    def hidden_persona(self):
        print("Name is ", self.name, "and salary is", self.__quality)

    # setter method to modify the quality
    def set_quality(self, quality):
        self.__quality = quality

    # getter method the access the quality
    def get_quality(self):
        return f"{self.__quality}"


person = Person("Athan", "Secretive", "Evil")
person.hidden_persona()
# The protected member is directly accesible as other members or methods if we call it with a _single undersocre
print(person._state)

# Only accessible inside the class
try:
    print(person.__quality)
except AttributeError as e:
    print(
        "\n It's a private member u can access it using name mangling check the dir(dictionary) of the Object"
    )
    print(dir(person))

# New Thing learned name mangling
print(
    f"\n Accessing the private member using Name mangling and the value is {person._Person__quality}"
)

# Big Threat
person._Person__quality = "OpenMinded"
print(
    f"\n Modifying  the private member using Name mangling and the value is {person._Person__quality}"
)

# The Protective member is helpful when u want to share sensitive data between classes and its sublasses

# Use setter method to set the quality
person.set_quality("Critical")
print("\n", person.get_quality())
