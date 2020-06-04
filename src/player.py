# Write a class to hold player information, e.g. what room they are in
# currently.
class Player:
    def __init__(self, name, current):
        self.name = name
        self.current = current

    def __str__(self):
        return f"Name: {self.name}\nCurrent: {self.current}"
        