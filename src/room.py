# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

    def add_item(self, new_item):
        self.items.append(new_item)

    def remove_item(self, item):
        self.items.remove(item)
        print(f'You have removed {item} form {self.name}')

    def __str__(self):
        return f'{self.name}, {self.description}'
