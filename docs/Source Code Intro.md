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
db_create.py
```
`admin.py` and `customer.py` are the different interfaces. `cart.py` is a user defined module used by customer.py for certain functions. `error_corrector.py` is used to make sure all the required modules are installed and that they are working properly before executing the program. `boxprint.py` is a user defined module which is used to display the output neatly in boxes. `sql_handler.py` is used by the python program to communicate with the MySQL database.

`main.py` is where the program starts, it the file that should be executed to start the program.

`db_create.py` is a script to create a sample database for testing