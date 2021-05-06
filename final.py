# -*- coding: utf-8 -*-

#C:\Users\Weke\Downloads\tapahtumat20210101-20210411.csv
import sys
import random
from functools import partial

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

shortcut = False
debug = False

class Example(QWidget):
    def __init__(self, normal_run):
        if debug:
            print("There is object called 'debug' that has value of True. This will cause program to print\na lot of stuff in console")
        #The role is meant to control interface
        #Focuses on use of PyQt and saves values needed to run interface
        super().__init__()
        self.state = 0
        self.setWindowTitle("Welcome")
        self.setGeometry(50, 50, 400, 500)
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
        self.manually_added_lines = {}
        self.oversaved = []
        self.test_run = normal_run == False
        self.test_counter = 0
        if debug:
            print("Test_run ", self.test_run)



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
            self.button4 = QPushButton("", self)
            self.button4.setCheckable(True)


            self.hbox.addWidget(self.button1)
            self.setLayout(self.hbox)
            self.show()

            self.button1.clicked.connect(self.button1.hide)
            self.button1.clicked.connect(self.gostate1)
            self.hbox.addStretch(1)
        self.hbox = QVBoxLayout()

        self.button1.hide()
        self.button3.hide()
        self.button4.hide()
        self.qLineEdit2 = QLineEdit(self)
        self.qLineEdit2.hide()
        self.gostate1()
    def window_reset(self):

        #There are problems caused by window remaining same size and some object not updating
        self.setGeometry(50, 50, 401, 501)
        self.setGeometry(50, 50, 400, 500)


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
        self.label1.setText("Write the path of the file you want to use.\nIf no name is given, an example file will be used")
        self.label1.move(150,50)
        self.label1.show()

        self.setWindowTitle('Find file -phase')
        self.button2.setCheckable(True)
        self.button2.move(75, 200)

        self.qLineEdit.move(120, 120)
        self.qLineEdit.textChanged[str].connect(self.onChanged)
        self.qLineEdit.textChanged[str].connect(self.qLineEdit.adjustSize)
        self.qLineEdit.setText("")
        self.qLineEdit.show()
        self.qLineEdit2.move(80, 100)
        self.qLineEdit2.textChanged[str].connect(self.onChanged)

        self.hbox.addWidget(self.qLineEdit)
        self.hbox.addWidget(self.button1)
        self.button1.setText("Use example file")
        self.button1.clicked.connect(self.find_file_use_example)
        self.button1.move(225, 200)
        self.button1.show()
        self.button2.setText("RUN")
        self.button2.show()

        self.show()
        self.button2.clicked.connect(self.isfilefound)
        if self.test_run:
            print("test_run")
            self.button1.click()
            self.button2.click()
            if len(self.colors) == 11:
                pass
