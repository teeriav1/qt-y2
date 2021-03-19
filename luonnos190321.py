# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:41:33 2021


"""
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *






class Example(QWidget):

    #This is used as a "Welcome-screen"

    def __init__(self):

        #The role is meant to control interface
        #Focuses on use of PyQt
        super().__init__()
        self.state = 0
        self.setWindowTitle("Welcome")
        self.setGeometry(50, 50, 400, 400)
        self.show()
        hbox = QVBoxLayout()

        #This is where you create buttons
        if self.state == 0:
            self.label1=QLabel("Press button")
            self.label1.setFont(QFont('Arial', 10))

            hbox.addWidget(self.label1)
            self.button1 = QPushButton("Push", self)
            self.button1.setCheckable(True)
            hbox.addWidget(self.button1)
            self.setLayout(hbox)
            self.show()
            self.button1.clicked.connect(self.buttompressed)
            self.button1.clicked.connect(self.button1.hide)
            self.button1.clicked.connect(self.gostate1)
            hbox.addStretch(1)

        #Too much clicking, added this. This remove welcome screen
        self.button1.hide()
        self.gostate1()
    def onChanged(self, text):
        #onChaned is meant to update name of the file stats-object so data keeps up with interface

        stats.filename = text
    def gostate1(self):

        #Gostate1 is meant to switch from Welcome-screen to "Ask for a file screen"
        self.state = 1
        self.setGeometry(50, 50, 400, 400)
        hbox = QVBoxLayout()

        self.label1.setText("Write the name of the file you want to use.\nIf no name is given, an example file will be used")
        self.label1.move(150,100)

        self.setWindowTitle('Find file -phase')
        self.button2 = QPushButton("Jotain", self)

        self.button2.setCheckable(True)
        self.qLineEdit = QLineEdit(self)
        self.qLineEdit.move(150, 100)

        self.button2.move(150, 200)
        self.qLineEdit.textChanged[str].connect(self.onChanged)
        self.qLineEdit.textChanged[str].connect(self.qLineEdit.adjustSize)

        self.qLineEdit.show()
        hbox.addWidget(self.qLineEdit)
        hbox.addWidget(self.button1)
        self.button2.show()

        self.show()
        hbox.addStretch(1)
        self.setLayout(hbox)
        self.button2.clicked.connect(self.clickedToRun)
        #self.button2.clicked.connect(self.qLineEdit.textChanged[str])
        self.button2.clicked.connect(self.isfilefound)




    def isfilefound(self):

        #isfilefound is meant to check whether there is a real file found that can be used

        #If file cannot be used for whatever reason, it will tell you
        if stats.filenotfound == False:
            self.button2.clicked.connect(self.qLineEdit.hide)
            self.button2.clicked.connect(self.button2.hide)
            self.button2.clicked.connect(self.label1.hide)
            self.gostate2()
        else:
            self.label1.setText(
                "Write the name of the file you want to use.\nIf no name is given, an example file will be used\n\nThere was an error finding the file")

    def gostate2(self):

        #Gostate2 happens when you have a file that can be used and you continue to seeing info about the file
        #Gostate2 is supposed to have multiple ways to go forward
        if len(stats.uppersave) > 0:
            self.qLineEdit.hide()
            self.button2.hide()
            self.label1.hide()
            processlist = []
            allTotal = 0
            for keyword in stats.uppersave:

                sumOfOne = 0
                for alkio in stats.uppersave[keyword]:
                    sumOfOne -= alkio
                allTotal += sumOfOne

                processlist.append(str(keyword) + ":" + str(sumOfOne)+":")
            processlist.append("All Total:"+str(allTotal)+":")

            #Now this shows the info of payment usages
            text = ""
            for x in processlist:
                splittedX = x.split(":")
                percent = float(splittedX[1]) / allTotal * 100
                text += "\n" + x +str(round(percent,2))
            self.label1.show()
            self.label1.setText(text)


    def clickedToRun(self):

        #There are multiple other options than the main function
        #This runs the main function as in regular meaning of main, not python-code function called main
        run()


    def btnstate(self, state):

        #This is how to do stuff when you click on buttons in PyQt
        if state == Qt.Checked:
            self.setWindowTitle('Checked')
            print(self.objectName)
            self.button2.setCheckable(False)
            self.button2.setCheckable(True)
        else:
            self.setWindowTitle("Unchecked")


    def keyPressEvent(self, e):

        #This is what happens when you press a key
        #The first one closes window if you press esc. I dont know if I want to keep this but it seems ok for now
        if e.key() == Qt.Key_Escape:
            self.close()
    def buttompressed(self):
        #print("Tapahtuu painaessa")
        #Me learning PyQt
        pass







class Stats():
    def __init__(self):
        #Stats-object is the place to save info. It is used in between interface and engine
        self.id = 0
        self.lowerlist = {}
        self.upperlist = {}
        self.keywordlist = {"Teknologforeningen":"Ruokailu","Compass Gr":"Ruokailu","Ylva palve":"Ruokailu","Prisma":"Kaupat","HOAS":"Asuminen","Alepa":"Kaupat","MOB.PAY":"TILISIIRROT","TILISIIRTO":"TILISIIRROT","Tokmanni":"Kaupat","Steam":"Viihde","Market":"Kaupat","Clas Ohlson":"Kaupat","Luckiefun":"Viihde","Pallohalli":"Urheilu","Lidl":"Kaupat","R ":"Kaupat","Sanoma":"Viihde","Farmasialiitto":"Muu","Amarillo":"Viihde","Pizze":"Viihde"}
        self.defined = []
        self.filename = ""
        self.filenotfound = False
        self.lowersave = {}
        self.uppersave = {}
    def reset(self):

        #Reset is used to reset info of stats. One can run "run()", that is the main function of the engine, multiple times
        #And reset() cleans stats in between

        #This is not the great reset you've heard about
        if len(self.lowerlist) > 0:
            self.lowersave = self.lowerlist
            self.uppersave = self.upperlist
        self.lowerlist = {}
        self.upperlist = {}
        self.defined = []
        self.filename = ""
        self.filenotfound = False
    def filenotfound(self):

        #Im lost with these formats, if not used, delete
        return self.filenotfound
    def alltotal(self):

        #When this is used, program in run in console
        #Fix
        alltotal = 0
        for keyword in stats.upperlist:
            print(keyword, " ", end="")
            summa = 0
            for luku in stats.upperlist[keyword]:
                summa += luku
            print(summa * -1)
            alltotal += summa
        return alltotal

stats = Stats()
def openfile(name):
    
    #This opens file and does handleline-function to all lines except the one with names
    #path = r"C:\Users\Weke\Documents\Pyton\Y2\projekti\tapahtumat20210101-20210218.csv"
    if name == "":
        path = r"tapahtumat20210101-20210218.csv"
    else:
        path = name
    try:
        with open(path) as file:
            stats.filenotfound = False
            for i,x in enumerate( file):
                if i == 0:
                    pass
                else:
                    handleline(x)
    except FileNotFoundError:
        stats.filenotfound = True

    #Allow only one of these. They do the same thing

    addinfotostatsUPPER()
    #sortwithinputs()
def handleline(line):
    
    #handleline is used to convert csv-files info into form easily used
    line = str(line)
    lineparts = line.split(";")
    date = lineparts[0]
    price = lineparts[2]
    price = str(price)

    price = price.replace(",", ".")
    price = price.replace('"', '')
    paymenttype = lineparts[4]
    receiver = lineparts[5]     
    receiver = str(receiver)
    receiver = receiver.lstrip('"')
    receiver = receiver.rstrip('"')


    price = float(price)    
    price = price * 100
    price = int(price)
    if price < 0:

        #print(date, price, receiver, paymenttype)     
        
        addinfotostatsLOWER(receiver,price,paymenttype)
def addinfotostatsLOWER(receiver,price,paymenttype):

    
    #This function saves the info from file used
    
    #First we add in to lowerlist
    if "TILISIIRTO" in paymenttype:
        receiver = "TILISIIRTO:" + receiver
    if receiver in stats.lowerlist:
        stats.lowerlist[receiver] += price
    else:
        stats.lowerlist[receiver] = price
def addinfotostatsUPPER():

    #There are 2 functions that add info to upperlist. This one is automatic, based on hardcoded list
    for oppressor in stats.lowerlist:
        if oppressor in stats.defined:
            pass
        else:
            for keyword in stats.keywordlist:
                if keyword.upper() in oppressor.upper():
                    addthistoUpper(oppressor, stats.keywordlist[keyword])
                    break
def sortwithinputs():

    #This is the second function adding info to upperlsit. This one asks for user input and uses those
    while True:
        if len(stats.defined) == len(stats.lowerlist):
            break
        else:
            for oppressor in stats.lowerlist:
                if oppressor in stats.defined:
                    pass
                else:
                    print("This one is not defined. Define: ", oppressor)
                    usercommand = str(input(""))
                    addthistoUpper(oppressor, usercommand)
def addthistoUpper(oppressor, uppergroub):
    #This adds ONE LINE to upperlist.
    #This is made clear up the code

    if uppergroub in stats.upperlist:
        stats.upperlist[uppergroub].append(stats.lowerlist[oppressor])
    else:
        stats.upperlist[uppergroub] = [stats.lowerlist[oppressor]]
    stats.defined.append(oppressor)   
def searchUndefined():
    #So there are lines that dont really fit anything. At least if it's not my file.
    #THis is used to search for those
    palautuslista = []
    for oppressor in stats.lowerlist:
        if oppressor in stats.defined:
            pass
        else:
            palautuslista.append(oppressor)
    return palautuslista
def clean():
    #This worked in older python. Im sad it dont work anymore and I've not found a fix.
    print('cls')
    print("\033[H\033[J")
def run():

    #This is the main function of engine
    nameForFile = stats.filename
    openfile(nameForFile)
    for oppressor in stats.lowerlist:
        #print(oppressor, stats.lowerlist[oppressor])
        pass




    alltotal = 0

    for keyword in stats.upperlist:
        summa = 0
        for luku in stats.upperlist[keyword]:
            summa += luku
        alltotal += summa


    """
    #This line enables the use in console. It is saved for debug usage
    print("All total ", stats.alltotal())
    """
    if len(searchUndefined()) > 0:
        print("\n\nNow this print those not defined:")
        for undefined in searchUndefined():
            print(undefined)

    if len(stats.upperlist) > 0:
        stats.reset()

def main():


    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


main()