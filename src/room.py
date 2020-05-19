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
        for room_item in self.items:
            if room_item.name == item:
                index_of_item = self.items.index(room_item)
                room_item.on_take()
                return self.items.pop(index_of_item)
            else:
                return False

    def __str__(self):
        return f'{self.name}, {self.description}, {self.items}'
