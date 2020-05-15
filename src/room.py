# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []

        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def print_items(self):
        if len(self.items) == 0:
            return f'Items: There are no items currently in this room'
        else:
            for item in self.items:
                return item

    def add_item(self, new_item):
        self.items.append(new_item)
        self.print_items()

    def __str__(self):
        return f'{self.name}, {self.description}'
