class Dog:
    name = "Dog"

    def _init__(self):
        self.name = Dog.name

    def sound(self, custom_sound):
        return f" Hi I'm {self.name} and i can sound u as commanded {custom_sound}"


class Cat:
    name = "Cat"

    def _init__(self):
        self.name = Cat.name

    def sound(self, custom_sound):
        return f" Hi I'm {self.name} and i can sound u as commanded {custom_sound}"


# Here we using the same name for two different classes
d1 = Dog()
print(d1.sound("Bow Bow"))
c1 = Cat()
print(c1.sound("Meow Meow"))
