from menu.item_menu import Menu
class Beers(Menu):
    def __init__(self, name, price, description):
        super().__init__(name, price)
        self.description = description
    
    def __str__(self):
        return f'{self.name} | {self.price} | {self.description}'