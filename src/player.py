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
        self.name = name
        self.room = room
        self.inventory = []

    def add_to_inventory(self, new_item):
        self.inventory.append(new_item)
        new_item.on_take()

    def remove_from_inventory(self, item):
        for inventory_item in self.inventory:
            if inventory_item.name == item:
                item_at_location = self.inventory.index(inventory_item)
                inventory_item.on_drop()
                return self.inventory.pop(item_at_location)

    def print_inventory(self):
        if len(self.inventory) < 1:
            print(f'No items {self.name} inventory')
        else:
            print(f'{self.name} inventory:')
            for item in self.inventory:
                print(item)

    def __str__(self):
        return f'{self.name}, {self.room}'
