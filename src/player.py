# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    '''
        Class modeling properties of the player.

        Attributes:
            name (String): Player name.
            room (String): Current room player is in.
    '''

    def __init__(self, name, room):
        '''Initializes Player class with the name of the player and current room that the player is in.'''
        self.name = name
        self.room = room

    def __str__(self):
        return f'{self.name}, {self.room}'
