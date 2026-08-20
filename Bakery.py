import random
# The blurprint
# The bakery class is the blue print for bakery items.
# It stores the item's name and price and provides methods
# for changing the price and delivering the item.
class Bakery:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def set_price(self, price):
        if price < 0:
            print("Invalid price.")
        else:
            self.price = price
        
        def deliver(self):
            print(f"Your {self.name} will be delivered soon.")
