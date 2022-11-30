# Cart

# The cart module used by the customer interface.

from boxprint import box, pad
import sql_handler as sqh
import csv

# The cart is temporary and is cleared on exit, unlike the database
user_cart = [] # Product ids are stored in the cart

# A function to start a loop
def cart_init():
    
    # Use a while loop to accept and process input
    while True:

        box(["Cart"], width=10)

        showCart()

        print("[CART] q:QUIT r:REMOVE x:EXPORT")
        ch = input(": ")

        if ch=="r":
            removeProduct()
                
        elif ch=="x":
            exportAsCSV()

        elif ch=="q":
            print("[ Returning to SHOP ]")
            break # Break from this loop to enter previous loop in customer.py

        else:
            print("[ INVALID INPUT ]")


# Some functions are defined here

# Add a product to the cart
def addProduct():
    pid = int(input("Enter the product id: "))
    pids = sqh.getPIDs()

    if pid in user_cart:
        box(["Product already in cart"], width=5)

    elif pid in pids:
        user_cart.append(pid)
        product = sqh.getProduct(pid)
        box([f"{product[1]} added to cart"], width=5)

    else:
        print("[ INVALID PRODUCT ID ]")
    
# Remove a product from the cart
def removeProduct():
    pid = int(input("Enter the product id: "))

    if pid in user_cart:
        user_cart.remove(pid)
        product = sqh.getProduct(pid)
        box([f"{product[1]} removed from cart"], width=5)

    else:
        print("[ PRODUCT NOT IN CART ]")

# Show all items in the cart
def showCart():
    if user_cart == []:
        print("[ CART IS EMPTY ]")
    
    else:

        lines = [] # All the lines to be printed

        # Add the header
        lines.append("ID" + "  "+ "Name" + " "*28 + "Price"+ " "*5)
        lines.append("-"*46)

        price_total = 0

        # Add the products
        for pid in user_cart:
            product = sqh.getProduct(pid)
            lines.append(f"{pad(product[0], 2)}  {pad(product[1], 30)}  {pad(product[2], 10)}") # len -> 46
            price_total+=product[2]
        
        box(lines)
        box([f"Total: {price_total}"], width=28) # Print the total price

# Export all items in the cart as a CSV file
def exportAsCSV():
    name = input("Enter name of file (without .csv): ")

    with open(name+".csv", "w", newline="") as f:

        wr = csv.writer(f)
        wr.writerow(["Product ID", "Name", "Price"])

        price_total = 0 # Price of each product is added to the total
        for pid in user_cart:
            product = sqh.getProduct(pid)
            wr.writerow([product[0], product[1], product[2]])
            price_total += product[2] # Keep tally of the prices
        
        # Write the total price
        wr.writerow(["Total", "", price_total])
    
    box([f"Cart was exported to {name}.csv"], width=5)
