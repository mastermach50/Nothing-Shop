import mysql.connector
from boxprint import box

conn = mysql.connector.connect(host="localhost",user="root",passwd="password",database="nothing_shop")
cur = conn.cursor()

def getPIDs():
    cur.execute("select pid from products")
    data = cur.fetchall()
    pids = []

    for item in data:
        pids.append(item[0])

    return pids

def getShop():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

# General Functions
def showShop():
    products = getShop()
    for item in products:
        box([
        f"ID: {item[0]}",
        f"Name  :  {item[1]}",
        f"Price :  {item[2]}",
        f"Stock :  {item[3]}",
        ], width=30)

def getProduct(pid):
    cur.execute(f"select * from products where pid={pid}")
    product = cur.fetchall()
    return product[0]

# Admin Interface
def listProduct():
    # TODO
    print("{NOT IMPLEMENTED}")
    pass

def unlistProduct():
    # TODO
    print("{NOT IMPLEMENTED}")
    pass