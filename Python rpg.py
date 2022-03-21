import cmd
import textwrap
import sys
import os 
import time


screen_width = 100

##### Player Setup ##### 
class player:
    def __init__(self):
        self.name = ''
        self.hp = 0
        self.mp = 0
        self.status_effects = []
        self.location = 'start'
myPlayer = player()

##### Title screen #####
def title_screen_selections():
    option = input("> ")
    if option.lower() == ("play"):
        start_game() #placeholder untill written
    elif option.lower() == ("help"):
        help_menu() #placeholder untill written
    elif option.lower() == ("quit"):
        sys.exit()
    while option.lower() not in ['play', 'help', 'quit']:
        print("Please enter a valid command.")
        option = input("> ") 
        if option.lower() == ("play"):
            start_game() #placeholder untill written
        elif option.lower() == ("help"):
            help_menu() #placeholder untill written
        elif option.lower() == ("quit"):
            sys.exit()

def title_screen():
    os.system('clear')
    print('############################')
    print('# Wlecome to the Text RPG! #')
    print('############################')
    print('            - Play -        ')
    print('            - Help -        ')
    print('            - Quit -        ')
    title_screen_selections()

def help_menu():
    os.system('clear')
    print('############################')
    print('# Wlecome to the Text RPG! #')
    print('############################')
    print('- Use up, down, left, right to move.')
    print('- Type your commands to do them.')
    print('- Use "look" to inspect something')
    print('- Good luck and have fun!')
    title_screen_selections


##### Map #####
"""
a   b  c  d 
-------------
|  |  |  |  |1 
-------------
|  |  |  |  |2
-------------
|  |  |  |  |3 
--------------
|  |  |  |  |4 
"""

ZONENAME = "",
DESCRIPTION = 'description',
EXAMINATION = 'examine',
SOLVED = False,
UP = 'up', 'north'     
DOWN = 'down', 'south'     
LEFT = 'left', 'west'     
RIGHT = 'right', 'east' 


solved_places = {'a1': False, 'b1' : False, 'c1' : False, 'd1' : False,
                'a2': False, 'b2' : False, 'c2' : False, 'd2' : False,
                'a3': False, 'b3' : False, 'c3' : False, 'd3' : False,
                'a4': False, 'b4' : False, 'c4' : False, 'd4' : False,
                }
                
zonemap = {
    'a1': {
        ZONENAME: "Town",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP:  '',     
        DOWN: 'a2',     
        LEFT: '',     
        RIGHT: 'b2' 
    },
    'a2': {
        ZONENAME: "Town",
        DESCRIPTION: 'description',
        EXAMINATION: 'examine',
        SOLVED: False,
        UP: '',     
        DOWN: 'a2',     
        LEFT: '',     
        RIGHT: 'b2' 
    }
}


##### Game Interactivity #####
def print_location():
    print('\n' + ('#' * (4 + len(myPlayer.location))))
    print('#' + myPlayer.location.upper() + '#')
    print('#' + zonemap[myPlayer.position][DESCRIPTION] + ' #')
    print('\n' + ('#' * (4 + len(myPlayer.location))))

def prompt():
    print("\n " + "===============================")
    print("< What would you like to do?")
    action == input("> ")
    acceptable_actions = ('move', 'go', 'travel', 'walk', 'quit', 'examine', 'inspect', 'interact', 'look')
    while action.lower() not in acceptable_actions:
        print("Unknown action, try again \n")
        action == input("> ")
    if action.lower() == 'quit':
        sys.exit
    elif action.lower() in ['move', 'go', 'travel', 'walk']:
        player_move(action.lower())
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        player_examine(action.lower())

def player_move(myAction):
    ask = "Where would you like to move to?\n"
    dest = input(ask)
    if dest in ['up', 'north']:
        destination = zonemap[myPlayer.location][UP]
        movement_handler(destination)
    elif dest in ['left', 'west']:
        destination = zonemap[myPlayer.location][LEFT]
        movement_handler(destination)
    elif dest in ['right', 'east']:
        destination = zonemap[myPlayer.location][RIGHT]
        movement_handler(destination)
    elif dest in ['down', 'south']:
        destination = zonemap[myPlayer.location][DOWN]
        movement_handler(destination)


def movement_handler(destination):
    print("\n" + "You have moved to the " + destination + ".")
    myPlayer.location = destination
    print_location() 

def player_examine(action):
    if [zonemap][myPlayer.location][SOLVED]:
        print("You have already exhausted this zone.")
    else: 
        print("Placeholder puzzle or smth")

##### Game Functionality #####
def start_game():
    print("something")