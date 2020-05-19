# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, inventory=[]):
        self.name = name
        self.room = room
        self.inventory = []

    def print_inventory(self):
        if len(self.inventory) < 1:
            print(f'***** There are currently no items in your inventory *****')

        for item in self.inventory:
            print(f'Inventory: \n{item.name} = {item.description}\n')

    def add_item(self, new_item):
        self.inventory.append(new_item)
        new_item.on_take()

    def remove_item(self, item):
        for inventory_item in self.inventory:
            if inventory_item.name == item:
                index_of_item = self.inventory.index(inventory_item)
                inventory_item.on_drop()
                return self.inventory.pop(index_of_item)

    def __str__(self):
        return f'{self.name}, {self.room}, {self.inventory}'
