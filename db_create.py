import mysql.connector

conn = mysql.connector.connect(host="localhost",user="root",passwd="password")
cur = conn.cursor()

cur.execute("drop database nothing_shop")
cur.execute("create database nothing_shop")

conn.close()

conn = mysql.connector.connect(host="localhost",user="root",passwd="password",database="nothing_shop")
cur = conn.cursor()

products = [
    ["Item1", "10.00", "12343"],
    ["Item2", "432.00", "1233"],
    ["Item3", "3420.00", "134323"],
    ["Item4", "4310.00", "123"],
    ["Item5", "1340.00", "1323"],
    ["Item6", "140.00", "1243"],
    ["Item7", "130.00", "12323"],
    ["Item8", "12340.00", "1423"],
    ["Item9", "140.00", "1243"],
    ["Item10", "1230.00", "1243"]
]

cur.execute("create table products(pid int primary key, name varchar(30), price numeric(13,2), stock int);")

i = 1
for item in products:
    cur.execute(f"insert into products values({i}, '{item[0]}', {item[1]}, {item[2]})")
    i+=1

conn.commit()

