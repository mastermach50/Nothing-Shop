from boxprint import box
import sql_handler as sqh


def cart_init():
    
    box(["Shop"], width=10)

    while True:

        sqh.showCart()

        print("q:QUIT r:REMOVE x:EXPORT`")
        ch = input(": ")

        if ch=="r":
            pid = input("Enter product id: ")
            sqh.removeProduct(pid)
                
        if ch=="x":
            sqh.exportAsCSV()
        
        if ch=="q":
            print("[Exiting]")
            break