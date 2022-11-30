# SQL Handler

# This module is used to communicate with the MySQL Database Server.
# This is the module that accesses data from the database and parses it for
# easier use throughout the program.

import mysql.connector
from boxprint import box

conn = mysql.connector.connect(host="localhost",user="root",passwd="password",database="nothing_shop")
cur = conn.cursor()

# Get a list of all the product IDs
def getPIDs():
    cur.execute("select pid from products")
    data = cur.fetchall()
    pids = []

    for item in data:
        pids.append(item[0])

    return pids

# Get all the products in the shop
def getShop():
    cur.execute("select * from products")
    products = cur.fetchall()
    return products

# Print all the products in the shop
def showShop():
    products = getShop()

    if products == []:
        box(["Shop is Empty"], width=5)
    
    else:
        for item in products:
            box([
            f"ID: {item[0]}",
            f"Name  :  {item[1]}",
            f"Price :  {item[2]}",
            f"Stock :  {item[3]}",
            ], width=30)

# Get the details of a product using its ID
def getProduct(pid):
    cur.execute(f"select * from products where pid={pid}")
    product = cur.fetchall()

    if product:
        return product[0]
    else:
        return False

# List a product in the shop
def listProduct(name, price, stock):
    pids = getPIDs()

    for n in range(1, len(pids)+2):
        if n not in pids:
            newpid = n
            break

    try:
        cur.execute(f"insert into products values({newpid}, '{name}', {price}, {stock})")
        conn.commit()

    except:
        print("[ INVALID PARAMETERS ]")
        return False

    return getProduct(newpid)

# Unlist a product from the shop
def unlistProduct(pid):
    pids = getPIDs()

    if pid in pids:
        cur.execute(f"delete from products where pid={pid}")
        conn.commit()
        return True
    
    else:
        print("[ INVALID PRODUCT ID ]")
        return False

# Modify the details of a product in the shop
def modifyProduct(pid, name, price, stock):
    
    if pid in getPIDs():
        cur.execute(f"update products set name='{name}', price={price}, stock={stock} where pid={pid}")
        conn.commit()

        return getProduct(pid)

    else:
        print("[ INVALID PRODUCT ID ]")
        return False
