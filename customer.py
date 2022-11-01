from boxprint import box
import sql_handler as sqh
import cart

box(["Welcome Customer"], width=20)

box(["Shop"], width=10)

while True:
    print("q:QUIT a:ADD c:GO-TO-CART S:SHOW-SHOP`")
    ch = input(": ")


    if ch=="a":
        pid = input("Enter product id: ")
        sqh.addProduct(pid)

    if ch=="c":
        cart.cart_init()

    if ch=="s":
        sqh.showShop()
    
    if ch=="q":
        print("[Exiting]")
        exit()
