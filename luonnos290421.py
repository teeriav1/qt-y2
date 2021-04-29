# -*- coding: utf-8 -*-

#C:\Users\Weke\Downloads\tapahtumat20210101-20210411.csv
import sys
import time
import math
import random
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
shortcut = False
debug = False


class Example(QWidget):

    def __init__(self):
        if debug:
            print("There is object called 'debug' that has value of True. This will cause program to print\na lot of stuff in console")
        #The role is meant to control interface
        #Focuses on use of PyQt
        super().__init__()
        self.state = 0
        self.setWindowTitle("Welcome")
        self.setGeometry(50, 50, 400, 400)
        self.hbox = QVBoxLayout()
        self.new_keyword = ""
        self.groupnames = []
        self.groupnominals = []
        self.grouppercents = []
        self.scene = QGraphicsScene()
        self.colors = []
        self.view = QGraphicsView(self.scene)
        self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.view.setStyleSheet("border: 0px")
        self.qLineEdit = QLineEdit(self)
        self.qLineEdit3 = QLineEdit(self)
        self.textEdit = QTextEdit()
        self.hbox.addWidget(self.textEdit)
        self.textEdit.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.textEdit.hide()
        self.show()


        #This is where you create buttons
        if self.state == 0:
            self.label1=QLabel("Press button")
            self.label2=QLabel()
            self.label1.setFont(QFont('Arial', 10))
            self.label2.setFont(QFont('Arial', 10))

            self.hbox.addWidget(self.view)
            self.hbox.addWidget(self.label1)
            self.hbox.addWidget(self.label2)
            self.label2.setAlignment(Qt.AlignRight)
            self.button1 = QPushButton("Push", self)
            self.button1.setCheckable(True)
            self.button2 = QPushButton("Jotain", self)
            self.button3 = QPushButton("Manual adding", self)
            self.button3.setCheckable(True)
            self.button3.setFixedWidth(100)
            self.button3.setFixedHeight(30)


            self.hbox.addWidget(self.button1)
            self.setLayout(self.hbox)
            self.show()

            self.button1.clicked.connect(self.button1.hide)
            self.button1.clicked.connect(self.gostate1)
            self.hbox.addStretch(1)

        #Too much clicking, added this. This remove welcome screen

        self.button1.hide()
        self.button3.hide()
        self.qLineEdit2 = QLineEdit(self)
        self.qLineEdit2.hide()
        self.gostate1()
    def window_reset(self):
        self.setGeometry(50, 50, 401, 401)
        self.setGeometry(50, 50, 400, 400)


    def onChanged(self, text):

        #onChanged is meant to update name of the file stats-object so data keeps up with interface
        #This changed behavior based on self.state and uses info of qLineEdit
        if text == "":
            pass
        elif self.state == 1:
            stats.filename = text
        elif self.state == "go_sorting_stage":
            self.new_keyword = text
        else:
            pass


    def gostate1(self):
        self.hideall()
        if debug:
            print("gostate1")
        #Gostate1 is meant to switch from Welcome-screen to "Ask for a file screen"
        self.state = 1

        self.hbox = QVBoxLayout()

        self.label1.setText("Write the name of the file you want to use.\nIf no name is given, an example file will be used")
        self.label1.move(150,50)
        self.label1.show()

        self.setWindowTitle('Find file -phase')

        self.button2.setCheckable(True)
        self.button2.move(150, 200)

        self.qLineEdit.move(150, 150)
        self.qLineEdit.textChanged[str].connect(self.onChanged)
        self.qLineEdit.textChanged[str].connect(self.qLineEdit.adjustSize)
        self.qLineEdit.show()
        self.qLineEdit2.move(150, 150)
        self.qLineEdit2.textChanged[str].connect(self.onChanged)

        self.hbox.addWidget(self.qLineEdit)
        self.hbox.addWidget(self.button1)

        self.button2.setText("RUN")
        self.button2.show()

        self.show()
        #self.hbox.addStretch(1)
        self.button2.clicked.connect(self.isfilefound)

        if shortcut:
            self.button2.click()

        #bugfixing


    def isfilefound(self):
        if debug:
            print("isfilefound")
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
    def hideall(self):
        self.window_reset()
        if debug:
            print("hideall")
        self.view.hide()
        self.button1.hide()
        self.button1 = QPushButton("", self)
        self.button1.hide()
        self.button2.hide()
        self.button3.hide()
        self.qLineEdit2.hide()
        self.label1.hide()
        self.textEdit.hide()
        self.label2.hide()
        self.qLineEdit3.hide()
        self.button1.click()
    def gostate3(self):
        self.state = 3
        if debug:
            print("gostate3")
            for group in stats.lowersave:
                print(group, stats.lowersave[group])
        #This state is state of automatic sorting and continue to info printing
        self.hideall()
        self.clickedToRun()


        #This state happens when you have a file that can be used and you continue to seeing info about the file
        #This is supposed to have multiple ways to go forward
        if len(stats.uppersave) > 0:
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
        #This should also show info about non defined transactions
        #And have a route to continue
        if debug:
            print(stats.undefined)
        if len(stats.undefined) > 0:
            self.go_sorting_stage()
    def autosort(self):
        if debug:
            print("autosort")
        addinfotostatsUPPER()
    def gostate2(self):
        self.state = 2
        if debug:
            print("gostate2")
        self.qLineEdit.hide()
        self.hideall()
        self.setWindowTitle('Decide how to sort')

        #This state 3 is to sort how stuff should be defined
        #This will decide whether to auto-sort
        self.label1.setText("There is inbuild autosort\nDo you want to use it?")

        self.label1.show()
        self.button1 = QPushButton("Yes", self)
        self.button2 = QPushButton("No", self)

        self.button1.move(25,60)
        self.button1.show()

        self.button2.move(150,60)
        self.button2.show()
        self.button1.clicked.connect(self.gostate3)
        self.button2.clicked.connect(self.go_manual_sorting_start)
        if shortcut:
            self.button1.click()
    def go_manual_sorting_start(self):
        if debug:
            print("go_manual_sorting_start")
        self.state = "manual_sorting"
        #Sort of with manual labor
        stats.keywordlist = {}
        self.gostate3()

    def go_sorting_stage(self):
        self.qLineEdit.hide()
        self.state = "go_sorting_stage"
        if debug:
            print(self.state)
        self.hideall()
        #First we create the window we see

        self.setWindowTitle("Sorting stage")
        text = "There are lines to be sorted: " + str(len(stats.undefined))
        if len(stats.undefined) == 0:
            self.go_showinfo_phase()
        else:
            if debug:
                print(len(stats.undefined))
            text += "\n"+str(stats.undefined[0])+"\nPlease enter a group to sort these into"
        self.label1.setText(text)
        self.label1.show()
        text2 = "There are already groups called:\n"
        for x in stats.uppersave:
            text2 += str(x) + "\n"

        self.label2.setText(text2)
        self.label2.move(290,50)
        self.label2.show()

        self.button1.setText("Enter")
        self.button1.move(50,160)
        self.button1.show()

        #Then we create the functionality
        #Functionality 1: Adds suitable keywords and reruns the process here
        #We need a place to save info from field(QLineEdit) and then add it to keywords
        #It is called self.new_keyword

        #Then button 1 functionality
        self.button1.clicked.connect(self.add_keyword_and_rerun)
        self.qLineEdit2.show()

        self.qLineEdit2.move(50,120)
        self.qLineEdit2.textChanged[str].connect(self.onChanged)

        self.hbox.addWidget(self.button1)

    def add_keyword_and_rerun(self):
        if debug:
            print("add_keyword_and_rerun")
            print(self.new_keyword)
        if self.new_keyword == "":
            pass
        else:
            stats.keywordlist[str(stats.undefined[0])] = self.new_keyword
            if debug:
                print(stats.keywordlist)
            self.clickedToRun()
            if len(stats.undefined) > 0:
                self.go_sorting_stage()
            else:
                self.qLineEdit.hide()
                self.go_showinfo_phase()
        pass
    def infowindow_reset(self):
        #Info is in stats.uppersave
        #This calculates values
        if debug:
            print("go_showinfo_phase: Calculating numbers")
        totalsum = 0
        self.groupnames = []
        self.groupnominals = []
        self.grouppercents = []
        for group in stats.uppersave:
            self.groupnames.append(group)
            nominal = 0
            for number in stats.uppersave[group]:
                nominal += number
            self.groupnominals.append(nominal)
            totalsum += nominal

        for i in range(len(self.groupnominals)):
            self.grouppercents.append(float(self.groupnominals[i] / totalsum)*100)

        self.text = ""
        totaltoShow = float(0)
        for i in range(len(self.groupnames)):
            numberToUse = self.grouppercents[i]
            #numberToUse = self.groupnominals[i]
            self.text += str("{:22s} {:.2f}€  {:.2f}\n".format(self.groupnames[i],self.groupnominals[i] * -0.01, self.grouppercents[i]))
            totaltoShow += numberToUse



        nominalTotal = -totalsum / 100
        self.text += str("{:22s}{:.2f}\n".format("Total", nominalTotal))
    def go_showinfo_phase(self):
        if debug:
            print("go_showinfo")
        # self.infowindow_reset should be run, when info shown in the window changes
        # If not, then not run
        list_of_reset_stages = ["go_sorting_stage", "manual_sorting", 2]
        if self.state in list_of_reset_stages:
            self.infowindow_reset()
        if debug:
            print("Amount of groupnames: ",len(self.groupnames))

        #colors have to be made once
        self.changeColor_infowindow()
        self.state = "info"

        self.hideall()
        self.setWindowTitle("Statistics")

        # First show info as plain text

        self.label1.setText(self.text)
        self.label1.show()

        #Now this will draw some shit
        if debug:
            print("go_showinfo_phase: Draw something")


        if debug:
            print("Get colors: changeColor_infowindow()")

        #And we shall make options to click in the window
        #insert buttom for recolor
        self.button1.clicked.connect(self.changeColor_infowindow)
        self.button1.setText("Color change")
        self.button1.move(30, 325)
        self.button1.show()

        #insert buttom to restart
        self.button2.clicked.connect(self.restarting)
        self.button2.setText("Restart ?")
        self.button2.move(150,325)
        self.button2.show()

        #insert buttom to saving-program
        self.button3.clicked.connect(self.manual_adding_of_lines)
        self.button3.setText("Manual adding")
        self.button3.move(270,325)
        self.button3.show()

    def restarting(self):
        self.window_reset()
        stats.__init__()
        stats.keywordlist = stats.keywordlistsave
        self.gostate1()

    def manual_adding_of_lines(self):
        # This needs 2 fields of info: Place where money is spent and the amount
        # Then it should add info and go to sorting state without f up
        self.setWindowTitle("Manual adding of Lines")
        qlineX = 35
        self.state = "Manual_line_adding"
        if debug:
            print(self.state)
        self.hideall()
        text = "1: Write the name of the place where money was spent:\n"
        text += "2: Insert the amount of money spent. Do not use , or ., but insert the amount in cents"
        text += "\n\n\n1:\n\n\n2:"

        self.label1.setText(text)
        self.label1.show()
        self.qLineEdit.move(qlineX,75)
        self.qLineEdit.show()

        self.qLineEdit3.move(qlineX,120)
        self.qLineEdit3.show()
        buttomY = 175
        self.button1.move(25, buttomY)
        self.button1.setText("Add info")
        self.button1.clicked.connect(self.manual_adding_of_lines_add_a_line)
        self.button2.move(150, buttomY)
        self.button2.setText("Calcel")
        self.button2.clicked.connect(self.go_showinfo_phase)
        self.button1.show()
        self.button2.show()
    def manual_adding_of_lines_add_a_line(self):
        oppressor = self.qLineEdit.text()
        amount = self.qLineEdit3.text()
        if debug:
            print("1,2", oppressor,amount)
        print(len(stats.lowersave))
        amount = str(amount).strip(" ")
        amount = int(amount)
        amount = -1 * amount
        try:
            stats.lowerlist[oppressor] += amount
        except KeyError:
            stats.lowerlist[oppressor] = amount
            stats.undefined.append(oppressor)

        self.go_sorting_stage()





        # insert apply button
        # implement me!

    def apply_changed_info_from_line_edit(self):
        pass

    def changeColor_infowindow(self):
        #We need colors to differentiate chart pieces from each other
        #This can both create new or overwrite old
        self.colors = []
        colorsneeded = len(stats.uppersave)
        if len(self.groupnames) > colorsneeded:
            colorsneeded = len(self.groupnames)

        for i in range((colorsneeded)+1):
            number = []
            for count in range(3):
                number.append(random.randrange(0, 255))
            self.colors.append(QColor(number[0], number[1], number[2]))
        if debug:
            print("Self.colors LEN: ", len(self.colors))

    def paintEvent(self, event):

        #So far this only shows nice pictures when in info-state

        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        painter.drawRect(0, 0, self.width(), self.height())
        if self.state == "info":

                #And now we try to paint pie chart
                angle_start = 0
                for i, x in enumerate(self.groupnames):
                    # Based on max span 5760, internet said so
                    #This is to create slices of pie
                    angle_end = round(float(57.6 * float(self.grouppercents[i]) ))
                    if debug:
                        pass
                    ellipse = QGraphicsEllipseItem(0, 0, 200, 200)
                    ellipse.setStartAngle(angle_start)
                    ellipse.setSpanAngle(angle_end)
                    try:
                        ellipse.setBrush(self.colors[i])
                    except IndexError:
                        pass
                    angle_start += angle_end
                    self.scene.addItem(ellipse)
                    #something so that user can see which color is which group
                    try:
                        painter.setBrush(QBrush(self.colors[i], Qt.SolidPattern))
                    except IndexError:
                        pass
                    painter.drawEllipse(10, 80+i*16, 10, 10)

                self.view.move(100,100)
                self.label1.move(25,75)
                self.view.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
                self.view.setSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
                self.view.setStyleSheet("background-color: gray;")
                self.view.show()

    def clickedToRun(self):
        if debug:
            print("clickedToRun")
            print(stats.filename,stats.filesave)

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
        # Enter pressed makes "an ok" or forwards to new stage or something like that
        # implement me!

