# Implement a class to hold room information. This should have name and
# description attributes.
from color import Color
from item import Item
from player import Player

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = self.setItems()
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        return f"{Color.BLUE}Name:{Color.END} {self.name}"
    
    def setItems(self, *args):
        self.items = [i for i in args]
        return self.items
    
    def callItems(self):
        index = 0
        for item in self.items:
            if not item == None:
                index += 1
                item.id = index 
                print(f"\n[{str(item.id)}] {item}")
            else:
                pass
    
    def grabItem(self, input):
        for item in self.items:
         if int(input) == item.id:
            print(f"\nAdded {item.name} to inventory.")
            Player.items = [item]
            self.items.pop(item.id - 1)

        