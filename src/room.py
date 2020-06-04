# Implement a class to hold room information. This should have name and
# description attributes.
from color import Color
from item import Item

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
        if not self.items == None:
            index = 0
            for item in self.items:
                index += 1
                item.id = index 
                print(f"\n{Color.YELLOW}[{str(item.id)}]{Color.END} {Color.GREEN}{item.name}{Color.END}: {item.description}")
        else:
            print("\nThis place is empty.")

        