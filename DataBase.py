# Alec Knobloch
# Project DataMiner- Bitcoin
# Date 6/6/2021
import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np


def readCSV(file):

    with open(file, newline='') as myFile:  # get first line of data to with titles of columns
        lines = csv.reader(myFile, delimiter=',')
        count = 0
        for line1 in lines: # this could be more efficient
            if count < 1:
                temp = line1
                count = count + 1
    COLUMN1 = temp[0]
    COLUMN2 = temp[1]

    print(COLUMN1)
    print(COLUMN2)

    cur.execute('CREATE TABLE IF NOT EXISTS Data (' + COLUMN1 + ' TEXT)')
    cur.execute('ALTER TABLE Data ADD COLUMN ' + COLUMN2 + ' INTEGER') #Add new column to table

    with open(file, newline='') as myFile2:

        lines1 = csv.DictReader(myFile2)

        for line in lines1:
            #determine if for each date that date has a corresponding value in COLUMN2
            cur.execute(
                'SELECT ' + COLUMN1 + ' FROM Data WHERE ' + COLUMN1 + " == '" + line[COLUMN1].split(" ")[0] + "'")
            test = cur.fetchone()

            if test != None:
                #if the date existes but there is no value set value for corresponding date
                if test[0] == line[COLUMN1].split(" ")[0]:
                    cur.execute("UPDATE Data SET " + COLUMN2 + " = " + line[COLUMN2] + " WHERE " + COLUMN1 + " == '" +
                                line[COLUMN1].split(" ")[0] + "'")
            else:
                #if there is no date found for a value add said new date and value to table
                cur.execute('INSERT INTO Data (' + COLUMN1 + ', ' + COLUMN2 + ') VALUES (?, ?)',
                            (line[COLUMN1].split(" ")[0], line[COLUMN2]))

    conn.commit()


# ---------------------------------------------------------------------

"""
This function removes any rows in the data set that do not have a full set of value in every column
Therefore, removes all holes in data
"""
def cleanData():
    cur.execute('SELECT * FROM Data')
    table = cur.fetchall()

    for rows in table:
        for each in rows:

            if (each == None):
                cur.execute("DELETE FROM Data WHERE ï»¿Timestamp == '" + rows[0] + "'")
                break
    conn.commit()


###---------------------------------------------------------------
# this function could be reduced if not totally scapted with sql plotting straight to matplotlib
def newplot(xAxis, yAxis):
    print(xAxis)
    print(yAxis)

    cur.execute("SELECT " + xAxis + "," + yAxis + " FROM Data")
    charting = cur.fetchall()
    x = []
    y = []
    print("got here")

    for rows in charting:
        x.append(rows[0])
        y.append(rows[1])

    global fig
    fig = fig + 1
    print(fig)
    plt.figure(fig)

    plt.scatter(x, y)
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.title(xAxis + " vs " + yAxis)
    plt.draw()


###--------------------------------------------------------------


def LinearRegession(xAxis, yAxis):
    print(xAxis)
    print(yAxis)

    cur.execute("SELECT " + xAxis + "," + yAxis + " FROM Data")
    charting = cur.fetchall()
    x = []
    y = []

    print("got here4")

    for rows in charting:
        x.append(rows[0])
        y.append(rows[1])

    z = np.vstack([x, np.ones(len(x))]).T
    m, c = np.linalg.lstsq(z, y, rcond=None)[0]

    A = [element * m + c for element in x]
    print(m, c)

    global fig
    fig = fig + 1
    print(fig)
    plt.figure(fig)

    plt.scatter(x, y)
    plt.xlabel(xAxis)
    plt.ylabel(yAxis)
    plt.title(xAxis + " vs " + yAxis)
    plt.plot(x, A, 'r', label='Fitted line')
    plt.draw()


###==============================================================================================================================


# 'ï»¿Timestamp'
print("hello world")
fig = 0

conn = sqlite3.connect('DataBase.sqlite')
cur = conn.cursor()
# 'DROP TABLE'  command deletes the table and all of its contents from the database
cur.execute('DROP TABLE IF EXISTS Data')

#readCSV('difficulty')
readCSV('marketPrice')
readCSV('MinersRevenue')
readCSV('hashRate')
readCSV('difficulty30DayAvg')

cleanData()

# newplot('hashRate', 'difficulty30DayAvg')

newplot('ï»¿Timestamp', 'hashRate')
newplot('ï»¿Timestamp', 'Market_Price')
newplot('Market_Price', 'Miners_Revenue')

LinearRegession('Market_Price', 'Miners_Revenue')
LinearRegession('hashRate', 'difficulty30DayAvg')
LinearRegession('Market_Price', 'hashRate')

plt.show()
cur.execute('SELECT * FROM Data')
table = cur.fetchall()

"""
for rows in table:
    print(rows)
"""
conn.close()

###
