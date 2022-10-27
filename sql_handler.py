import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="password",database="nothing_shop")

cur = conn.cursor()

def getProducts():
    cur.execute("select * from products")
    out = cur.fetchall()
    return out

def getProductNumber():
    cur.execute("select count(*) from products")
    result = cur.fetchall()
    num = result[0][0]
    return num

def addProduct(name,price,stock):
    num = getProductNumber()
    pid = "N"+str(num+1)
    cur.execute(f'insert into products values("{pid}", "{name}", {price}, {stock})')

# addProduct("Pen", "32.65", "333")
print(getProducts())
