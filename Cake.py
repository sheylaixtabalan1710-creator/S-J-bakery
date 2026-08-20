import random
# Kind 1
# The Cake class represents cakes sold by the bakery.
# It inherits the name and price information from Bakery.
from Bakery import Bakery
class Cake(Bakery):
    def __init__(self, name, price):
        super().__init__(name, price)

    def deliver(self):
        print(f"Your {self.name} will be delivered soon.")
