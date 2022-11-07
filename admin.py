from boxprint import box
import sql_handler as sqh

box(["Welcome Admin"], width=20)

box(["Shop"], width=10)

while True:
    print("q:QUIT l:LIST-ITEM u:UNLIST-ITEM S:SHOW-SHOP")
    ch = input(": ")

    if ch=="l":
        sqh.listProduct()

    if ch=="u":
        sqh.unlistProduct()

    if ch=="s":
        sqh.showShop()

    if ch=="q":
        print("[ Exiting ]")
        exit()