class Item:
    def __init__(self, name, description):
        self.id = None
        self.name = name
        self.description = description
    
    def __str__(self):
        return f"{self.name}: {self.description}"