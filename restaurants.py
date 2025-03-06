from avaliations import Avaliation



class Restaurant:
    restaurants = []

    def __init__(self, name, category):#constructor
        self._name = name.title()#to make a atribute private
        self._category = category.upper()
        self._active = False#as I'll not acess this atribute, I'll let out of the constructor's parameter
        self._rating = []
        Restaurant.restaurants.append(self)
    

    def __str__(self): #to transform the atributes into text (special method)
       return f'{self._name} | {self._category}'
    

    @classmethod#modify atributes let them alternete tha class state(classmethod)
    def list_restaurants(cls):
        print(f"{'Restaurant Name'.ljust(25)} | {'Category'.ljust(25)} | {'Status'.ljust(25)} | {'Avaliations'.ljust(25)}")
        for restaurant in cls.restaurants:
            print(f'{restaurant._name.ljust(25)} | {restaurant._category.ljust(25)} | {restaurant.active.ljust(25)} | {restaurant.avarege_avaliation}')


    @property#serves to transform a method into a property,
            #it means thar instead push a method call the method with parentheses, you can access it directly as an attribute.
    def active(self):
        return '⌧' if self._active else '☐'
    
    def alternate_state(self):#normal method
        self._active = not self._active

    def recive_avaliations(self, client,avaliation):
        avaliation = Avaliation(client, avaliation)
        self._rating.append(avaliation)
    
    @property
    def avarege_avaliation(self):
     if not self._rating:
      return 0
    
     avarege_sum = sum(avaliation._rating for avaliation in self._rating)
     quantidade_avaliacoes = len(self._rating)
     avarege = round(avarege_sum / quantidade_avaliacoes, 1)
     return avarege                                                                               
 



