import mysql.connector

def check_mysql():
    try:# VALIDATE
        conn = mysql.connector.connect(host="localhost", port="3305",user="root", passwd="password")
        print("MySQL found...")
    except:
        print("[Error] Unable to connect to MySQL")
        exit()

def check_data():
    # VALIDATE
    conn = mysql.connector.connect(host="localhost", port="3305",user="root", passwd="password")
    cursor = conn.cursor()
    try:
        cursor.execute("use nothing_shop")
        print("Database found...")
    except:
        print("[Error] Unable to access database")
        exit()

    try:
        cursor.execute("select * from products")
        print("Tables found...")
    except:
        print("[Error] Unable to access table")
        exit()

