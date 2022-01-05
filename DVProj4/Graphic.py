import matplotlib.pyplot as plot

userInput = ""
x = [10,20,30,40,50,60,70,80,90,100]
y = [10,78,32.66,45,20,10,54,23,34,0]

u = [10,20,30,40,50,60,70,80,90,100]
v = [99,34,56,23,67,34,46,86,0,99]

def setInputLable(quary):
    global userInput
    userInput = quary
    print(userInput)

def drawBasicGraph(xList,yList, xLable, yLable , title):
    plot.plot(xList, yList, color="red")
    plot.title(title)
    plot.xlabel(xLable)
    plot.ylabel(yLable)
    avg = 0;
    for i in yList:
        avg = avg + i
    avg = avg / len(yList)
    avgs = []
    for i in yList:
        avgs.append(avg)
    plot.plot(xList, avgs, color = "red", linestyle = "dotted")
    plot.gca().legend(("Elon Musk", "Elon's Average"))  # loc="upper left")
    plot.show()

def compareBasicGraphs(xList0,yList0, xLable, yLable, title,xList1,yList1):
    plot.plot(xList0, yList0, color="red")#, lable="elonMusk")
    plot.title(title)
    plot.xlabel(xLable)
    plot.ylabel(yLable)
    avg = 0;
    for i in yList0:
        avg = avg + i
    avg = avg / len(yList0)
    avgs = []
    for i in yList0:
        avgs.append(avg)
    plot.plot(xList0, avgs, color = "red", linestyle = "dotted")#, lable="elonMusk avg")

    plot.plot(xList1, yList1, color="blue")#, lable=userInputLable)
    avg = 0;
    for i in yList1:
        avg = avg + i
    avg = avg / len(yList1)
    avgs = []
    for i in yList1:
        avgs.append(avg)
    plot.plot(xList1, avgs, color = "blue", linestyle = "dotted")#, lable = userInputLable + " avg")

    plot.gca().legend(("Elon Musk","Elon's Average",userInput,userInput + "'s Average"))#loc="upper left")
    plot.show()




#drawBasicGraph(x,y,"x","y","simple graph")
#compareBasicGraphs(x,y,"x","y","simple graph",u,v)