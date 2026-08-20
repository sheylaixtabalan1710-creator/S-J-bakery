import random
# Kind 2
# The Cookies class represents cookies sold by thebakery.
# It inherits the name and price informaion from Bakery.
from Bakery import Bakery
class Cookies(Bakery):
    def __init__(self, name, price):
        super().__init__(name, price)
    def deliver(self):
        print(f"Your {self.name} will be delivered soon.")
        