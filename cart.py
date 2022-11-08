from boxprint import box, pad
import sql_handler as sqh

user_cart = []

def cart_init():
    
    box(["Cart"], width=10)

    while True:

        showCart()

        print("q:QUIT r:REMOVE x:EXPORT")
        ch = input(": ")

        if ch=="r":
            removeProduct()
                
        if ch=="x":
            sqh.exportAsCSV()
        
        if ch=="q":
            print("[ Returning to SHOP ]")
            break

def addProduct():
    pid = int(input("Enter the product id: "))
    pids = sqh.getPIDs()

    if pid in user_cart:
        print("Product already in cart")

    elif pid in pids:
        user_cart.append(pid)
        product = sqh.getProduct(pid)
        box([f"{product[1]} added to cart"], width=5)

    else:
        print("[ INVALID PRODUCT ID ]")
    
def removeProduct():
    pid = int(input("Enter the product id: "))
    pids = sqh.getPIDs()

    if pid in user_cart:
        user_cart.remove(pid)
        product = sqh.getProduct(pid)
        box([f"{product[1]} removed from cart"], width=5)

    else:
        print("[ PRODUCT NOT IN CART ]")

def showCart():

    if user_cart == []:
        print("[ CART IS EMPTY ]")
    
    else:

        lines = []

        lines.append("ID" + "  "+ "Name" + " "*23 + "Price"+ "  ")
        lines.append("-"*40)

        price_total = 0

        for pid in user_cart:
            product = sqh.getProduct(pid)
            lines.append(f"{pad(product[0], 2)}  {pad(product[1], 25)}  {pad(product[2], 9)}") # len -> 40
            price_total+=product[2]
        
        box(lines)
        box([f"Total: {price_total}"], width=28)
