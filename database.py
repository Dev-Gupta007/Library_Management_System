import os
from dotenv import load_dotenv

load_dotenv()

import mysql.connector

mydb = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

myresult = mycursor.fetchall()

print(myresult)

mycursor.execute("SELECT * FROM Books")

myresult = mycursor.fetchall()

for record in myresult :
    print("Book: " , record[1])
    print("Author: " , record[2])
    print("Available Copies: " , record[5])
    print("-"*50)

Book_title = input("Enter Book Title: ")
Author = input("Enter Book Author: ")

sql = "INSERT INTO Books (title , author , total_copies , available_copies) VALUES (%s,%s,1,1)"
Values = (Book_title , Author)

mycursor.execute(sql , Values)
mydb.commit()

books_inserted = mycursor.rowcount
print(books_inserted , "book inserted successfully!")
