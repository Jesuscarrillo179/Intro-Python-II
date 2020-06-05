# Write a class to hold player information, e.g. what room they are in
# currently.
from color import Color
import random

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
            print("")
        else:
            print("\nInventory is empty\n")
    
    def attackMob(self, item):
        for i in self.items:
            if item == i.name:
                outputDamage = random.randint(int(i.damage[0]), int(i.damage[2]))
                return outputDamage
            else:
                print("cant find that Object!")
                outputDamage = 0
                return outputDamage

class Enemy(Player):
    def __init__(self, name, current, health, damage):
        super().__init__(name, current)
        self.current = current
        self.health = health
        self.damage = damage

    def attackPlayer(self):
        outputDamage = random.randint(int(self.damage[0]), int(self.damage[2]))
        return outputDamage
