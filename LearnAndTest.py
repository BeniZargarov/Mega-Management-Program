from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from ProgramGui import *

class Window(QWidget):

    def __init__(self):
        super().__init__()
        print(self.cal_main_calendar.selectedDate())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    gui = Window()
    gui.show()
    app.exec_()