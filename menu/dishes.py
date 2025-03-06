from menu.item_menu import Menu

#this class will inherit from the Menu class
class Dishes(Menu):
    def __init__(self, name, price,description):
      super().__init__(name, price)#the dish class will inherit the atributes from the Menu class
      #super() will allow that this class acess information from the parent class
      self.description = description

    def __str__(self):
        return f'{self.name} | {self.price} | {self.description}'