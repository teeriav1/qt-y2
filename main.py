from luonnos050521 import *
import os

def clean():
    #Old, worked on python 3.7
    print(u"{}[2J{}[;H".format(chr(27), chr(27)))
def main():
    clean()
    app = QApplication(sys.argv)
    ex = Example(True)
    sys.exit(app.exec_())

main()
