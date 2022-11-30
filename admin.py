# The Admin interface

# This module is used to list / unlist products, modify product details
# This interface is supposed to be used by the Administrator of the shop

from boxprint import box
import sql_handler as sqh

box(["Welcome Admin"], width=20)

# Use a while loop to accept and process input
while True:
    print("[ADMIN] q:QUIT l:LIST-ITEM u:UNLIST-ITEM m:MODIFY-ITEM s:SHOW-SHOP")
    ch = input(": ")

    if ch=="l":
        # Get product details
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        # Add the product to database using sql_handler module
        product = sqh.listProduct(name, price, stock)
        if product:
            box([f"{product[1]} added to shop"], width=5)

    if ch=="u":
        pid = int(input("Enter product id: "))
        
        # Remove product from database using sql_handler module
        response = sqh.unlistProduct(pid)

        if response:
            box([f"Product {pid} was removed from shop"], width=5)

    if ch=="m":
        pid = int(input("Enter product id: "))

        # Get new product details
        print("Enter the new details")
        name = input("  Name :")
        price = float(input("  Price:"))
        stock = int(input("  Stock:"))

        product = sqh.modifyProduct(pid, name, price, stock)

        if product:
            box([f"{product[1]} was modified"], width=5)

    if ch=="s":
        # Show all items in the database
        sqh.showShop()

    if ch=="q":
        print("[ Exiting ]")
        exit()