from color import Color

class Item:
    def __init__(self, name, description):
        self.id = None
        self.name = name
        self.description = description

    def __str__(self):
        return f"{Color.CYAN}{self.name}{Color.END}: {self.description}"

    def on_take(self):
        print(f"\nYou have picked up {Color.YELLOW}{self.name}{Color.END}.")

    def on_drop(self):
        print(f"\nDropped {Color.YELLOW}{self.name}{Color.END}.")

class Weapon(Item):
    def __init__(self, name, description, damage):
        super().__init__(name, description)
        self.damage = damage

    def __str__(self):
        return f"{Color.CYAN}{self.name}{Color.END}: {self.description}\nDamage Range: {self.damage}"