class Stats():
    def __init__(self):
        #Stats-object is the place to save info. It is used in between interface and engine
        self.id = 0
        self.lowerlist = {}
        self.upperlist = {}
        self.keywordlist = {"Compass Group":"Ruokailu","Ylva palve":"Ruokailu","Prisma":"Kaupat","HOAS":"Asuminen","Alepa":"Kaupat","Tokmanni":"Kaupat","Steam":"Viihde","Market":"Kaupat","Clas Ohlson":"Kaupat","Luckiefun":"Viihde","Pallohalli":"Urheilu","Lidl":"Kaupat","R ":"Kaupat","Sanoma":"Viihde","Farmasialiitto":"Muu","Amarillo":"Viihde","Pizze":"Viihde"}
        self.keywordlistsave = {"Compass Group":"Ruokailu","Ylva palve":"Ruokailu","Prisma":"Kaupat","HOAS":"Asuminen","Alepa":"Kaupat","Tokmanni":"Kaupat","Steam":"Viihde","Market":"Kaupat","Clas Ohlson":"Kaupat","Luckiefun":"Viihde","Pallohalli":"Urheilu","Lidl":"Kaupat","R ":"Kaupat","Sanoma":"Viihde","Farmasialiitto":"Muu","Amarillo":"Viihde","Pizze":"Viihde"}
        self.defined = []
        self.definedsave = []
        self.filename = ""
        self.filesave = ""
        self.filenotfound = False
        self.lowersave = {}
        self.uppersave = {}
        self.automatic = True
        self.lines = []
        self.undefined = []
    def reset(self):

        #Reset is used to reset info of stats. One can run "run()", that is the main function of the engine, multiple times
        #And reset() cleans stats in between

        #This is not the great reset you've heard about
        if len(self.lowerlist) > 0:
            self.lowersave = self.lowerlist
            self.uppersave = self.upperlist
            self.definedsave = self.definedsave
            self.filesave = self.filename
        self.lowerlist = {}
        self.upperlist = {}
        self.defined = []

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
    def return_defined(self):
        return self.defined
    def return_upperlist(self):
        return self.upperlist

