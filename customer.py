import mysql.connector
from boxprint import box

conn = mysql.connector.connect(host="localhost", port="3305",user="root", passwd="password")

box(["Welcome Customer"], width=20)