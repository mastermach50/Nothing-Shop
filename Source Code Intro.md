# Source Code

## Prerequisites

The program is divided into smaller modules for better readability and easier management.
Here is the file structure:

```
admin.py
boxprint.py
cart.py
customer.py
error_corrector.py
main.py
sql_handler.py
```
`admin.py` and `customer.py` are the different interfaces. `cart.py` is a user defined module used by customer.py for certain functions. `error_corrector.py` is use to make sure all the required modules are installed and they are working before executing the program. `boxprint.py` is a user defined module which is used to display the output neatly in boxes. `sql_handler.py` is used by the python program to communicate with the MySQL database.

`main.py` is where the program starts, it the file that should be executed to start the program.

## Code

### main.py

```py
from boxprint import box
import error_corrector as ec

print("""
888b    888          888    888      d8b                  
8888b   888          888    888      Y8P                  
88888b  888          888    888                           
888Y88b 888  .d88b.  888888 88888b.  888 88888b.   .d88b. 
888 Y88b888 d88""88b 888    888 "88b 888 888 "88b d88P"88b
888  Y88888 888  888 888    888  888 888 888  888 888  888
888   Y8888 Y88..88P Y88b.  888  888 888 888  888 Y88b 888
888    Y888  "Y88P"   "Y888 888  888 888 888  888  "Y88888
                                                       888
We sell everything...                             Y8b d88P
                                                   "Y88P" """)

print("Starting...")
ec.run_checks()

box(["Please Log In"], width=20)
user = input("Select User [Customer/Admin]: ")

if user.lower() == "customer" or user.lower() == "c":
    import customer
elif user.lower() == "admin" or user.lower() == "a":
    import admin
else:
    print("User not defined")
```

### error_corrector.py

```py
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


```
