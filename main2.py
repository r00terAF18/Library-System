import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
import sqlite3
import icons_rc



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        ### Setup the window ###
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(968, 516)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        ### add a default application wide font ###
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(10)
        font.setStrikeOut(False)
        font.setKerning(True)
        font.setStyleStrategy(QFont.PreferAntialias)
        MainWindow.setFont(font)
        MainWindow.setToolTip("")
        MainWindow.setStatusTip("")
        MainWindow.setWhatsThis("")
        MainWindow.setTabShape(QTabWidget.Rounded)
        MainWindow.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AllowTabbedDocks|QMainWindow.AnimatedDocks)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.mainTab = QTabWidget(self.centralwidget)
        self.mainTab.setGeometry(QRect(120, 0, 851, 471))
        self.mainTab.setObjectName("mainTab")
        self.mainTab.tabBar().setVisible(False)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.tableMain = QTableWidget(self.tab)
        self.tableMain.setGeometry(QRect(0, 80, 841, 361))
        self.tableMain.setObjectName("tableMain")
        self.tableMain.setColumnCount(6)
        self.tableMain.setRowCount(0)
        item = QTableWidgetItem()
        self.tableMain.setHorizontalHeaderItem(0, item)
        item = QTableWidgetItem()
        self.tableMain.setHorizontalHeaderItem(1, item)
        item = QTableWidgetItem()
        self.tableMain.setHorizontalHeaderItem(2, item)
        item = QTableWidgetItem()
        self.tableMain.setHorizontalHeaderItem(3, item)
        item = QTableWidgetItem()
        self.tableMain.setHorizontalHeaderItem(4, item)
        item = QTableWidgetItem()
        self.tableMain.setHorizontalHeaderItem(5, item)
        self.btnAddOperation = QPushButton(self.tab)
        self.btnAddOperation.setGeometry(QRect(740, 30, 75, 23))
        self.btnAddOperation.setLayoutDirection(Qt.LeftToRight)
        self.btnAddOperation.setFlat(False)
        self.btnAddOperation.setObjectName("btnAddOperation")
        self.txtOperationBookTitle = QLineEdit(self.tab)
        self.txtOperationBookTitle.setGeometry(QRect(20, 30, 251, 20))
        self.txtOperationBookTitle.setObjectName("txtOperationBookTitle")
        self.comboBoxDuration = QComboBox(self.tab)
        self.comboBoxDuration.setGeometry(QRect(590, 30, 69, 22))
        self.comboBoxDuration.setObjectName("comboBoxDuration")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxDuration.addItem("")
        self.comboBoxOperation = QComboBox(self.tab)
        self.comboBoxOperation.setGeometry(QRect(360, 30, 111, 22))
        self.comboBoxOperation.setObjectName("comboBoxOperation")
        self.comboBoxOperation.addItem("")
        self.comboBoxOperation.addItem("")
        self.label = QLabel(self.tab)
        self.label.setGeometry(QRect(310, 30, 47, 16))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QLabel(self.tab)
        self.label_2.setGeometry(QRect(510, 30, 71, 16))
        font = QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.mainTab.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabBooks = QTabWidget(self.tab_2)
        self.tabBooks.setGeometry(QRect(0, 0, 851, 451))
        self.tabBooks.setObjectName("tabBooks")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName("tab_5")
        self.txtAddBookTitle = QLineEdit(self.tab_5)
        self.txtAddBookTitle.setGeometry(QRect(30, 50, 301, 20))
        self.txtAddBookTitle.setObjectName("txtAddBookTitle")
        self.txtAddBookDesc = QTextEdit(self.tab_5)
        self.txtAddBookDesc.setGeometry(QRect(30, 80, 301, 231))
        self.txtAddBookDesc.setObjectName("txtAddBookDesc")
        self.txtAddBookCode = QLineEdit(self.tab_5)
        self.txtAddBookCode.setGeometry(QRect(510, 50, 301, 20))
        self.txtAddBookCode.setObjectName("txtAddBookCode")
        self.txtAddBookPrice = QLineEdit(self.tab_5)
        self.txtAddBookPrice.setGeometry(QRect(510, 200, 301, 20))
        self.txtAddBookPrice.setObjectName("txtAddBookPrice")
        self.cmbBoxAddBookCat = QComboBox(self.tab_5)
        self.cmbBoxAddBookCat.setGeometry(QRect(510, 80, 301, 22))
        self.cmbBoxAddBookCat.setObjectName("cmbBoxAddBookCat")
        self.cmbBoxAddBookCat.addItem("")
        self.cmbBoxAddBookAuthor = QComboBox(self.tab_5)
        self.cmbBoxAddBookAuthor.setGeometry(QRect(510, 120, 301, 22))
        self.cmbBoxAddBookAuthor.setObjectName("cmbBoxAddBookAuthor")
        self.cmbBoxAddBookAuthor.addItem("")
        self.cmbBoxAddBookPublisher = QComboBox(self.tab_5)
        self.cmbBoxAddBookPublisher.setGeometry(QRect(510, 160, 301, 22))
        self.cmbBoxAddBookPublisher.setObjectName("cmbBoxAddBookPublisher")
        self.cmbBoxAddBookPublisher.addItem("")
        self.btnAddBook = QPushButton(self.tab_5)
        self.btnAddBook.setGeometry(QRect(730, 290, 75, 23))
        self.btnAddBook.setObjectName("btnAddBook")
        self.tabBooks.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName("tab_6")
        self.txtEditBookCode = QLineEdit(self.tab_6)
        self.txtEditBookCode.setGeometry(QRect(510, 90, 301, 20))
        self.txtEditBookCode.setObjectName("txtEditBookCode")
        self.cmbBoxEditAuthor = QComboBox(self.tab_6)
        self.cmbBoxEditAuthor.setGeometry(QRect(510, 160, 301, 22))
        self.cmbBoxEditAuthor.setObjectName("cmbBoxEditAuthor")
        self.cmbBoxEditAuthor.addItem("")
        self.txtEditBookPrice = QLineEdit(self.tab_6)
        self.txtEditBookPrice.setGeometry(QRect(510, 240, 301, 20))
        self.txtEditBookPrice.setObjectName("txtEditBookPrice")
        self.btnBookSave = QPushButton(self.tab_6)
        self.btnBookSave.setGeometry(QRect(730, 330, 75, 23))
        self.btnBookSave.setObjectName("btnBookSave")
        self.txtEditBookTitle = QLineEdit(self.tab_6)
        self.txtEditBookTitle.setGeometry(QRect(30, 90, 301, 20))
        self.txtEditBookTitle.setObjectName("txtEditBookTitle")
        self.txtEditBookDesc = QTextEdit(self.tab_6)
        self.txtEditBookDesc.setGeometry(QRect(30, 120, 301, 231))
        self.txtEditBookDesc.setObjectName("txtEditBookDesc")
        self.cmbBoxEditCat = QComboBox(self.tab_6)
        self.cmbBoxEditCat.setGeometry(QRect(510, 120, 301, 22))
        self.cmbBoxEditCat.setObjectName("cmbBoxEditCat")
        self.cmbBoxEditCat.addItem("")
        self.cmbBoxEditPublisher = QComboBox(self.tab_6)
        self.cmbBoxEditPublisher.setGeometry(QRect(510, 200, 301, 22))
        self.cmbBoxEditPublisher.setObjectName("cmbBoxEditPublisher")
        self.cmbBoxEditPublisher.addItem("")
        self.txtSearchBookTitle = QLineEdit(self.tab_6)
        self.txtSearchBookTitle.setGeometry(QRect(30, 20, 301, 20))
        self.txtSearchBookTitle.setObjectName("txtSearchBookTitle")
        self.btnSearchBooks = QPushButton(self.tab_6)
        self.btnSearchBooks.setGeometry(QRect(510, 20, 75, 23))
        self.btnSearchBooks.setObjectName("btnSearchBooks")
        self.btnDeleteBook = QPushButton(self.tab_6)
        self.btnDeleteBook.setGeometry(QRect(640, 330, 75, 23))
        self.btnDeleteBook.setObjectName("btnDeleteBook")
        self.tabBooks.addTab(self.tab_6, "")
        self.mainTab.addTab(self.tab_2, "")
        self.tab_3 = QWidget()
        self.tab_3.setObjectName("tab_3")
        self.groupBoxAddNewUsr = QGroupBox(self.tab_3)
        self.groupBoxAddNewUsr.setGeometry(QRect(20, 20, 381, 401))
        self.groupBoxAddNewUsr.setObjectName("groupBoxAddNewUsr")
        self.txtNewUser = QLineEdit(self.groupBoxAddNewUsr)
        self.txtNewUser.setGeometry(QRect(40, 110, 291, 20))
        self.txtNewUser.setMaxLength(50)
        self.txtNewUser.setObjectName("txtNewUser")
        self.txtNewEmail = QLineEdit(self.groupBoxAddNewUsr)
        self.txtNewEmail.setGeometry(QRect(40, 140, 291, 20))
        self.txtNewEmail.setMaxLength(50)
        self.txtNewEmail.setObjectName("txtNewEmail")
        self.txtNewPasswd = QLineEdit(self.groupBoxAddNewUsr)
        self.txtNewPasswd.setGeometry(QRect(40, 170, 291, 20))
        self.txtNewPasswd.setInputMask("")
        self.txtNewPasswd.setMaxLength(32767)
        self.txtNewPasswd.setEchoMode(QLineEdit.Password)
        self.txtNewPasswd.setObjectName("txtNewPasswd")
        self.txtNewPasswdAgain = QLineEdit(self.groupBoxAddNewUsr)
        self.txtNewPasswdAgain.setGeometry(QRect(40, 200, 291, 20))
        self.txtNewPasswdAgain.setInputMask("")
        self.txtNewPasswdAgain.setMaxLength(32767)
        self.txtNewPasswdAgain.setEchoMode(QLineEdit.Password)
        self.txtNewPasswdAgain.setObjectName("txtNewPasswdAgain")
        self.btnRegister = QPushButton(self.groupBoxAddNewUsr)
        self.btnRegister.setGeometry(QRect(150, 240, 75, 23))
        self.btnRegister.setObjectName("btnRegister")
        self.groupBoxEditInfo = QGroupBox(self.tab_3)
        self.groupBoxEditInfo.setGeometry(QRect(430, 20, 381, 401))
        self.groupBoxEditInfo.setObjectName("groupBoxEditInfo")
        self.txtUpdateUser = QLineEdit(self.groupBoxEditInfo)
        self.txtUpdateUser.setEnabled(False)
        self.txtUpdateUser.setGeometry(QRect(60, 190, 291, 20))
        self.txtUpdateUser.setMaxLength(50)
        self.txtUpdateUser.setObjectName("txtUpdateUser")
        self.txtUpdatePasswd = QLineEdit(self.groupBoxEditInfo)
        self.txtUpdatePasswd.setEnabled(False)
        self.txtUpdatePasswd.setGeometry(QRect(60, 250, 291, 20))
        self.txtUpdatePasswd.setMaxLength(50)
        self.txtUpdatePasswd.setEchoMode(QLineEdit.Password)
        self.txtUpdatePasswd.setObjectName("txtUpdatePasswd")
        self.txtUpdateEmail = QLineEdit(self.groupBoxEditInfo)
        self.txtUpdateEmail.setEnabled(False)
        self.txtUpdateEmail.setGeometry(QRect(60, 220, 291, 20))
        self.txtUpdateEmail.setMaxLength(50)
        self.txtUpdateEmail.setObjectName("txtUpdateEmail")
        self.txtUpdateConfirmPasswd = QLineEdit(self.groupBoxEditInfo)
        self.txtUpdateConfirmPasswd.setEnabled(False)
        self.txtUpdateConfirmPasswd.setGeometry(QRect(60, 280, 291, 20))
        self.txtUpdateConfirmPasswd.setMaxLength(50)
        self.txtUpdateConfirmPasswd.setEchoMode(QLineEdit.Password)
        self.txtUpdateConfirmPasswd.setObjectName("txtUpdateConfirmPasswd")
        self.btnUpdateUser = QPushButton(self.groupBoxEditInfo)
        self.btnUpdateUser.setEnabled(False)
        self.btnUpdateUser.setGeometry(QRect(170, 320, 75, 23))
        self.btnUpdateUser.setObjectName("btnUpdateUser")
        self.txtUserLogin = QLineEdit(self.groupBoxEditInfo)
        self.txtUserLogin.setGeometry(QRect(60, 30, 291, 20))
        self.txtUserLogin.setMaxLength(50)
        self.txtUserLogin.setObjectName("txtUserLogin")
        self.txtPasswdLogin = QLineEdit(self.groupBoxEditInfo)
        self.txtPasswdLogin.setGeometry(QRect(60, 60, 291, 20))
        self.txtPasswdLogin.setMaxLength(50)
        self.txtPasswdLogin.setEchoMode(QLineEdit.Password)
        self.txtPasswdLogin.setObjectName("txtPasswdLogin")
        self.btnLogin = QPushButton(self.groupBoxEditInfo)
        self.btnLogin.setGeometry(QRect(170, 100, 75, 23))
        self.btnLogin.setObjectName("btnLogin")
        self.mainTab.addTab(self.tab_3, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName("tab_4")
        self.tabSubSettings = QTabWidget(self.tab_4)
        self.tabSubSettings.setGeometry(QRect(0, 0, 851, 451))
        self.tabSubSettings.setElideMode(Qt.ElideNone)
        self.tabSubSettings.setObjectName("tabSubSettings")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName("tab_7")
        self.tableCategory = QTableWidget(self.tab_7)
        self.tableCategory.setGeometry(QRect(0, 70, 841, 351))
        self.tableCategory.setObjectName("tableCategory")
        self.tableCategory.setColumnCount(1)
        self.tableCategory.setRowCount(0)
        item = QTableWidgetItem()
        self.tableCategory.setHorizontalHeaderItem(0, item)
        self.txtAddNewCategory = QLineEdit(self.tab_7)
        self.txtAddNewCategory.setGeometry(QRect(10, 20, 251, 20))
        self.txtAddNewCategory.setObjectName("txtAddNewCategory")
        self.btnAddCategory = QPushButton(self.tab_7)
        self.btnAddCategory.setGeometry(QRect(300, 20, 75, 23))
        self.btnAddCategory.setObjectName("btnAddCategory")
        self.tabSubSettings.addTab(self.tab_7, "")
        self.tab_8 = QWidget()
        self.tab_8.setObjectName("tab_8")
        self.tableAuthor = QTableWidget(self.tab_8)
        self.tableAuthor.setGeometry(QRect(0, 70, 841, 351))
        self.tableAuthor.setObjectName("tableAuthor")
        self.tableAuthor.setColumnCount(1)
        self.tableAuthor.setRowCount(0)
        item = QTableWidgetItem()
        self.tableAuthor.setHorizontalHeaderItem(0, item)
        self.txtAddNewAuthor = QLineEdit(self.tab_8)
        self.txtAddNewAuthor.setGeometry(QRect(10, 20, 251, 20))
        self.txtAddNewAuthor.setObjectName("txtAddNewAuthor")
        self.btnAddAuthor = QPushButton(self.tab_8)
        self.btnAddAuthor.setGeometry(QRect(300, 20, 75, 23))
        self.btnAddAuthor.setObjectName("btnAddAuthor")
        self.tabSubSettings.addTab(self.tab_8, "")
        self.tab_9 = QWidget()
        self.tab_9.setObjectName("tab_9")
        self.tablePublisher = QTableWidget(self.tab_9)
        self.tablePublisher.setGeometry(QRect(0, 70, 841, 351))
        self.tablePublisher.setObjectName("tablePublisher")
        self.tablePublisher.setColumnCount(1)
        self.tablePublisher.setRowCount(0)
        item = QTableWidgetItem()
        self.tablePublisher.setHorizontalHeaderItem(0, item)
        self.txtAddNewPublisher = QLineEdit(self.tab_9)
        self.txtAddNewPublisher.setGeometry(QRect(10, 20, 251, 20))
        self.txtAddNewPublisher.setObjectName("txtAddNewPublisher")
        self.btnAddPublisher = QPushButton(self.tab_9)
        self.btnAddPublisher.setGeometry(QRect(300, 20, 75, 23))
        self.btnAddPublisher.setObjectName("btnAddPublisher")
        self.tabSubSettings.addTab(self.tab_9, "")
        self.mainTab.addTab(self.tab_4, "")
        self.btnMainDayToDay = QPushButton(self.centralwidget)
        self.btnMainDayToDay.setGeometry(QRect(20, 10, 81, 71))
        self.btnMainDayToDay.setText("")
        icon = QIcon()
        icon.addPixmap(QPixmap(":/Icon/Today.png"), QIcon.Normal, QIcon.Off)
        self.btnMainDayToDay.setIcon(icon)
        self.btnMainDayToDay.setIconSize(QSize(60, 60))
        self.btnMainDayToDay.setObjectName("btnMainDayToDay")
        self.btnMainBooks = QPushButton(self.centralwidget)
        self.btnMainBooks.setGeometry(QRect(20, 100, 81, 71))
        self.btnMainBooks.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap(":/Icon/Books.png"), QIcon.Normal, QIcon.Off)
        self.btnMainBooks.setIcon(icon1)
        self.btnMainBooks.setIconSize(QSize(60, 60))
        self.btnMainBooks.setObjectName("btnMainBooks")
        self.btnMainUsers = QPushButton(self.centralwidget)
        self.btnMainUsers.setGeometry(QRect(20, 190, 81, 71))
        self.btnMainUsers.setText("")
        icon2 = QIcon()
        icon2.addPixmap(QPixmap(":/Icon/User.png"), QIcon.Normal, QIcon.Off)
        self.btnMainUsers.setIcon(icon2)
        self.btnMainUsers.setIconSize(QSize(60, 60))
        self.btnMainUsers.setObjectName("btnMainUsers")
        self.btnTheme = QPushButton(self.centralwidget)
        self.btnTheme.setGeometry(QRect(20, 370, 81, 71))
        self.btnTheme.setText("")
        icon3 = QIcon()
        icon3.addPixmap(QPixmap(":/Icon/Theme.png"), QIcon.Normal, QIcon.Off)
        self.btnTheme.setIcon(icon3)
        self.btnTheme.setIconSize(QSize(60, 60))
        self.btnTheme.setObjectName("btnTheme")
        self.btnMainSettings = QPushButton(self.centralwidget)
        self.btnMainSettings.setGeometry(QRect(20, 280, 81, 71))
        self.btnMainSettings.setText("")
        icon4 = QIcon()
        icon4.addPixmap(QPixmap(":/Icon/Settings.png"), QIcon.Normal, QIcon.Off)
        self.btnMainSettings.setIcon(icon4)
        self.btnMainSettings.setIconSize(QSize(60, 60))
        self.btnMainSettings.setObjectName("btnMainSettings")
        self.ThemeWindow = QGroupBox(self.centralwidget)
        self.ThemeWindow.setEnabled(True)
        self.ThemeWindow.setGeometry(QRect(320, 120, 361, 221))
        self.ThemeWindow.setStyleSheet("background-color: rgb(160, 160, 160);")
        self.ThemeWindow.setTitle("")
        self.ThemeWindow.setAlignment(Qt.AlignCenter)
        self.ThemeWindow.setObjectName("ThemeWindow")
        self.ThemeWindow.setVisible(False)
        self.btnLightTheme = QPushButton(self.ThemeWindow)
        self.btnLightTheme.setGeometry(QRect(80, 130, 91, 71))
        self.btnLightTheme.setObjectName("btnLightTheme")
        self.btnDarkTheme = QPushButton(self.ThemeWindow)
        self.btnDarkTheme.setGeometry(QRect(190, 130, 91, 71))
        self.btnDarkTheme.setObjectName("btnDarkTheme")
        self.label_3 = QLabel(self.ThemeWindow)
        self.label_3.setGeometry(QRect(100, 60, 181, 21))
        font = QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(16)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        # self.statusbar = QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)
        # self.menubar = QMenuBar(MainWindow)
        # self.menubar.setGeometry(QRect(0, 0, 968, 21))
        # self.menubar.setObjectName("menubar")
        # MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.mainTab.setCurrentIndex(0)
        self.tabBooks.setCurrentIndex(0)
        self.cmbBoxAddBookCat.setCurrentIndex(0)
        self.cmbBoxAddBookAuthor.setCurrentIndex(0)
        self.cmbBoxAddBookPublisher.setCurrentIndex(0)
        self.cmbBoxEditAuthor.setCurrentIndex(0)
        self.cmbBoxEditCat.setCurrentIndex(0)
        self.cmbBoxEditPublisher.setCurrentIndex(0)
        self.tabSubSettings.setCurrentIndex(0)
        QMetaObject.connectSlotsByName(MainWindow)

        ### UI Funtions ###

        def showDayToDay():
            self.mainTab.setCurrentIndex(0)

        def showBooksTab():
            self.mainTab.setCurrentIndex(1)

        def showUsersTab():
            self.mainTab.setCurrentIndex(2)

        def showSettingsTab():
            self.mainTab.setCurrentIndex(3)
            updateSettingsDB()

        def showThemeWindow():
            self.ThemeWindow.setVisible(True)

        def setLightTheme():
            self.ThemeWindow.setVisible(False)

        def setDarkTheme():
            self.ThemeWindow.setVisible(False)

        ### BOOKS ###

        def addNewOperation():
            connection = sqlite3.connect('LibraryDB.db')
            cur = connection.cursor()

            bookTitle = self.txtOperationBookTitle.text()
            operation = self.comboBoxOperation.currentText().text()
            duration = int(self.comboBoxDuration.currentText())

            cur.execute('INSERT INTO OperationsDB(Name, Type, Duration) VALUES(?, ?, ?)', (bookTitle, operation, duration))
            connection.commit()
            connection.close()
            self.txtOperationBookTitle.setText('')



        def addNewBook():
            connection = sqlite3.connect('LibraryDB.db')
            cur = connection.cursor()

            bookTitle = self.txtAddBookTitle.text()
            bookCode = self.txtAddBookCode.text()
            bookCat = self.cmbBoxAddBookCat.currentText()
            bookAuthor = self.cmbBoxAddBookAuthor.currentText()
            bookPublisher = self.cmbBoxAddBookPublisher.currentText()
            bookPrice = self.txtAddBookPrice.text()

        def addNewCat():
            connection = sqlite3.connect('LibraryDB.db')
            cur = connection.cursor()
            category = self.txtAddNewCategory.text()
            cur.execute('INSERT INTO CategoriesDB(Name) VALUES(?)', (category, ))
            connection.commit()
            connection.close()
            self.txtAddNewCategory.setText('')
            updateSettingsDB()

        def addNewAutohr():
            connection = sqlite3.connect('LibraryDB.db')
            cur = connection.cursor()
            author = self.txtAddNewAuthor.text()
            cur.execute('INSERT INTO AuthorsDB(Name) VALUES(?)', (author, ))
            connection.commit()
            connection.close()
            self.txtAddNewAuthor.setText('')
            updateSettingsDB()

        def addNewPublisher():
            connection = sqlite3.connect('LibraryDB.db')
            cur = connection.cursor()
            publisher = self.txtAddNewPublisher.text()
            cur.execute('INSERT INTO PublishersDB(Name) VALUES(?)', (publisher,))
            connection.commit()
            connection.close()
            self.txtAddNewPublisher.setText('')
            updateSettingsDB()

        def updateOperationsDB():
            ### first we need to clear out the entries and then add the new ones
            clearTables()
            ### Update the databse view for Categories ###
            connection = sqlite3.connect('LibraryDB.db')
            # connection.row_factory = sqlite3.Row
            cur = connection.cursor()
            cur.execute('SELECT Name FROM CategoriesDB')
            data = cur.fetchall()

            if data:
                self.tableCategory.insertRow(0)
                for row, form in enumerate(data):
                    for col, item in enumerate(form):
                        self.tableCategory.setItem(row, col, QTableWidgetItem(str(item)))
                        col += 1

                    rowCount = self.tableCategory.rowCount()
                    self.tableCategory.insertRow(rowCount)


        def updateSettingsDB():
            clearTables()
            clearTables()
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
        
        ### a function that will fill the combo boxes for the UI ###
        def fillComboBoxes():
            connection = sqlite3.connect('LibraryDB.db')
            cur = connection.cursor()

        def clearComboBoxes():
            self.cmbBoxEditAuthor.clear()
            self.cmbBoxAddBookAuthor.clear()
            self.cmbBoxAddBookCat.clear()
            self.cmbBoxEditCat.clear()
            self.cmbBoxAddBookPublisher.clear()
            self.cmbBoxEditPublisher.clear()

        def clearTables():
            self.tableAuthor.clearContents()
            self.tableAuthor.setColumnCount(1)
            self.tableAuthor.setRowCount(0)
            self.tableCategory.clearContents()
            self.tableCategory.setColumnCount(1)
            self.tableCategory.setRowCount(0)
            self.tablePublisher.clearContents()
            self.tablePublisher.setColumnCount(1)
            self.tablePublisher.setRowCount(0)
            self.tableMain.clearContents()
            self.tableMain.setColumnCount(1)
            self.tableMain.setRowCount(0)



        ### Buttons ###
        self.btnMainDayToDay.clicked.connect(showDayToDay)
        self.btnMainBooks.clicked.connect(showBooksTab)
        self.btnMainUsers.clicked.connect(showUsersTab)
        self.btnMainSettings.clicked.connect(showSettingsTab)
        self.btnTheme.clicked.connect(showThemeWindow)
        self.btnLightTheme.clicked.connect(setLightTheme)
        self.btnDarkTheme.clicked.connect(setDarkTheme)
        self.btnAddCategory.clicked.connect(addNewCat)
        self.btnAddAuthor.clicked.connect(addNewAutohr)
        self.btnAddPublisher.clicked.connect(addNewPublisher)
        self.btnAddOperation.clicked.connect(addNewOperation)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library System"))
        item = self.tableMain.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Code"))
        item = self.tableMain.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.tableMain.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Author"))
        item = self.tableMain.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Publisher"))
        item = self.tableMain.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Category"))
        item = self.tableMain.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Price"))
        self.btnAddOperation.setText(_translate("MainWindow", "Add"))
        self.txtOperationBookTitle.setPlaceholderText(_translate("MainWindow", "Enter Book Title"))
        self.comboBoxDuration.setItemText(0, _translate("MainWindow", "1"))
        self.comboBoxDuration.setItemText(1, _translate("MainWindow", "2"))
        self.comboBoxDuration.setItemText(2, _translate("MainWindow", "3"))
        self.comboBoxDuration.setItemText(3, _translate("MainWindow", "4"))
        self.comboBoxDuration.setItemText(4, _translate("MainWindow", "5"))
        self.comboBoxDuration.setItemText(5, _translate("MainWindow", "6"))
        self.comboBoxDuration.setItemText(6, _translate("MainWindow", "7"))
        self.comboBoxDuration.setItemText(7, _translate("MainWindow", "8"))
        self.comboBoxDuration.setItemText(8, _translate("MainWindow", "9"))
        self.comboBoxDuration.setItemText(9, _translate("MainWindow", "10"))
        self.comboBoxOperation.setItemText(0, _translate("MainWindow", "Retrieve"))
        self.comboBoxOperation.setItemText(1, _translate("MainWindow", "Rent"))
        self.label.setText(_translate("MainWindow", "Type"))
        self.label_2.setText(_translate("MainWindow", "Duration(W)"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab), _translate("MainWindow", "Operations"))
        self.txtAddBookTitle.setPlaceholderText(_translate("MainWindow", "Enter Book Title"))
        self.txtAddBookDesc.setPlaceholderText(_translate("MainWindow", "Enter Book Description"))
        self.txtAddBookCode.setPlaceholderText(_translate("MainWindow", "Enter Book Code"))
        self.txtAddBookPrice.setPlaceholderText(_translate("MainWindow", "Enter Book Price"))
        # self.cmbBoxAddBookCat.setCurrentText(_translate("MainWindow", "Category"))
        # self.cmbBoxAddBookCat.setItemText(0, _translate("MainWindow", "Category"))
        # self.cmbBoxAddBookAuthor.setCurrentText(_translate("MainWindow", "Category"))
        # self.cmbBoxAddBookAuthor.setItemText(0, _translate("MainWindow", "Category"))
        # self.cmbBoxAddBookPublisher.setCurrentText(_translate("MainWindow", "Category"))
        # self.cmbBoxAddBookPublisher.setItemText(0, _translate("MainWindow", "Category"))
        self.btnAddBook.setText(_translate("MainWindow", "Save"))
        self.tabBooks.setTabText(self.tabBooks.indexOf(self.tab_5), _translate("MainWindow", "Add New Book"))
        self.txtEditBookCode.setPlaceholderText(_translate("MainWindow", "Enter Book Code"))
        self.cmbBoxEditAuthor.setCurrentText(_translate("MainWindow", "Category"))
        self.cmbBoxEditAuthor.setItemText(0, _translate("MainWindow", "Category"))
        self.txtEditBookPrice.setPlaceholderText(_translate("MainWindow", "Enter Book Price"))
        self.btnBookSave.setText(_translate("MainWindow", "Save"))
        self.txtEditBookTitle.setPlaceholderText(_translate("MainWindow", "Edit Book Title"))
        self.txtEditBookDesc.setPlaceholderText(_translate("MainWindow", "Edit Book Description"))
        self.cmbBoxEditCat.setCurrentText(_translate("MainWindow", "Category"))
        self.cmbBoxEditCat.setItemText(0, _translate("MainWindow", "Category"))
        self.cmbBoxEditPublisher.setCurrentText(_translate("MainWindow", "Category"))
        self.cmbBoxEditPublisher.setItemText(0, _translate("MainWindow", "Category"))
        self.txtSearchBookTitle.setPlaceholderText(_translate("MainWindow", "Search Book Title"))
        self.btnSearchBooks.setText(_translate("MainWindow", "Search"))
        self.btnDeleteBook.setText(_translate("MainWindow", "Delete"))
        self.tabBooks.setTabText(self.tabBooks.indexOf(self.tab_6), _translate("MainWindow", "Edit or Delete Book"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_2), _translate("MainWindow", "Books"))
        self.groupBoxAddNewUsr.setTitle(_translate("MainWindow", "Add New User"))
        self.txtNewUser.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.txtNewEmail.setPlaceholderText(_translate("MainWindow", "Email"))
        self.txtNewPasswd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.txtNewPasswdAgain.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.btnRegister.setText(_translate("MainWindow", "Register"))
        self.groupBoxEditInfo.setTitle(_translate("MainWindow", "Edit User Info"))
        self.txtUpdateUser.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.txtUpdatePasswd.setPlaceholderText(_translate("MainWindow", "Password"))
        self.txtUpdateEmail.setPlaceholderText(_translate("MainWindow", "Email"))
        self.txtUpdateConfirmPasswd.setPlaceholderText(_translate("MainWindow", "Confirm Password"))
        self.btnUpdateUser.setText(_translate("MainWindow", "Update"))
        self.txtUserLogin.setPlaceholderText(_translate("MainWindow", "User Name"))
        self.txtPasswdLogin.setPlaceholderText(_translate("MainWindow", "Password"))
        self.btnLogin.setText(_translate("MainWindow", "Login"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_3), _translate("MainWindow", "Users"))
        item = self.tableCategory.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Category"))
        self.txtAddNewCategory.setPlaceholderText(_translate("MainWindow", "Enter New Category Name"))
        self.btnAddCategory.setText(_translate("MainWindow", "Add"))
        self.tabSubSettings.setTabText(self.tabSubSettings.indexOf(self.tab_7), _translate("MainWindow", "Categories"))
        item = self.tableAuthor.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author"))
        self.txtAddNewAuthor.setPlaceholderText(_translate("MainWindow", "Enter New Author Name"))
        self.btnAddAuthor.setText(_translate("MainWindow", "Add"))
        self.tabSubSettings.setTabText(self.tabSubSettings.indexOf(self.tab_8), _translate("MainWindow", "Author"))
        item = self.tablePublisher.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Publisher"))
        self.txtAddNewPublisher.setPlaceholderText(_translate("MainWindow", "Enter New Publisher Name"))
        self.btnAddPublisher.setText(_translate("MainWindow", "Add"))
        self.tabSubSettings.setTabText(self.tabSubSettings.indexOf(self.tab_9), _translate("MainWindow", "Publisher"))
        self.mainTab.setTabText(self.mainTab.indexOf(self.tab_4), _translate("MainWindow", "Settings"))
        self.btnLightTheme.setText(_translate("MainWindow", "Light Theme"))
        self.btnDarkTheme.setText(_translate("MainWindow", "Dark Theme"))
        self.label_3.setText(_translate("MainWindow", "Apply a new Theme"))


def main():
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    window = Ui_MainWindow()
    window.setupUi(mainWindow)
    mainWindow.show()
    app.exec()


if __name__ == '__main__':
    main()