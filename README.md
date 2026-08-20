Bakery Manager App:
    The Bakery Manager App allows a customer to choose baked goods from a bakery menu and add them to a cart. It keeps track of the items and calculates the total price of the order.
    The customer chooses an item by entering the number that corresponds to the item on the menu. They can also choose how many of each item they want. When they are finished adding items, they can type 'checkout' to finish their order and see the total price.

Features:
- Warmly Welcomes you to our bakery!
- Displays a list of baked goods and their prices
- Allows the user to select an item using its menu number
- Allows the user to choose how many of an item they want
- Adds selected items to a cart
- Keeps track of the total cost
- Allows the user to continue adding items
- Allows the user to type checkout when they are finished
- Displays the final total price using a receipt

How to Use:
1. Look at the bakery menu.
2. Enter the number of the baked goods you want.
3. Enter how many of that item you want.
4. Continue selecting items to add them to your cart.
5. When you are finished, type checkout.
6. The program will display your receipt.


EXAMPLE:
% python3 Menu.py
Welcome to our Bakery! Please select an item to add to your cart:

1. Chocolate Cake - $15.00
2. Vanilla Cake - $15.00
3. Tres Leches Cake - $15.00
4. Chocolate Chip Cookie - $3.00
5. Oatmeal Raisin Cookie - $3.00
6. Smores Cookie - $3.00

Please select an item (1-6) or type 'checkout' to finish: 2

How many Vanilla Cakes would you like to add? 1
1 Vanilla Cake(s) added!
1. Chocolate Cake - $15.00
2. Vanilla Cake - $15.00
3. Tres Leches Cake - $15.00
4. Chocolate Chip Cookie - $3.00
5. Oatmeal Raisin Cookie - $3.00
6. Smores Cookie - $3.00

Please select an item (1-6) or type 'checkout' to finish: 3

How many Tres Leches Cakes would you like to add? 1
1 Tres Leches Cake(s) added!
1. Chocolate Cake - $15.00
2. Vanilla Cake - $15.00
3. Tres Leches Cake - $15.00
4. Chocolate Chip Cookie - $3.00
5. Oatmeal Raisin Cookie - $3.00
6. Smores Cookie - $3.00

Please select an item (1-6) or type 'checkout' to finish: checkout

========== RECEIPT ==========
Your order:
1 x Vanilla Cake - $15.00
1 x Tres Leches Cake - $15.00
--------------------------------
Total: $30.00
================================
Thank you for your order!