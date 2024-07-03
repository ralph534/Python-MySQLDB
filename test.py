import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="12345678",
    database="testdb"
)


mycursor = mydb.cursor()



# mycursor.execute("SHOW DATABASES")  ## Show the database created

# mycursor.execute("SHOW TABLES")   ## Show the table created



# sqlFormula = "INSERT INTO students (name, age) VALUES (%s, %s)"
# students = [("Smith", 22),
#             ("Bill", 31),
#             ("Chance", 22),
#             ("Jessica", 26),
#             ("Nicole", 33)]
# mycursor.execute(sqlFormula, student1)        ## Execute for line of data
# mycursor.executemany(sqlFormula, students)
# mycursor.execute("SELECT * FROM students")       #execute all students from DB through Python
# sql = "SELECT * FROM students WHERE age=26"     #SELECT a specifc query which holds a specific value
sql = "SELECT * FROM students WHERE name LIKE 'Je%'"   ## Wildcard
mycursor.execute(sql)
myResults = mycursor.fetchall()

# mycursor.execute("SELECT age FROM students")     #SELECTs all students age from DB through Python
# myResults = mycursor.fetchall()
# myResults = mycursor.fetchone()    ## Fetchs a single row in the database
for result in myResults:              ## Loop through each row
    print(result)
# mydb.commit()          ## commit change in database when using the INSERT query

