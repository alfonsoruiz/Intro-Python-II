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

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Create object instances
player = Player('Dr.Doctor', room['outside'])
item1 = Item('knife', 'A tool to cut things with')
item2 = Item('hammer', 'A tool to hit things with')
room['outside'].add_item(item1)
room['outside'].add_item(item2)

# Begin game loop
player_input = True
while player_input:
    print(f'\nYou are in {player.room.name}, {player.room.description}.')
    print('Items in room ->')
    player.room.print_items()
    print('')
    player_input = input('Enter a direction or q to exit game: ').split()

    command = player_input[0]

    # If player is getting or dropping items
    if len(player_input) > 1:
        item = player_input[1]

        if command == 'get':
            room_item = player.room.romove_item(item)

            if room_item:
                player.add_to_inventory(room_item)
            else:
                print(f'The {item} is not in the room.')
        elif command == 'drop':
            player_item = player.remove_from_inventory(item)

            if player_item:
                player.room.add_item(player_item)
            else:
                print(f'You do not have the {item} item in your inventory.')
        else:
            print('Invalid command. Enter get or drop followed by the item')

    # If player is moving in a direction, quitting or printing invenotry
    elif command == 'q' or 'n' or 's' or 'e' or 'w' or 'i' or 'inventory':
        if command == 'q':
            print('Game Over')
            player_input = False
        elif command == 'i' or command == 'inventory':
            player.print_inventory()
        elif command == 'n' or 's' or 'e' or 'w':
            command = command + '_to'

            try:
                player.room = getattr(player.room, command)
            except AttributeError:
                print("You can't move in that direction")
    # If commands are invalid
    else:
        print('''
        Invalid command:
        Enter n, s, e, w to go in a direction.
        Enter q to quit
        Enter i or invenotry to print out a players inventory.
        '''
              )
