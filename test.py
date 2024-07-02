import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456",
    database="testdb"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE testdb") ### Created database

# mycursor.execute("SHOW DATABASES")  ## Show the database created

mycursor.execute("SHOW TABLES")

