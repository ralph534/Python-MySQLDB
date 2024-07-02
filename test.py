import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="5347978er",
    database="testdb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testdb") ### Created database

# mycursor.execute("SHOW DATABASES")  ## Show the database created

mycursor.execute("SHOW TABLES")

for tb in mycursor:
    print(tb)