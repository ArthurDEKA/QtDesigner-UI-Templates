from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.uic import loadUi
import sys

#import the themes
from qt_material import *

class MainUI(QMainWindow):
    def __init__(self):
        super(MainUI, self).__init__()
        
        loadUi("mainui.ui", self)

        #call a function when a menu button is clicked
        self.actionDark_red.triggered.connect(self.dark_red)
        self.actionDark_blue.triggered.connect(self.dark_blue)
        self.actionLight_Yellow.triggered.connect(self.light_yellow)
        
    def dark_red(self):
        apply_stylesheet(app, theme='dark_red.xml')

    def dark_blue(self):
        apply_stylesheet(app, theme='dark_blue.xml')
        
    def light_yellow(self):
        apply_stylesheet(app, theme='dark_yellow.xml')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = MainUI()
    ui.show()
    app.exec_()