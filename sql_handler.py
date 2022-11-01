import mysql.connector

from boxprint import box

conn = mysql.connector.connect(host="localhost",user="root",passwd="password",database="nothing_shop")
cur = conn.cursor()

def getPIDs():
    cur.execute("select pid from products")
    pids = cur.fetchall()
    print(pids)
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

# Cart Interface
def exportAsCSV():
    # TODO
    pass

def removeProduct():
    # TODO
    pass


# Customer Interface
def addProduct():
    # TODO
    pass


# Admin Interface
def listProduct():
    # TODO
    pass

def unlistProduct():
    # TODO
    pass