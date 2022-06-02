import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np

class Plots:

    def newplot(xAxis, yAxis):
        conn = sqlite3.connect('DataBase.sqlite')
        cur = conn.cursor()
        print(xAxis)
        print(yAxis)

        cur.execute("SELECT "+xAxis+","+yAxis+" FROM Data")
        charting = cur.fetchall()
        x = []
        y = []
        print("got here")


        for rows in charting:

            x.append(rows[0])
            y.append(rows[1])

        global fig
        fig = fig+1
        print(fig)
        plt.figure(fig)

        plt.scatter(x, y)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.title(xAxis+" vs "+yAxis)
        plt.draw()

    def LinearRegession(xAxis, yAxis):
        conn = sqlite3.connect('DataBase.sqlite')
        cur = conn.cursor()
        print(xAxis)
        print(yAxis)

        cur.execute("SELECT " + xAxis + "," + yAxis + " FROM Data")
        charting = cur.fetchall()
        x = []
        y = []
        z = []
        print("got here4")

        for rows in charting:
            x.append(rows[0])
            y.append(rows[1])
            z.append(np.linalg.lstsq(x, y))

        global fig
        fig = fig + 1
        print(fig)
        plt.figure(fig)

        plt.scatter(x, y)
        plt.plot(x,z)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.title(xAxis + " vs " + yAxis)
        plt.draw()