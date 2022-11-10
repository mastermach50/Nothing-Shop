from boxprint import box
import sql_handler as sqh
import cart

box(["Welcome Customer"], width=20)

box(["Shop"], width=10)

while True:
    print("[SHOP] q:QUIT a:ADD c:GO-TO-CART s:SHOW-SHOP")
    ch = input(": ")

    if ch=="a":
        cart.addProduct()

    if ch=="c":
        cart.cart_init()

    if ch=="s":
        sqh.showShop()
    
    if ch=="q":
        print("[ Exiting ]")
        exit()
