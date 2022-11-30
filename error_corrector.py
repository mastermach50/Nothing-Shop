# Error Corrector

# A simple script to check whether all the required modules are installed
# and that they are working properly.

def run_checks():
    """Check whether MySQL is installed, it is accessible
    and whether it has the proper databases and tables"""

    # Check for MySQL-Python connector
    try:
        import mysql.connector
        print("[ ok ] mysql.connector working")
    except:
        print("[Error] Unable to import mysql.connector")
        exit()

    # Check for MySQL installation
    try:
        conn = mysql.connector.connect(host="localhost", user="root", passwd="password")
        print("[ ok ] MySQL found")
    except:
        print("[Error] Unable to connect to MySQL")
        exit()

    # Check for database
    try:
        cursor = conn.cursor()
        cursor.execute("use nothing_shop")
        print("[ ok ] Database found")
    except:
        print("[Error] Unable to access database")
        exit()

    # Check for tables
    try:
        cursor.execute("select * from products")
        print("[ ok ] Tables found")
    except:
        print("[Error] Unable to access table")
        exit()

    # Check for CSV module
    try:
        import csv
        print("[ ok ] CSV module found")
    except:
        print("[Error] Unable to import csv")
        exit()

