from boxprint import box
import sql_handler as sqh

box(["Welcome Admin"], width=20)

while True:
    print("q:QUIT l:LIST-ITEM u:UNLIST-ITEM s:SHOW-SHOP")
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

    if ch=="s":
        sqh.showShop()

    if ch=="q":
        print("[ Exiting ]")
        exit()