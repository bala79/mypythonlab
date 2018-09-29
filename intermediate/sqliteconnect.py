import sqlite3

connection =  sqlite3.connect("jeopardydb")
cursor = connection.cursor()
cursor.execute("SELECT name FROM category LIMIT 10")
results = cursor.fetchall()
print(results[0][0])
connection.close()
