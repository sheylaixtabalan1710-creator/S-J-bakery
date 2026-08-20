import random
from Cake import Cake
from Cookies import Cookies
# The boss
# The Menu class manages the bakery items in the customer's cart.
# It allows items to be added and calculates the total during checkout.


item1 = Cake("Chocolate Cake", 15.00)
item2 = Cake("Vanilla Cake", 15.00)
item3 = Cake("Tres Leches Cake", 15.00)
item4 = Cookies("Chocolate Chip Cookie", 3.00)
item5 = Cookies("Oatmeal Raisin Cookie", 3.00)
item6 = Cookies("Smores Cookie", 3.00)




class Menu:
    def __init__(self):
        self.items = []
    def add(self, item, quantity):
        for i in range(quantity):
            self.items.append(item)
        print(f"{quantity} {item.name}(s) added!")
    def checkout(self):
        total = 0
        counted_items = []

        print("========== RECEIPT ==========")
        print("Your order:")

        for item in self.items:
            if item not in counted_items:
                quantity = self.items.count(item)
                item_total = item.price * quantity
                total += item_total
                print(f"{quantity} x {item.name} - ${item_total:.2f}")
            counted_items.append(item)
        print("--------------------------------")
        print(f"Total: ${total:.2f}")
        print("================================")

Bakery = {"1": item1, "2": item2, "3": item3, "4": item4, "5": item5, "6": item6, "cart": Menu()}

print("Welcome to our Bakery! Please select an item to add to your cart:")
print()
while True:
    print("1. Chocolate Cake - $15.00")
    print("2. Vanilla Cake - $15.00")
    print("3. Tres Leches Cake - $15.00")
    print("4. Chocolate Chip Cookie - $3.00")
    print("5. Oatmeal Raisin Cookie - $3.00")
    print("6. Smores Cookie - $3.00")
    print()

    try:
        choice = input("Please select an item (1-6) or type 'checkout' to finish: ")
  
        if choice == "checkout":
            break
        elif choice in Bakery:
            print()
            quantity = int(input(f"How many {Bakery[choice].name}s would you like to add? "))
            Bakery["cart"].add(Bakery[choice], quantity)
        else:
            print()
            print("Invalid choice. Please try again.")
    except Exception as e:
        print("Something went wrong. Please try again.")

print()
Bakery["cart"].checkout()
print("Thank you for your order!")
      


