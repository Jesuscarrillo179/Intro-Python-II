# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current):
        self.name = name
        self.current = current
        self.items = None
        self.health = 10

    def __str__(self):
        return f"Name: {self.name}\nCurrent: {self.current}"
        