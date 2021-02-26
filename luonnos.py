# -*- coding: utf-8 -*-
"""
Created on Sat Feb 20 09:41:33 2021


"""
class Stats():
    def __init__(self):
        self.id = 0
        self.lowerlist = {}
        self.upperlist = {}
        self.keywordlist = {"Teknologforeningen":"Ruokailu","Compass Gr":"Ruokailu","Ylva palve":"Ruokailu","Prisma":"Kaupat","HOAS":"Asuminen","Alepa":"Kaupat","MOB.PAY":"TILISIIRROT","TILISIIRTO":"TILISIIRROT","Tokmanni":"Kaupat","Steam":"Viihde","Market":"Kaupat","Clas Ohlson":"Kaupat","Luckiefun":"Viihde","Pallohalli":"Urheilu","Lidl":"Kaupat","R ":"Kaupat","Sanoma":"Viihde","Farmasialiitto":"Muu","Amarillo":"Viihde","Pizze":"Viihde"}
        self.defined = []
stats = Stats()
def openfile():
    
    #This opens file and does handleline-function to all lines except the one with names
    #path = r"C:\Users\Weke\Documents\Pyton\Y2\projekti\tapahtumat20210101-20210218.csv"
    path = r"tapahtumat20210101-20210218.csv"
    with open(path) as file:
        for i,x in enumerate( file):
            if i == 0:
                pass
            else:
                handleline(x)

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
def printundefined():
    for oppressor in stats.lowerlist:
        if oppressor in stats.defined:
            pass
        else:
            print(oppressor)

def clean():
    print('cls')
    print("\033[H\033[J")           
         
def main():
    clean()
    openfile()
    for oppressor in stats.lowerlist:
        print(oppressor, stats.lowerlist[oppressor])
        pass

    
    print("\n\n\n")
    #print(stats.upperlist)
    alltotal = 0
    for keyword in stats.upperlist:
        print(keyword," ",end="")
        summa = 0
        for luku in stats.upperlist[keyword]:
            summa += luku
        print(summa*-1)
        alltotal += summa

    print("")
    print("All total ", alltotal)
    print("\n\nNow this print those not defined:")
    printundefined()
main()