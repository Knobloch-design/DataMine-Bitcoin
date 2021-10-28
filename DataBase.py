 # Alec Knobloch
 # Project DataMiner- Bitcoin
 # Date 6/6/2021
import sqlite3
import csv

def readCSV(file):

    COLUMN1 = ''
    COLUMN2 = ''
    with open(file, newline='') as myFile:
        lines=csv.reader(myFile, delimiter = ',')
        count = 0
        for line1 in lines:
            if count  < 1:
                temp  = line1
                count = count + 1
    COLUMN1 = temp[0]
    COLUMN2 = temp[1]

    print(COLUMN1)
    print(COLUMN2)


    cur.execute('CREATE TABLE IF NOT EXISTS Data ('+COLUMN1+' TEXT)')
    cur.execute('ALTER TABLE Data ADD COLUMN '+COLUMN2+' INTEGER')


    with open(file, newline='') as myFile2:

        lines1= csv.DictReader(myFile2)

        for line in lines1:

            cur.execute('SELECT '+COLUMN1+' FROM Data WHERE '+ COLUMN1+ " == '"+line[COLUMN1]+"'")
            realTime = cur.fetchone()

            try:
                realTime = realTime[0]
            except:
                pass

            if(line[COLUMN1] == realTime):
                #cur.execute('SELECT '+COLUMN2+'FROM Data')

                cur.execute("UPDATE Data SET "+COLUMN2+" = "+line[COLUMN2]+" WHERE "+ COLUMN1+ " == '"+line[COLUMN1]+"'")
            else:
                cur.execute('INSERT INTO Data ('+COLUMN1+', '+COLUMN2+') VALUES (?, ?)',(line[COLUMN1],line[COLUMN2]))



    conn.commit()

#'ï»¿Timestamp'
print("hello world")


conn = sqlite3.connect('DataBase.sqlite')
cur = conn.cursor()
# 'DROP TABLE'  command deletes the table and all of its contents from the database
cur.execute('DROP TABLE IF EXISTS Data')
#The second command creates a table named Tracks with a text column named title and an integer column named plays.
readCSV('difficulty')
readCSV('marketPrice')
readCSV('MinersRevenue')
cur.execute('SELECT * FROM Data')
table = cur.fetchall()


for rows in table:
    print(rows)

conn.close()


###
