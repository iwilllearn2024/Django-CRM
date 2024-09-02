import mysql.connector

#Prepare a variable
database = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'PEugeot@2024'
)

#Prepare a cursor object
cursorObject = database.cursor()

#Create a database
cursorObject.execute("CREATE DATABASE elderco")

print("Database Created")