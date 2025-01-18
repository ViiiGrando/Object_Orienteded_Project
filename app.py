from restaurants import Restaurant

restaurant_square = Restaurant('Square', 'Gourmet')#this is a instance for the class restaurant
restaurant_pizza = Restaurant('Pizza','Italian' )
restaurant_pizza.recive_avaliations('Victor', 10)

restaurant_pizza.alternate_state()



def main():
    Restaurant.list_restaurants()

if __name__ == '__main__':
    main() 