stats = Stats()
def openfile(name):
    
    #This opens file and does handleline-function to all lines except the one with names
    #path = r"C:\Users\Weke\Documents\Pyton\Y2\projekti\tapahtumat20210101-20210218.csv"
    examplefile = r"tapahtumat20210101-20210218.csv"
    if debug:
        print("openfile filename: ", name)
    # Program says "If no name is entered, example file will be used
    if name == "":
        path = examplefile
    # onChanged-function sometimes leaves a letter when QLineEdit is being emtied. This fixes when you type
    # something and erase it, but program thinks there is still one letter left
    elif len(str(name)) <= 1:
        path = examplefile
    # And of course, one should be able to use other file
    else:
        path = name
    try:
        if debug:
            print(path)
        with open(path) as file:
            stats.filenotfound = False
            for i, x in enumerate( file):
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
            #This is to prevent double adding certain things
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
    #prerequisite : oppressor in stats.lowerlist
    # Upperlist[place to spend money] = [[amount] , [amount]]
    # lowerlist[place to spend money] = [amount]
    # function
    # Upperlist[place to spend money] = [[amount] , [amount], [amount]]


    if uppergroub in stats.upperlist:
        stats.upperlist[uppergroub].append(stats.lowerlist[oppressor])
    else:
        stats.upperlist[uppergroub] = [stats.lowerlist[oppressor]]
    stats.defined.append(oppressor)

def searchUndefined():
    #So there are lines that dont really fit anything. At least if it's not my file.
    #THis is used to search for those
    palautuslista = []

    listused = stats.lowerlist
    definedused = stats.defined
    if len(stats.lowerlist) == 0:
        listused = stats.lowersave
        definedused = stats.definedsave
        print(len(listused), len(definedused))
    for oppressor in listused:
        if oppressor in definedused:
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
    if debug:
        print("All total ", stats.alltotal())

    if len(searchUndefined()) > -1:
        stats.undefined = []
        if debug:
            print("\n\nNow will this print those not defined:")
        for undefined in searchUndefined():
            stats.undefined.append(undefined)
            if debug:
                print(undefined)

    if len(stats.upperlist) > 0:
        stats.reset()


def main():
    """
    app = QApplication(sys.argv)
    sys.exit(app.exec_())
    """

    print("")
main()