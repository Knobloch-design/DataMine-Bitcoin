import sqlite3
import csv


print("got here testbase")

conn = sqlite3.connect('DataBase.sqlite')
cursor = conn.cursor()
# 'DROP TABLE'  command deletes the table and all of its contents from the database
cursor.execute('DROP TABLE IF EXISTS testbase')
cursor.execute('CREATE TABLE IF NOT EXISTS testbase (ONE TEXT)')

cursor.execute('ALTER TABLE testbase ADD COLUMN TWO INTEGER')
cursor.execute('ALTER TABLE testbase ADD COLUMN THREE INTEGER')
cursor.execute('INSERT INTO testbase (ONE, TWO, THREE) VALUES (?, ?, ?)',('A', 2, 3))
cursor.execute('INSERT INTO testbase (ONE, TWO, THREE) VALUES (?, ?, ?)',('B', 3, 4))
cursor.execute("UPDATE testbase SET TWO = 100 WHERE ONE == 'A'")
cursor.execute('SELECT TWO FROM testbase WHERE THREE == 4')
test = cursor.fetchone()
print(test)
print(type(test[0]))
result = cursor.fetchall()
cursor.execute("SELECT * FROM testbase")
tabletest = cursor.fetchall()
for rows in tabletest:
    print(rows)

#The second command creates a table named Tracks with a text column named title and an integer column named plays.
