class Item:
    '''
    Class modeling Items a player or room can have

    Attributes:
        name (String): Item name.
        description: (String): description of item.
    '''

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        print(f'You have taken {self.name}')

    def on_drop(self):
        print(f'You have droped {self.name}')

    def __str__(self):
        return f'{self.name}, {self.description}'