#                self.close()

    def find_file_use_example(self):
        self.qLineEdit.setText("tapahtumat20210101-20210218.csv")
    def isfilefound(self):
        if debug:
            print("isfilefound")
        stats.filename = str(self.qLineEdit.text())
        #isfilefound is meant to check whether there is a real file found that can be used
        #If file cannot be used for whatever reason, it will tell you
        if debug:
            print("File trying to be found", str(self.qLineEdit.text()))

        if stats.filenotfound == False:
            self.button2.clicked.connect(self.qLineEdit.hide)
            self.button2.clicked.connect(self.button2.hide)
            self.button2.clicked.connect(self.label1.hide)
            self.gostate2()

    def hideall(self):
        # hideall() is used to hide object when switching from one window to another
        self.window_reset()
        if debug:
            print("hideall")
        self.view.hide()
        self.button1.hide()
        self.button1 = QPushButton("", self)
        self.button1.hide()
        self.button4.hide()
        self.button2.hide()
        self.button3.hide()
        self.qLineEdit.hide()
        self.qLineEdit2.hide()
        self.label1.hide()
        self.textEdit.hide()
        self.label2.hide()
        self.qLineEdit3.hide()
        self.button1.click()
        try:
            for x in self.savings_buttonlist:
                x.hide()
        except AttributeError:
            pass
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
        if len(stats.uppersave) >= 0:
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
            try:
                for x in processlist:
                    splittedX = x.split(":")
                    percent = float(splittedX[1]) / allTotal * 100
                    text += "\n" + x +str(round(percent,2))
            except ZeroDivisionError:
                pass
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
        self.hideall()
        #This state 3 is to sort how stuff should be defined
        #This will decide whether to auto-sort
        self.state = 2
        if debug:
            print("gostate2")
        self.qLineEdit.hide()
        self.hideall()
        self.setWindowTitle('Decide how to sort')
        text = ""
        try:
            if self.test_run:
                pass
            else:
                i = 0
                for line in open(stats.filename):
                    i += 1
                text += "There is file found with "+str(i)+" lines."


            text += "There is inbuild autosort\nDo you want to use it?"
            self.label1.setText(text)

            self.label1.show()
            self.button1 = QPushButton("Yes", self)
            self.button2 = QPushButton("No", self)
            buttomYaxis = 100
            self.button1.move(25,buttomYaxis)
            self.button1.show()

            self.button2.move(150,buttomYaxis)
            self.button2.show()
            self.button1.clicked.connect(self.gostate3)
            self.button2.clicked.connect(self.go_manual_sorting_start)
            if shortcut:
                self.button1.click()
            if self.test_run:
                self.button1.click()
        except FileNotFoundError:
            if debug:
                print("Gostate2; Filenotfounderror")
            self.gostate1()
    def go_manual_sorting_start(self):
        #Sort with manual labor

        if debug:
            print("go_manual_sorting_start")
        self.state = "manual_sorting"
        stats.keywordlist = {}
        self.gostate3()

    def go_sorting_stage(self):
        # In sorting stage, program asks you names for pieces of piechart
        # Plausible automatic sorting is already done and this is only with manual labor

        self.qLineEdit.hide()
        self.state = "go_sorting_stage"
        if debug:
            print(self.state)
        self.hideall()
        #First we create the window we see
        self.qLineEdit2.setText("")
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
        if len(stats.uppersave) == 0:
            text2 = "There are no groups made yet ): "
        else:
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
        self.button1.clicked.connect(self.manual_adding_user_input_validation)
        self.qLineEdit2.show()

        self.qLineEdit2.move(50,120)
        self.qLineEdit2.textChanged[str].connect(self.onChanged)
        self.hbox.addWidget(self.button1)

        xpos = [30,150,270]             # There 3 column at these coordinates
        ypos = [300, 50]                # ypos[0] is base value of y and ypos[1] is multiplier
                                        # 0 is where charting starts and 1 is the length between two rows
        self.savings_buttonlist = []    # We use this to access unnamed buttons
        for i, name in enumerate(sorted(stats.uppersave)):
            buttom_for_a_group = QPushButton(name, self)
            self.savings_buttonlist.append(buttom_for_a_group)
            buttom_for_a_group.move(xpos[i % 3], ypos[0] + ypos[1] * (i // 3))
            self.savings_buttonlist[i].clicked.connect(partial(self.whichbtn, self.savings_buttonlist[i]))
            buttom_for_a_group.show()
        if self.test_run:
            self.qLineEdit2.setText("asd")
            self.button1.click()
    def add_keyword_and_rerun(self):
        # When sorting is one with manual labor, this function adds keywords
        # This means this sorts a thing

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
        #This calculates values used by go_showinfo_phase

        if debug:
            print("go_showinfo_phase: Calculating numbers")
        totalsum = 0
        self.groupnames = []
        self.groupnominals = []
        self.grouppercents = []
        self.oversaved = []
        for group in stats.uppersave:
            self.groupnames.append(group)
            nominal = 0
            for number in stats.uppersave[group]:
                nominal += number
            self.groupnominals.append(nominal)

            # This is used to create snarky comment
            totalsum += nominal
            if nominal > 0:
                if debug:
                    print("NOMINAL IS UNDER 0")
                if group in self.oversaved:
                    pass
                else:
                    self.oversaved.append(group)

        # Here continues the legit functionality
        for i in range(len(self.groupnominals)):
            self.grouppercents.append(float(self.groupnominals[i] / totalsum)*100)

        self.text = ""
        totaltoShow = float(0)
        for i in range(len(self.groupnames)):
            numberToUse = self.grouppercents[i]
            self.text += str("{:22s} {:.2f}€  {:.2f}\n".format(self.groupnames[i],self.groupnominals[i] * -0.01, self.grouppercents[i]))
            totaltoShow += numberToUse

        nominalTotal = -totalsum / 100
        self.text += str("{:22s}{:.2f}\n".format("Total", nominalTotal))

    def go_showinfo_phase(self):
        # In this state of program the actualy piechart is shown. This is like Rome, every road leads here
        if debug:
            print("go_showinfo")
        # self.infowindow_reset should be run, when info shown in the window changes
        # If not, then not run
        list_of_reset_stages = ["get_savings_data", "go_sorting_stage", "manual_sorting", 2,"add_keyword_and_rerun","manual_adding_of_lines_add_a_line"]
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
        self.button2.setText("Restart")
        self.button2.move(150,325)
        self.button2.show()

        #insert buttom to manually add "lines" or events
        self.button3.clicked.connect(self.manual_adding_of_lines)
        self.button3.setText("Manual adding")
        self.button3.move(270,325)
        self.button3.show()

        #insert buttom to saving-program
        self.button4.clicked.connect(self.start_saving_program_step1)
        self.button4.setText("Savings program")
        self.button4.move(30,370)
        self.button4.show()

        # Program tells you if your too eager to save
        if len(self.oversaved) > 0:
            texti = "Oops, you cheap bastard\nLook what you did to budjet of "

            for i, x in enumerate(self.oversaved):
                texti += x
                if i < len(self.oversaved)-1:
                    texti += ","
                texti += " "
            self.label2.setText(texti)
            self.label2.move(25,375)
            self.label2.show()
        if self.test_run:
            self.button1.click()
            self.test_counter += 1


    def whichbtn(self, b):
        # This functionality is used by savings_program
        # Saving program has unnamed button in self.savings_buttonlist and this turn clicks
        # into names in lists.
        try:
            if debug:
                print("clicked button is " + b.text())
        except AttributeError:
            pass
        if self.state == "start_saving_program_step1":
            if b.text() in self.necessity:
                pass
            else:
                self.necessity.append(b.text())
            if debug:
                print("Necessity: ", self.necessity)
        elif self.state == "start_saving_program_step2":
            if b.text() in self.secondary:
                pass
            if b.text() in self.necessity:
                pass
            else:
                self.secondary.append(b.text())
            if debug:
                print("Secondary", self.secondary)
        elif self.state == "ask_amount":
            if str(b.text()) in self.secondary:
                pass
            if str(b.text()) in self.necessity:
                pass
            else:
                self.priority.append(b.text())
            if debug:
                print("priority", self.priority)
        elif self.state == "go_sorting_stage":
            self.qLineEdit2.setText(b.text())
        elif self.state == "Manual_line_adding":
            self.qLineEdit.setText(b.text())

        else:
            pass
        pass

    def start_saving_program_step1(self):
        # Here we first classify which are priorities and which are not
        # Then we think about how much can be saved
        # And then we will looks what does the situation looks like with savings

        # These info used to transfer info between states
        self.necessity = []
        self.priority = []
        self.secondary = []
        self.hideall()
        self.state = "start_saving_program_step1"
        if debug:
            print(self.state)

        # Forward and backwards functionalities
        self.setWindowTitle("Savings program")
        self.label1.setText("Click on the ones you cannot save from")
        self.label1.show()
        self.button1.setText("Continue")
        self.button1.move(270,50)
        self.button1.clicked.connect(self.start_saving_program_step2)
        self.button1.show()
        self.button2.setText("Cancel")
        self.button2.move(270,100)
        self.button2.clicked.connect(self.go_showinfo_phase)
        self.button2.show()

        # Here we create buttons the the existing groups
        # The buttoms are used to sort them into groups
        xpos = [30,150,270]             # There 3 column at these coordinates
        ypos = [150, 50]                # ypos[0] is base value of y and ypos[1] is multiplier
                                        # 0 is where charting starts and 1 is the length between two rows
        self.savings_buttonlist = []    # We use this to access unnamed buttons
        for i, name in enumerate(self.groupnames):
            #button_text = str(i)+str(name)
            buttom_for_a_group = QPushButton(name, self)
            self.savings_buttonlist.append(buttom_for_a_group)
            buttom_for_a_group.move(xpos[i % 3], ypos[0] + ypos[1] * (i // 3))
            self.savings_buttonlist[i].clicked.connect(partial(self.whichbtn, self.savings_buttonlist[i]))
            self.savings_buttonlist[i].clicked.connect(partial(self.savings_buttonlist[i].hide))
            buttom_for_a_group.show()
        # First we choose necessities
        if self.test_run:
            first_group = [4,5,6,7]
            for i in range(4):
                self.savings_buttonlist[first_group[i]].click()
            self.button1.click()


    def start_saving_program_step2(self):
        # Then we choose the "maybe yes, but i dont wanna"
        # We continue with the same chart and ones picked in earlier state are already gone

        self.state = "start_saving_program_step2"
        if debug:
            print(self.state)

        xpos = [30,150,270]
        ypos = [150, 50]


        self.setWindowTitle("Savings program")
        self.label1.setText("Click on the ones you can save from but rather not")
        self.label1.show()
        self.button1.setText("Continue")
        self.button1.move(270,50)
        self.button1.clicked.connect(self.ask_amount)
        self.button1.show()
        self.button2.setText("Cancel")
        self.button2.move(270,100)
        self.button2.clicked.connect(self.go_showinfo_phase)
        self.button2.show()

        # For testing
        if self.test_run:
            self.savings_buttonlist[1].click()
            self.savings_buttonlist[2].click()
            self.ask_amount()

    def ask_amount(self):
        # Now that you have your priorities in order, here we think how much can be saved

        self.state= "ask_amount"
        if debug:
            print("State:",self.state)
        self.hideall()
        for i in range(len(self.savings_buttonlist)):
            self.savings_buttonlist[i].click()
        self.label1.setText("How much are you planning to save?\nPlease give number in cents ")
        self.label1.show()
        self.qLineEdit.move(100,100)
        self.qLineEdit.setText("")
        self.qLineEdit.show()
        # For some reason, button1 becomes f upped
        self.button1.setText("Continue")
        self.button1.move(270,50)
        self.button1.clicked.connect(self.get_savings_data)
        self.button1.show()
        # This remains ok it seems
        self.button2.show()

        if self.test_run:

            self.qLineEdit.setText("30000")
            self.button1.click()


    def get_savings_data(self):


        for name in self.secondary:        # This is a cleanup
            if name in self.priority:
                self.priority.remove(name)
        amount = self.qLineEdit.text()
        amount = amount.strip(" ")
        amount = int(amount)
        self.state= "get_savings_data"
        if debug:
            print("State:",self.state)
            print("Amount", amount)
        self.hideall()
        # Math is like savings are doubled for priority
        # amount is between groups
        weighted_amount = len(self.priority) * 2 + len(self.secondary)
        per_unit_save_target = round(amount / weighted_amount,0)
        per_unit_save_target = -int(per_unit_save_target)




        i = 0
        if debug:
            print("Amount", amount)
            print("WA ", weighted_amount)
            print("Unit target ", per_unit_save_target)

        stats.uppersave["Saved amount"] = [-amount]
        text = "These values are based in\namount wanted to be saved, priorities given earlier\n\n"
        for name in self.priority:
            self.qLineEdit.setText(name)
            value = (2*per_unit_save_target)
            self.qLineEdit3.setText(str(value))
            textToAdd = str(name) + "   " + str(value) + "\n"
            for i in range(len(textToAdd)):
                if i == len(textToAdd) - 3:
                    text += ","
                text += textToAdd[i]
            self.manual_adding_of_lines_add_a_line()
        for name in self.secondary:
            self.qLineEdit.setText(name)
            value = (per_unit_save_target)
            self.qLineEdit3.setText(str(value))
            textToAdd = str(name) + "   " + str(value) + "\n"
            for i in range(len(textToAdd)):
                if i == len(textToAdd) - 3:
                    text += ","
                text += textToAdd[i]
            self.manual_adding_of_lines_add_a_line()
        self.show_savings_data(text)
    def show_savings_data(self, text):
        self.state = "show_savings_data"
        numberOfNextLines = text.count("\n")
        if debug:
            print(self.state)
            print("numberOfNextLines", numberOfNextLines)
        self.hideall()
        self.label1.setText(text)
        self.label1.show()
        self.button1.clicked.connect(self.go_showinfo_phase)
        self.button1.setText("See results")
        buttom1_yaxis = 30 * numberOfNextLines
        self.button1.move(150,buttom1_yaxis)
        self.button1.show()
        if self.test_run:
            self.button1.click()
    def restarting(self):
        # Still dont know if this should be deleted
        self.window_reset()
        stats.__init__()
        stats.keywordlist = stats.keywordlistsave
        stats.filename = ""
        stats.filenotfound = True
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
        text = "1: Write the name of the piece of the pie to which you want to add an amount:\n"
        text += "2: Insert the amount of money spent. \n! Do not use , or ., but insert the amount in cents !"
        text += "\nValues below 0 reduce spending"

        self.label1.setText(text)
        self.label1.show()
        self.qLineEdit.move(qlineX,90)
        self.qLineEdit.setCursorPosition(0)
        self.qLineEdit.show()

        self.qLineEdit3.move(qlineX,135)
        self.qLineEdit3.show()
        buttomY = 187
        self.button1.move(25, buttomY)
        self.button1.setText("Add info")

        self.button1.clicked.connect(self.manual_adding_user_input_validation)
        self.button2.move(150, buttomY)
        self.button2.setText("Calcel")
        self.button2.clicked.connect(self.go_showinfo_phase)
        self.button1.show()
        self.button2.show()



        xpos = [30,150,270]             # There 3 column at these coordinates
        ypos = [300, 50]                # ypos[0] is base value of y and ypos[1] is multiplier
                                        # 0 is where charting starts and 1 is the length between two rows
        self.savings_buttonlist = []    # We use this to access unnamed buttons
        for i, name in enumerate(sorted(stats.uppersave)):
            buttom_for_a_group = QPushButton(name, self)
            self.savings_buttonlist.append(buttom_for_a_group)
            buttom_for_a_group.move(xpos[i % 3], ypos[0] + ypos[1] * (i // 3))
            self.savings_buttonlist[i].clicked.connect(partial(self.whichbtn, self.savings_buttonlist[i]))
            buttom_for_a_group.show()


    def manual_adding_user_input_validation(self):
        # I asked a friend to try my interface whether it was understandable without additional info from me
        # He replied "I was able to crash program with adding random asian letter to field asking for a number
        # So here we are

        # This is the max limit for str-type objects when trying to add in fields
        # What goes over this is cut ): Too large string make the window look bad like MJ
        maxStrRange = 35

        if self.state == "Manual_line_adding":
            try:
                 muuttuja = self.qLineEdit3.text()
                 muuttuja = int(muuttuja)
                 muuttuja = self.qLineEdit.text()
                 muuttuja2 = ""
                 if len(muuttuja) > maxStrRange:
                     for i in range(maxStrRange):
                         muuttuja2 += muuttuja[i]
                     self.qLineEdit = muuttuja2
                 self.manual_adding_of_lines_add_a_line()
            except ValueError:
                if debug:
                    print("ValueError")
                self.label1.setText("There seems to be a problem trying to\nConvert field 2 to a round number")
                pass
        elif self.state == "go_sorting_stage":
            if debug:
                print(self.state, "-> validation")
            muuttuja = self.qLineEdit2.text()
            muuttuja2 = ""
            if len(muuttuja) > maxStrRange:
                for i in range(maxStrRange):
                    muuttuja2 += muuttuja[i]
            self.qLineEdit2.setText(muuttuja2)
            self.add_keyword_and_rerun()
        else:
            pass

    def manual_adding_of_lines_add_a_line(self):
        if self.state == "get_savings_data":
            continuue = False
        else:
            continuue = True

        self.state= "manual_adding_of_lines_add_a_line"
        if debug:
            print(self.state)
        oppressor = self.qLineEdit.text()
        oppressor = oppressor.rstrip(" ")
        oppressor = oppressor.lstrip(" ")
        amount = self.qLineEdit3.text()
        if debug:
            print("1,2", oppressor,amount)
            print(len(stats.lowersave))
        amount = str(amount).strip(" ")
        amount = int(amount)
        amount = -1 * amount
        self.manually_added_lines[oppressor] = amount
        if debug:
            print(self.manually_added_lines)

        try:
            stats.uppersave[oppressor].append(self.manually_added_lines[oppressor])
        except KeyError:
            stats.uppersave[oppressor] = [self.manually_added_lines[oppressor]]
        if continuue:
            self.go_showinfo_phase()




    def changeColor_infowindow(self):
        #We need colors to differentiate chart pieces from each other
        #This can both create new or overwrite old
        self.colors = []
        colorsneeded = len(stats.uppersave)
        # First this uses len(stats.uppersave) and then len(self.groupnames)
        # The amount of groups will change during the run of program
        if len(self.groupnames) > colorsneeded:
            colorsneeded = len(self.groupnames)

        # One extra is needed for savings-program
        # One extra is in case coder messes things up
        for i in range((colorsneeded)+2):
            number = []
            for count in range(3):
                number.append(random.randrange(0, 255))
            self.colors.append(QColor(number[0], number[1], number[2]))
        if debug:
            print("Self.colors LEN: ", len(self.colors))

    def paintEvent(self, event):
        def piechart1():
                #And now we try to paint pie chart
                # This draws the piechart that represents the true values
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

        painter = QPainter(self)
        painter.setBrush(QBrush(Qt.darkGray, Qt.SolidPattern))
        painter.drawRect(0, 0, self.width(), self.height())
        if self.state == "info":
            piechart1()
        elif self.state == "saving_info":
            piechart1()

        else:
            pass

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
    def keyPressEvent( self , e ):

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
        self.keywordlist = {"MOB.PAY":"Tilisiirrot", "Compass Group":"Ruokailu","Ylva palve":"Ruokailu","Prisma":"Kaupat","HOAS":"Asuminen","Alepa":"Kaupat","Tokmanni":"Kaupat","Steam":"Viihde","Market":"Kaupat","Clas Ohlson":"Kaupat","Luckiefun":"Viihde","Pallohalli":"Urheilu","Lidl":"Kaupat","R ":"Kaupat","Sanoma":"Viihde","Farmasialiitto":"Muu","Amarillo":"Viihde","Pizze":"Viihde"}
        self.keywordlistsave = {"MOB.PAY":"Tilisiirrot","Compass Group":"Ruokailu","Ylva palve":"Ruokailu","Prisma":"Kaupat","HOAS":"Asuminen","Alepa":"Kaupat","Tokmanni":"Kaupat","Steam":"Viihde","Market":"Kaupat","Clas Ohlson":"Kaupat","Luckiefun":"Viihde","Pallohalli":"Urheilu","Lidl":"Kaupat","R ":"Kaupat","Sanoma":"Viihde","Farmasialiitto":"Muu","Amarillo":"Viihde","Pizze":"Viihde"}
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
        self.manually_added_lines = {}
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
#print(text)
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
    elif len(str(name)) <= 2:
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
        if debug:
            print(len(listused), len(definedused))
    for oppressor in listused:
        if oppressor in definedused:
            pass
        else:
            palautuslista.append(oppressor)
    return palautuslista

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
            print("\n\nNow this will print those not defined:")
        for undefined in searchUndefined():
            stats.undefined.append(undefined)
            if debug:
                print(undefined)

    if len(stats.upperlist) > 0:
        stats.reset()


