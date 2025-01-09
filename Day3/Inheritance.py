class Vehicle:
    def __init__(self, name, type, price):
        self.name = name
        self.type = type
        self.price = price

    def shout_vehicle_info(self):
        return (
            f"\n My {self.name} is a {self.type} and its price is {self.price} dollars"
        )


# here we're inheriting the Parent class by delcaring it in the Parenthesis
class Car(Vehicle):
    def car_sound(self):
        return f"\n sususuussususus"


c1 = Car("Porsche", "car", "3.2M")
print(c1.shout_vehicle_info())
print(c1.car_sound())
