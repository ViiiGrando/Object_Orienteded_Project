from restaurants import Restaurant
from menu.dishes import Dishes
from menu.beers import Beers

restaurant_square = Restaurant('Square', 'Gourmet')#this is a instance for the class restaurant
beer = Beers('Water', 5.00, 'Big bottle')
dish = Dishes('Rice', 15.00, 'White rice')



def main():
    print(beer)
    print(dish)

if __name__ == '__main__':
    main() 