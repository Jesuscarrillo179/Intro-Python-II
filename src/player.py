# Write a class to hold player information, e.g. what room they are in
# currently.
from color import Color

class Player:
    def __init__(self, name, current):
        self.name = name
        self.current = current
        self.items = []
        self.health = 10

    def __str__(self):
        return f"Name: {self.name}\nCurrent: {self.current}"
    
    def callItems(self):
        if not self.items == []:
            index = 0
            for item in self.items:
                if not item == None:
                    index += 1
                    item.id = index 
                    print(f"\n{Color.PINK}[{str(item.id)}]{Color.END} {item}")
        else:
            print("\nInventory is empty")