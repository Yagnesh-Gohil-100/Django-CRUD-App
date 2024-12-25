# pip install mysql-connector (it did not work)
# pip install mysql-connector-python (it worked for me)

# (If 1st one doesn't work then use 2nd)

# http://127.0.0.1:8000/  surver runs on this

import mysql.connector

dataBase = mysql.connector.connect(
  host = 'localhost',
  user = 'root',
  passwd = 'pwd'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

# create a database
cursorObject.execute("CREATE DATABASE mydatabase")

print("database created")

