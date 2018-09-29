import sqlite3

connection = sqlite3.connect("jeopardydb")
cursor = connection.cursor()

cursor.execute("select text, answer, value from clue limit 10")
results =  cursor.fetchall()
for clue in results:
    #text =  clue[0]
    #answer = clue[1]
    #value = clue [2]
    text,answer,value = clue
    print ("[$%s]" % (value,))
    print ("The Question is %s" % (text,))
    print ("The Answer is %s" % answer)
connection.close()
