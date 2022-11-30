# The Customer interface

# This interface is used to add products to cart and also to start the cart module
# to manage the cart (i.e add / remove items, view cart and export items in cart as CSV files)
# This interface is supposed to be used by the customer

from boxprint import box
import sql_handler as sqh
import cart

box(["Welcome Customer"], width=20)

box(["Shop"], width=10)

# Use a while loop to accept and process input
while True:
    print("[SHOP] q:QUIT a:ADD c:GO-TO-CART s:SHOW-SHOP")
    ch = input(": ")

    if ch=="a":
        # Add a product to the Cart
        cart.addProduct()

    if ch=="c":
        # Start the cart loop
        cart.cart_init()

    if ch=="s":
        sqh.showShop()
    
    if ch=="q":
        print("[ Exiting ]")
        exit()
