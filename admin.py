from boxprint import box
import sql_handler as sqh

box(["Welcome Admin"], width=20)

while True:
    print("[ADMIN] q:QUIT l:LIST-ITEM u:UNLIST-ITEM m:MODIFY-ITEM s:SHOW-SHOP")
    ch = input(": ")

    if ch=="l":
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        stock = int(input("Enter product stock: "))

        product = sqh.listProduct(name, price, stock)
        if product:
            box([f"{product[1]} added to shop"])

    if ch=="u":
        pid = int(input("Enter product id: "))
        
        response = sqh.unlistProduct(pid)

        if response:
            box([f"Product {pid} was removed from shop"])

    if ch=="m":
        pid = int(input("Enter product id: "))

        print("Enter the new details")
        name = input("  Name :")
        price = float(input("  Price:"))
        stock = int(input("  Stock:"))

        product = sqh.modifyProduct(pid, name, price, stock)

        if product:
            box([f"{product[1]} was modified"], width=5)

    if ch=="s":
        sqh.showShop()

    if ch=="q":
        print("[ Exiting ]")
        exit()