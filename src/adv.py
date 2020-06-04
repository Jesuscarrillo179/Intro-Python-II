from room import Room
from player import Player
from item import Item
from color import Color

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

items = {
    'axe': Item("Axe", "has some rust, but still sharp."),
    'rock': Item("Rock", "the rock is the size of my fist, but looks pretty usless")
}
# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# creates items in game

room['outside'].setItems(items["axe"], items["rock"])
room['foyer'].setItems(items["rock"])

# input massage panel
inputMessage = f"""
     {Color.GREEN}[w]{Color.END} North        {Color.CYAN}[i]{Color.END} Inventory\n
{Color.YELLOW}[a]{Color.END} West  {Color.YELLOW}[d]{Color.END} East    {Color.PINK}[l]{Color.END} Current Location\n
     {Color.YELLOW}[s]{Color.END} South        {Color.PURPLE}[k]{Color.END} Location Items\n 
{Color.BLUE}[m]{Color.END} Map    {Color.RED}[q]{Color.END} Quit   {Color.GREEN}[f]{Color.END} Pay respects
"""

# checks if route is available
def checkRoute(direction):
    value = getattr(room[player.current], direction)
    if not value == None:
        for key, val in room.items():
            if val == value:
                player.current = key
                print(f"\nyou went to {Color.YELLOW}{room[player.current].name}{Color.END}.")
    else:
        print("\nSorry, you cannot go there!")

# shows map
def showMap():
    compass = {
    'North':'n_to',
    'South':'s_to',
    'East':'e_to',
    'West':'w_to'
    }
    print(f"\n{Color.YELLOW}Available Routes:{Color.END}\n")
    for key, val in compass.items():
        value = getattr(room[player.current] , val)
        if not value == None:
            print(f"{Color.GREEN}{key}:{Color.END}\n  {value}\n")

# shows current location
def showLocation():
    print(f"\n{room[player.current]}\n{Color.CYAN}Description:{Color.END} {room[player.current].description}")

# welcomes player
name = input(f"\n{Color.YELLOW}Hello there! What is your name?{Color.END}\n")

if name == '':
    print(f"{Color.RED}If your not telling, then we are not playing!{Color.END}")
else:
    player = Player(name, "outside")

    print(f"\nWelcome {Color.GREEN}{player.name}{Color.END}! Choose your path and start your adventure!\n")
    userInput = input(f"{inputMessage}\n")
    while not userInput == 'q':
        north = 'n_to'
        south = 's_to'
        east = 'e_to'
        west = 'w_to'

        if userInput == 'w':
            print("------------------------------------------")
            checkRoute(north)
        elif userInput == 's':
            print("------------------------------------------")            
            checkRoute(south)
        elif userInput == 'd':
            print("------------------------------------------")
            checkRoute(east)
        elif userInput == 'a':
            print("------------------------------------------")
            checkRoute(west)
        elif userInput == 'm':
            print("------------------------------------------")
            showMap()
        elif userInput == 'p':
            print("------------------------------------------")
            showLocation()
        elif userInput == 'f':
            print("------------------------------------------")
            print(f"\n{Color.CYAN}Respects Paid.{Color.END}")
        elif userInput == 'k':
            # pickup items from room
            print("------------------------------------------")
            while not userInput == 'g':
                print(f"\n{room[player.current].callItems()}\n")
                userInput = input("[g] Go Back [h] Help\n")
                if userInput == 'h':
                    print("\nto pickup an item, enter the number\n")
                if userInput == 'g':
                    pass
                elif userInput > "0":
                    room[player.current].grabItem(userInput)
        elif userInput == 'i':
            # checks inventory
            print("------------------------------------------")
            while not userInput == 'g':
                print(f"\n{room[player.current].callItems()}\n")
                userInput = input("[g] Go Back [h] Help\n")
                if userInput == 'h':
                    print("\nto drop an item, enter the number\n")
                if userInput == 'g':
                    pass
                elif userInput > "0":
                    room[player.current].dropItem(userInput) #work on this
        else:
            print("------------------------------------------")
            print(f"\n{Color.RED}Sorry, that is not a valid input{Color.END}")

        userInput = input(f"{inputMessage}\n")

    print(f"\n{Color.RED}game over.{Color.END}")

