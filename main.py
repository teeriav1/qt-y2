from final import *
import os


def main():

    app = QApplication(sys.argv)
    ex = Example(True)
    sys.exit(app.exec_())

main()
