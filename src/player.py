# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, room, items=[]):
        self.name = name
        self.room = room
        self.items = []

    def print_items(self):
        for item in self.items:
            print(f'Inventory: \n{item.name} = {item.description}\n')

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, item):
        self.items.remove(item)
        print(f'You have left your {item}')

    def __str__(self):
        return f'{self.name}, {self.room}, {self.items}'
