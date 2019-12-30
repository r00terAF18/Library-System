import os
import sqlite3
import sys
import datetime

from PyQt5 import QtGui, uic
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType

import icons_rc

ui,_ = loadUiType('Library System UI v4.ui')

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
        self.updateSettingsDB()
        self.mainTab.tabBar().setVisible(False)
        self.showBooks()
        self.showClients()
        self.updateOperationsDB()

    ### Button Handler ####
    def ButtonHandler(self):
        self.btnTheme.clicked.connect(self.showThemeWindow)
        self.btnLightTheme.clicked.connect(self.setLightTheme)
        self.btnDarkTheme.clicked.connect(self.setDarkTheme)
        self.btnDarkOrange.clicked.connect(self.setDarkOrangeTheme)
        self.btnDarkGray.clicked.connect(self.setDarkGrayTheme)
        self.btnMainDayToDay.clicked.connect(self.showDayToDay)
        self.btnMainBooks.clicked.connect(self.showBooksTab)
        self.btnMainUsers.clicked.connect(self.showUsersTab)
        self.btnMainClients.clicked.connect(self.showClientsTab)
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
        self.btnSaveNewClient.clicked.connect(self.addNewClient)
        self.btnSearchClient.clicked.connect(self.searchClient)
        self.btnSaveEditClient.clicked.connect(self.editClient)
        self.btnDeleteClient.clicked.connect(self.deleteClient)

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
        style = open('Themes\Dark.css', 'r')
        style = style.read()
        MainApp.setStyleSheet(self, style)
        self.ThemeWindow.setVisible(False)

    def setDarkGrayTheme(self):
        style = open('Themes\DarkGray.css', 'r')
        style = style.read()
        MainApp.setStyleSheet(self, style)
        self.ThemeWindow.setVisible(False)
    
    def setDarkOrangeTheme(self):
        style = open('Themes\DarkOrange.css', 'r')
        style = style.read()
        MainApp.setStyleSheet(self, style)
        self.ThemeWindow.setVisible(False)

    ### UI Funtions ###

    def showDayToDay(self):
        self.mainTab.setCurrentIndex(0)

    def showBooksTab(self):
        self.mainTab.setCurrentIndex(1)

    def showUsersTab(self):
        self.mainTab.setCurrentIndex(2)

    def showClientsTab(self):
        self.mainTab.setCurrentIndex(3)

    def showSettingsTab(self):
        self.mainTab.setCurrentIndex(4)


    ### OPERATIONS ###

    def addNewOperation(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        bookTitle = self.txtOperationBookTitle.text()
        clientID = self.txtOperationClientsID.text()
        operation = self.comboBoxOperation.currentText()
        duration = int(self.comboBoxDuration.currentText())
        toDay = datetime.date.today()
        dueDate = toDay + datetime.timedelta(days=duration)

        cur.execute('INSERT INTO OperationsDB("Book Name", "Client ID", Type, Start, "Due Date") VALUES(?, ?, ?, ?, ?)', (bookTitle, clientID, operation, toDay, dueDate, ))
        connection.commit()
        connection.close()
        self.txtOperationBookTitle.setText('')
        self.txtOperationClientsID.setText('')

        self.updateOperationsDB()

    ### EXPORTING DB ###

    


    ### USERS ###

    def addUser(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        usrName = self.txtNewUser.text()
        email = self.txtNewEmail.text()
        passwd = self.txtNewPasswd.text()
        passwd2 = self.txtNewPasswdAgain.text()

        if passwd == passwd2:
            cur.execute('INSERT INTO UsersDB(Name, Email, Password) VALUES(?, ?, ?)', (usrName, email, passwd, ))
            connection.commit()
            QMessageBox.information(self.tab_7, 'Success', 'You may now login with the entered credetnials', QMessageBox.Ok)
        elif passwd != passwd2:
            QMessageBox.warning(self.tab_7, 'Password not mathcing', 'Please make sure that you have typed your password right', QMessageBox.Ok)
        elif usrName == '' or usrName == ' ':
            QMessageBox.warning(self.tab_7, 'Empty field', 'Please make sure that you have filled all teh fields', QMessageBox.Ok)
        elif email == '' or email == ' ':
            QMessageBox.warning(self.tab_7, 'Empty field', 'Please make sure that you have filled all teh fields', QMessageBox.Ok)
        
        connection.close()

        self.txtNewUser.setText('')
        self.txtNewEmail.setText('')
        self.txtNewPasswd.setText('')
        self.txtNewPasswdAgain.setText('')

    def login(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        usrName = self.txtUserLogin.text()
        ### I dont want to store the passswdord in a variable

        cur.execute(f'SELECT Name, Email, Password FROM UsersDB WHERE Name = \'{usrName}\' AND Password = \'{self.txtPasswdLogin.text()}\'')
        data = cur.fetchone()
        if data:
            QMessageBox.information(self.tab_7, 'Successfully loged in', 'You have successfully loged in, you may now browse the app freely', QMessageBox.Ok)
            self.txtUpdateUser.setEnabled(True)
            self.txtUpdateEmail.setEnabled(True)
            self.txtUpdatePasswd.setEnabled(True)
            self.txtUpdateConfirmPasswd.setEnabled(True)
            self.btnUpdateUser.setEnabled(True)
            self.txtUpdateUser.setText(data[0])
            self.txtUpdateEmail.setText(data[1])
            connection.close()
        else:
            QMessageBox.warning(self.tab_7, 'Error', 'No mathcing Username or Password were found, please make sure you have entered everything correctly', QMessageBox.Ok)
        
        connection.close()


    def editUser(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        originalUsrName = self.txtUserLogin.text()
        originalPasswd = self.txtPasswdLogin.text()
        usrName = self.txtUpdateUser.text()
        email = self.txtUpdateEmail.text()
        passwd = self.txtUpdatePasswd.text()
        passwd2 = self.txtUpdateConfirmPasswd.text()

        if passwd == passwd2:
            cur.execute(f'UPDATE UsersDB SET Name = \'{usrName}\', Email = \'{email}\', Password = \'{passwd2}\' WHERE Name = \'{originalUsrName}\' AND Password = \'{originalPasswd}\'')
            connection.commit()
            QMessageBox.information(self.tab_7, 'Info updated', 'Your data hase been successfully updated, please login again', QMessageBox.Ok)
        else:
            QMessageBox.warning(self.tab_7, 'Error', 'No mathcing Username or Password were found, please make sure you have entered everything correctly', QMessageBox.Ok)

        connection.close()


    ### Clients ####

    def addNewClient(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        name = self.txtNewClientName.text()
        email = self.txtNewClientEmail.text()
        nID = int(self.txtNewClientID.text())

        cur.execute('INSERT INTO ClientsDB(Name, Email, "National ID") VALUES(?, ?, ?)', (name, email, nID, ))
        connection.commit()
        connection.close()

        self.showClients()

    def searchClient(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        searchID = int(self.txtSearchClientID.text())

        cur.execute(f'SELECT * FROM ClientsDB WHERE "National ID" = \'{searchID}\'')
        data = cur.fetchone()

        if data:
            self.txtEditClientName.setText(data[1])
            self.txtEditClientEmail.setText(data[2])
            self.txtEditClientID.setText(str(data[3]))

    def editClient(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        searchID = int(self.txtSearchClientID.text())
        name = self.txtEditClientName.text()
        email = self.txtEditClientEmail.text()
        nID = int(self.txtEditClientID.text())

        cur.execute(f'UPDATE ClientsDB SET Name=\'{name}\', Email=\'{email}\', "National ID"=\'{nID}\' WHERE "National ID"=\'{searchID}\'')
        connection.commit()
        connection.close()

        self.showClients()

    def deleteClient(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        searchID = int(self.txtSearchClientID.text())

        message = f"Are you sure that you want to delete the following Client >>> {searchID}"
        warning = QMessageBox.warning(self.tab_6, 'Delete Book', 'Are you sure you want to delete this Book?', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            cur.execute(f'DELETE FROM ClientsDB WHERE "National ID"=\'{searchID}\'')
            connection.commit()
            connection.close()
            self.txtSearchClientID.setText('')
            self.txtEditClientName.setText('')
            self.txtEditClientEmail.setText('')
            self.txtEditClientID.setText('')
        else:
            connection.close()
        
        self.showClients()

    ### BOOKS ###

    def searchBook(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        bookTitle = self.txtSearchBookTitle.text()

        cur.execute(f'SELECT * FROM BooksDB WHERE Name = \'{bookTitle}\'')
        data = cur.fetchone()

        if data:
            self.txtEditBookTitle.setText(data[1])
            self.txtEditBookDesc.setText(data[2])
            self.txtEditBookCode.setText(data[3])
            self.cmbBoxEditCat.setCurrentText(data[4])
            self.cmbBoxEditAuthor.setCurrentText(data[5])
            self.cmbBoxEditPublisher.setCurrentText(data[6])
            self.txtEditBookPrice.setText(str(data[7]))

    def editBook(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        searchBookTitle = self.txtSearchBookTitle.text()
        bookTitle = self.txtEditBookTitle.text()
        bookCode = self.txtEditBookCode.text()
        bookDesc = self.txtEditBookDesc.toPlainText()
        bookCat = self.cmbBoxEditCat.currentText()
        bookAuthor = self.cmbBoxEditAuthor.currentText()
        bookPublisher = self.cmbBoxEditPublisher.currentText()
        bookPrice = float(self.txtEditBookPrice.text())

        cur.execute(f'UPDATE BooksDB SET Name=\'{bookTitle}\', Descreption=\'{bookDesc}\', Code=\'{bookCode}\', Category=\'{bookCat}\', Author=\'{bookAuthor}\', Publisher=\'{bookPublisher}\', Price=\'{bookPrice}\' WHERE Name=\'{searchBookTitle}\'')
        connection.commit()
        connection.close()

        self.showBooks()

    def deleteBook(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        bookTitle = self.txtSearchBookTitle.text()
        message = f"Are you sure that you want to delete the following book >>> {bookTitle}"
        warning = QMessageBox.warning(self.tab_6, 'Delete Book', 'Are you sure you want to delete this Book?', QMessageBox.Yes | QMessageBox.No)
        if warning == QMessageBox.Yes:
            cur.execute(f'DELETE FROM BooksDB WHERE Name = \'{bookTitle}\'')
            connection.commit()
            connection.close()
        else:
            connection.close()
        self.showBooks()



    def addNewBook(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()

        bookTitle = self.txtAddBookTitle.text()
        bookCode = self.txtAddBookCode.text()
        bookDesc = self.txtAddBookDesc.toPlainText()
        bookCat = self.cmbBoxAddBookCat.currentText()
        bookAuthor = self.cmbBoxAddBookAuthor.currentText()
        bookPublisher = self.cmbBoxAddBookPublisher.currentText()
        bookPrice = float(self.txtAddBookPrice.text())

        cur.execute(f'INSERT INTO BooksDB(Name, Descreption, Code, Category, Author, Publisher, Price) VALUES(?, ?, ?, ?, ?, ?, ?)', (bookTitle, bookDesc, bookCode, bookCat, bookAuthor, bookPublisher, bookPrice, ))
        connection.commit()
        connection.close()

        self.txtAddBookTitle.setText('')
        self.txtAddBookCode.setText('')
        self.txtAddBookDesc.setText('')
        self.txtAddBookPrice.setText('')
        self.cmbBoxAddBookCat.setCurrentIndex(0)
        self.cmbBoxAddBookAuthor.setCurrentIndex(0)
        self.cmbBoxAddBookPublisher.setCurrentIndex(0)
        
        self.showBooks()

        ### SETTINGS ####

    def addNewCat(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        category = self.txtAddNewCategory.text()
        cur.execute('INSERT INTO CategoriesDB(Name) VALUES(?)', (category, ))
        connection.commit()
        connection.close()
        self.txtAddNewCategory.setText('')
        self.updateSettingsDB()

    def addNewAutohr(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        author = self.txtAddNewAuthor.text()
        cur.execute('INSERT INTO AuthorsDB(Name) VALUES(?)', (author, ))
        connection.commit()
        connection.close()
        self.txtAddNewAuthor.setText('')
        self.updateSettingsDB()

    def addNewPublisher(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        publisher = self.txtAddNewPublisher.text()
        cur.execute('INSERT INTO PublishersDB(Name) VALUES(?)', (publisher,))
        connection.commit()
        connection.close()
        self.txtAddNewPublisher.setText('')
        self.updateSettingsDB()

    ### TABLES ####

    def updateOperationsDB(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        cur.execute('SELECT "Book Name", "Client ID", Type, Start, "Due Date" FROM OperationsDB')
        data = cur.fetchall()

        if data:
            self.tableMain.setRowCount(0)
            self.tableMain.insertRow(0)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableMain.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1

                rowCount = self.tableMain.rowCount()
                self.tableMain.insertRow(rowCount)

    def showClients(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        cur.execute('SELECT Name, Email, "National ID" FROM ClientsDB')
        data = cur.fetchall()

        if data:
            self.tableAllClients.setRowCount(0)
            self.tableAllClients.insertRow(0)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableAllClients.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1

                rowCount = self.tableAllClients.rowCount()
                self.tableAllClients.insertRow(rowCount)

    def showBooks(self):
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        cur.execute('SELECT Name, Descreption, Code, Category, Author, Publisher, Price FROM BooksDB')
        data = cur.fetchall()

        if data:
            self.tableAllBooks.setRowCount(0)
            self.tableAllBooks.insertRow(0)
            for row, form in enumerate(data):
                for col, item in enumerate(form):
                    self.tableAllBooks.setItem(row, col, QTableWidgetItem(str(item)))
                    col += 1

                rowCount = self.tableAllBooks.rowCount()
                self.tableAllBooks.insertRow(rowCount)

    def updateSettingsDB(self):
        self.clearComboBoxes()
        self.clearTables()
        # first initilise a list so that we can loop over
        #  with mostly the same code-base
        tables = ['AuthorsDB', 'CategoriesDB', 'PublishersDB']
        connection = sqlite3.connect('LibraryDB.db')
        cur = connection.cursor()
        for table in tables:
            query = f'SELECT Name FROM {table}'
            # print(query)
            cur.execute(query)
            data = cur.fetchall()
            if data:
                if table == 'AuthorsDB':
                    self.tableAuthor.insertRow(0)
                    for row, form in enumerate(data):
                        for col, item in enumerate(form):
                            self.tableAuthor.setItem(row, col, QTableWidgetItem(str(item)))
                            self.cmbBoxAddBookAuthor.addItem(str(item))
                            self.cmbBoxEditAuthor.addItem(str(item))
                            col += 1

                        rowCount = self.tableAuthor.rowCount()
                        self.tableAuthor.insertRow(rowCount)
                
                elif table == 'CategoriesDB':
                    self.tableCategory.insertRow(0)
                    for row, form in enumerate(data):
                        for col, item in enumerate(form):
                            self.tableCategory.setItem(row, col, QTableWidgetItem(str(item)))
                            self.cmbBoxAddBookCat.addItem(str(item))
                            self.cmbBoxEditCat.addItem(str(item))
                            col += 1

                        rowCount = self.tableCategory.rowCount()
                        self.tableCategory.insertRow(rowCount)

                elif table == 'PublishersDB':
                    self.tablePublisher.insertRow(0)
                    for row, form in enumerate(data):
                        for col, item in enumerate(form):
                            self.tablePublisher.setItem(row, col, QTableWidgetItem(str(item)))
                            self.cmbBoxAddBookPublisher.addItem(str(item))
                            self.cmbBoxEditPublisher.addItem(str(item))
                            col += 1

                        rowCount = self.tablePublisher.rowCount()
                        self.tablePublisher.insertRow(rowCount)

    def clearComboBoxes(self):
        self.cmbBoxEditAuthor.clear()
        self.cmbBoxAddBookAuthor.clear()
        self.cmbBoxAddBookCat.clear()
        self.cmbBoxEditCat.clear()
        self.cmbBoxAddBookPublisher.clear()
        self.cmbBoxEditPublisher.clear()

    def clearTables(self):
        self.tableAuthor.clearContents()
        self.tableAuthor.setColumnCount(1)
        self.tableAuthor.setRowCount(0)
        self.tableCategory.clearContents()
        self.tableCategory.setColumnCount(1)
        self.tableCategory.setRowCount(0)
        self.tablePublisher.clearContents()
        self.tablePublisher.setColumnCount(1)
        self.tablePublisher.setRowCount(0)



def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
