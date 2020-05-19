import sys
import textwrap

from room import Room
from player import Player
from item import Item

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player('Rupert', room['outside'])
hammer = Item('hammer', 'A tool to hit things with')
player.add_item(hammer)

directions = {'n': 'n_to', 's': 's_to', 'e': 'e_to', 'w': 'w_to'}

player_input = True

# Write a loop that:
while player_input != False:
    # * Prints the current room name
    print(f'\nYou are currently in {player.room.name}.')

    # * Prints the current description (the textwrap module might be useful here).
    print(f'{player.room.description}')

    # * Waits for user input and decides what to do.
    player_input = input("\nEnter a command:\n")
    print('')
    player_selection = player_input.split()

    command = player_selection[0]

    # If more than one argument is passed on script call
    if len(player_selection) > 1:
        item = player_selection[1]

        # if player input is get or take
        if command == 'get' or command == 'take':
            room_item = player.room.remove_item(item)

            if room_item:
                player.add_item(room_item)
            else:
                print("***** That item is not the room *****")
        # If player input is drop
        elif command == 'drop':
            player_item = player.remove_item(item)
            player.room.add_item(player_item)
    # If only one argument is passed on script call
    elif command == 'q' or 'n' or 's' or 'e' or 'w' or 'i':
        if command == 'q':
            print('Game Over')
            player_input = False
        elif command == 'i' or command == 'inventory':
            player.print_inventory()
        else:
            direction = directions[player_input]
            # If the user enters a cardinal direction, attempt to move to the room there.
            try:
                player.room = getattr(player.room, direction)
            # Print an error message if the movement isn't allowed.
            except AttributeError:
                print("\n***** You can't go in that direction *****\n")
