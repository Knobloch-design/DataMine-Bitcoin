
from DataBase import Table
import sqlite3
import csv
import matplotlib.pyplot as plt
import numpy as np


"""
This class's job is to display the data from the data tables set up in the database class
"""


class Graph(Table):
    fig = 0
    # default constructor
    def show(self):
        plt.show()
    ###---------------------------------------------------------------
    # this function could be reduced if not totally scapted with sql plotting straight to matplotlib
    def newplot(self,xAxis, yAxis):
        print(xAxis)
        print(yAxis)

        Table.cur.execute("SELECT " + xAxis + "," + yAxis + " FROM Data")
        charting = Table.cur.fetchall()
        x = []
        y = []


        for rows in charting:
            x.append(rows[0])
            y.append(rows[1])


        self.fig = self.fig + 1
        print(self.fig)
        plt.figure(self.fig)

        plt.scatter(x, y)
        plt.xlabel(xAxis)
        plt.ylabel(yAxis)
        plt.title(xAxis + " vs " + yAxis)
        plt.draw()


    ###--------------------------------------------------------------

    def LinearRegession(self, xAxis, yAxis):
        print(xAxis)
        print(yAxis)

        Table.cur.execute("SELECT " + xAxis + "," + yAxis + " FROM Data")
        charting = Table.cur.fetchall()
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


    ###---------------------------------------------------------------

