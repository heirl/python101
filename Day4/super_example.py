# By default every class inherits object
class characters:
    def __init__(self, name, role):
        self.name = name
        self.role = role

    def show_char_info(self):
        return f"The Character name is {self.name} and the role is {self.role}"


class lost_in_space(characters):
    def __init__(self, name, role, strength):
        # calling init method of Parent
        super().__init__(name, role)
        self.strength = strength

    def show_char_info(self):
        return f"The Character name is {self.name} the role is {self.role} and its strength is {self.strength}"


char_name = input("Please enter your charcater name: ")
char_role = input("Please enter your character role: ")
char_strength = input("Please enter your character Strength: ")

character = lost_in_space(char_name, char_role, char_strength)
print(character.show_char_info())
