from tkinter import *
from Represent import Graph


class GUI(Graph):

    global root, eq1, eq2



    root = Tk()
    root.title("Bitcoin Model SIM")

    eq1 = Entry(root, width=50)
    eq1.pack()
    eq1.insert(0, "ï»¿Timestamp")#"Enter X Axis"
    eq2 = Entry(root, width=50)
    eq2.pack()
    eq2.insert(0, "Miners_Revenue")#"Enter Y Axis"

    def myCLick():

        xAxis=eq1.get()
        yAxis=eq2.get()
        chart = Graph()
        #chart.model1D('hashRate','CostDollars', 0.0001242528)
        print("got here 1")
        chart.model1D('hashRate', 'CostDollars', 0.00007919796)
        chart.newplot(xAxis,yAxis)
        chart.newplot('ï»¿Timestamp', 'CostDollars')
        chart.show()




    def CLickLinearReg():

        xAxis=eq1.get()
        yAxis=eq2.get()
        chart = Graph()
        chart.LinearRegession(xAxis,yAxis)

    myButton = Button(root, text="Graph Me!", command=myCLick)

    ##myButton = Button(root, text="Graph Me!", command=CLickLinearReg)
    myButton.pack()

    root.mainloop()

