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
    print(products)

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

def getProduct(pid):
    cur.execute(f"select * from products where pid={pid}")
    product = cur.fetchall()
    return product[0]

# Admin Interface
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

def unlistProduct(pid):
    pids = getPIDs()

    if pid in pids:
        cur.execute(f"delete from products where pid={pid}")
        conn.commit()
        return True
    
    else:
        print("[ INVALID PRODUCT ID ]")
        return False

