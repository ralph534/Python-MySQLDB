import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5347978er"
)
print(mydb)