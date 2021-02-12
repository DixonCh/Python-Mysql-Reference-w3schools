'''
Python MySQL Limit:

Limit the Result:

You can limit the number of records returned from the query, by using the "LIMIT" statement:

Example:

Select the 5 first records in the "customers" table:
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5")

myresult = mycursor.fetchall()

for x in myresult:
  
  print(x)
 
'''
Start From Another Position:

If you want to return five records, starting from the third record, you can use the "OFFSET" keyword:

Example:

Start from position 3, and return 5 records:
'''
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  passwd="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)
