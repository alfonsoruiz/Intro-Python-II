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
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)

    def romove_item(self, item):
        for room_item in self.items:
            if room_item.name == item:
                item_at_location = self.items.index(room_item)
                return self.items.pop(item_at_location)

    def print_items(self):
        if len(self.items) < 1:
            print('No items in this room')
        else:
            for item in self.items:
                print(item)

    def __str__(self):
        return f'{self.name}, {self.description}'
