import os
import sqlite3
import sys

from PyQt5 import QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import icons_rc

ui,_ = loadUiType('Library System UI v2.ui')

class MainApp(QMainWindow, ui):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.UI_Handler()
        self.ButtonHandler()
    
    ### UI_Handler ###
    def UI_Handler(self):
        self.setDarkOrangeTheme()
        self.hideThemeWindow()

    ### Button Handler ####
    def ButtonHandler(self):
        self.btnTheme.clicked.connect(self.showThemeWindow)
        self.btnLightTheme.clicked.connect(self.setLightTheme)
        self.btnDarkTheme.clicked.connect(self.setDarkTheme)
        self.btnDarkOrange.clicked.connect(self.setDarkOrangeTheme)
        self.btnMainDayToDay.clicked.connect(self.showDayToDay)
        self.btnMainBooks.clicked.connect(self.showBooksTab)
        self.btnMainUsers.clicked.connect(self.showUsersTab)
        self.btnMainSettings.clicked.connect(self.showSettingsTab)
        self.btnAddCategory.clicked.connect(self.addNewCat)
        self.btnAddAuthor.clicked.connect(self.addNewAutohr)
        self.btnAddPublisher.clicked.connect(self.addNewPublisher)
        self.btnAddOperation.clicked.connect(self.addNewOperation)
        self.btnAddBook.clicked.connect(self.addNewBook)
        self.btnSearchBooks.clicked.connect(self.searchBook)
        self.btnBookSave.clicked.connect(self.editBook)
        self.btnDeleteBook.clicked.connect(self.deleteBook)
        self.btnLogin.clicked.connect(self.login)
        self.btnRegister.clicked.connect(self.addUser)
        self.btnUpdateUser.clicked.connect(self.editUser)

        ### Theme Window ###
    def showThemeWindow(self):
        self.ThemeWindow.setVisible(True)
    
    def hideThemeWindow(self):
        self.ThemeWindow.setVisible(False)

    def setLightTheme(self):
        style = ''
        MainApp.setStyleSheet(self, style)
        self.ThemeWindow.setVisible(False)

    def setDarkTheme(self):
        style = open('Themes\DarkGray.css', 'r')
        style = style.read()
        MainApp.setStyleSheet(self, style)
        self.ThemeWindow.setVisible(False)
    
    def setDarkOrangeTheme(self):
        style = open('Themes\DarkOrange.css', 'r')
        style = style.read()
        MainApp.setStyleSheet(self, style)
        self.ThemeWindow.setVisible(False)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
