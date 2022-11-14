from boxprint import box, pad
import sql_handler as sqh
import csv

user_cart = []

def cart_init():
    
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
            break

        else:
            print("[ INVALID INPUT ]")

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
    
def removeProduct():
    pid = int(input("Enter the product id: "))

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

        lines.append("ID" + "  "+ "Name" + " "*28 + "Price"+ " "*5)
        lines.append("-"*46)

        price_total = 0

        for pid in user_cart:
            product = sqh.getProduct(pid)
            lines.append(f"{pad(product[0], 2)}  {pad(product[1], 30)}  {pad(product[2], 10)}") # len -> 46
            price_total+=product[2]
        
        box(lines)
        box([f"Total: {price_total}"], width=28)

def exportAsCSV():
    name = input("Enter name of file (without .csv): ")
    with open(name+".csv", "w", newline="") as f:
        wr = csv.writer(f)
        wr.writerow(["Product ID", "Name", "Price"])

        for pid in user_cart:
            product = sqh.getProduct(pid)
            wr.writerow([product[0], product[1], product[2]])
    box([f"Cart was exported to {name}.csv"], width=5)
