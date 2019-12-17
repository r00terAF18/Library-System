import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sqlite3
import icons_rc

ui, _ = loadUiType('Library System UI.ui')


class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.handleUI()
        self.handleButtons()


    def handleButtons(self):
        ### Open and close Theme Window ###
        self.btnTheme.clicked.connect(self.showThemeWindow)
        self.btnLightTheme.clicked.connect(self.hideThemeWindow)
        self.btnDarkTheme.clicked.connect(self.hideThemeWindow)
        ### Move to different Tabs ###
        if self.btnMainDayToDay.clicked:
            print('Day to day operation buttons was clicked')
            self.mainTab.setCurrentIndex(0)
        elif self.btnMainBooks.clicked:
            print('Books buttons was clicked')
            self.mainTab.setCurrentIndex(1)
        # self.btnMainDayToDay.clicked(self.mainTab.setCurrentIndex(0))
        # self.btnMainBooks.clicked(self.mainTab.setCurrentIndex(1))
        # self.btnMainUsers.clicked(self.mainTab.setCurrentIndex(2))
        # self.btnMainSettings.clicked(self.mainTab.setCurrentIndex(3))


    def handleUI(self):
        self.hideThemeWindow()
        self.mainTab.tabBar().setVisible(False)
    
    def showThemeWindow(self):
        self.ThemeWindow.show()

    def hideThemeWindow(self):
        self.ThemeWindow.hide()


def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
