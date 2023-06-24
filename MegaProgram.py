from PyQt5 import QtGui, QtCore, QtWidgets
from MMP import MoneyMP
from Calender import Calender
from PyQt5.QtWidgets import *
from ProgramGui import Ui_allprograms
from datetime import *
from PyQt5.QtCore import QTime, QTimer
import glob
import operator

class MegaProgram(MoneyMP, Calender):
    def __init__(self):
        super().__init__()

        Calender.__init__(self)
        MoneyMP.__init__(self)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = MegaProgram()
    gui.show()
    app.exec_()