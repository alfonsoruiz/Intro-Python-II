# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    '''
        Class modeling properties of a room

        Attributes: 
            name (String): Name of room.
            description (String): description of room.
    '''

    def __init__(self, name, description):
        '''Initializes Room class with room name and a room description'''
        self.name = name
        self.description = description

    def __str__(self):
        return f'{self.name}, {self.description}'
