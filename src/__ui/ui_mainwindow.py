# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QButtonGroup, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLayout, QLineEdit,
    QMainWindow, QPushButton, QScrollArea, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 932)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.paneleft = QWidget(self.centralwidget)
        self.paneleft.setObjectName(u"paneleft")
        self.paneleft.setMinimumSize(QSize(260, 0))
        self.paneleft.setMaximumSize(QSize(260, 16777215))
        self.paneleft.setStyleSheet(u"background-color: rgb(33, 33, 45);")
        self.panelTitle = QWidget(self.paneleft)
        self.panelTitle.setObjectName(u"panelTitle")
        self.panelTitle.setGeometry(QRect(9, 9, 242, 80))
        self.panelTitle.setMaximumSize(QSize(16777215, 80))
        self.lblCoffee = QLabel(self.panelTitle)
        self.lblCoffee.setObjectName(u"lblCoffee")
        self.lblCoffee.setGeometry(QRect(80, 20, 61, 31))
        font = QFont()
        font.setFamilies([u"VfFree30"])
        font.setPointSize(18)
        font.setBold(False)
        font.setItalic(False)
        self.lblCoffee.setFont(font)
        self.lblCoffee.setStyleSheet(u"color: white;")
        self.lblCoffee.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee.setScaledContents(False)
        self.lblCoffee.setWordWrap(False)
        self.lblCoffee.setOpenExternalLinks(False)
        self.btnHelp = QPushButton(self.paneleft)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btnHelp)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setGeometry(QRect(0, 790, 261, 51))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        self.btnHelp.setFont(font1)
        self.btnHelp.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: rgb(64, 65, 66); \n"
"    color: white; \n"
"	 text-align: left;\n"
"    font-size: 18px;\n"
"	padding-left: 25px;\n"
"	border-radius: 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: black;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.btnHelp.setIconSize(QSize(20, 20))
        self.btnPay = QPushButton(self.paneleft)
        self.buttonGroup.addButton(self.btnPay)
        self.btnPay.setObjectName(u"btnPay")
        self.btnPay.setGeometry(QRect(0, 360, 261, 51))
        self.btnPay.setFont(font1)
        self.btnPay.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white; \n"
"    text-align: left;\n"
"    font-size: 18px;\n"
"    padding-left: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(46, 47, 48);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"\n"
"    color: white;\n"
"    border-left: 2px solid rgb(239, 50, 104);\n"
"}\n"
"")
        self.btnPay.setIconSize(QSize(20, 20))
        self.btnRefresh = QPushButton(self.paneleft)
        self.buttonGroup.addButton(self.btnRefresh)
        self.btnRefresh.setObjectName(u"btnRefresh")
        self.btnRefresh.setGeometry(QRect(0, 290, 261, 51))
        self.btnRefresh.setFont(font1)
        self.btnRefresh.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white; \n"
"    text-align: left;\n"
"    font-size: 18px;\n"
"    padding-left: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(46, 47, 48);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"\n"
"    color: white;\n"
"    border-left: 2px solid rgb(239, 50, 104);\n"
"}\n"
"")
        icon = QIcon()
        icon.addFile(u"../__ass/card.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btnRefresh.setIcon(icon)
        self.btnRefresh.setIconSize(QSize(20, 20))
        self.btnMenu = QPushButton(self.paneleft)
        self.buttonGroup.addButton(self.btnMenu)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(0, 220, 251, 51))
        self.btnMenu.setFont(font1)
        self.btnMenu.setStyleSheet(u"QPushButton {\n"
"    background-color: transparent;\n"
"    border: none;\n"
"    color: white; \n"
"    text-align: left;\n"
"    font-size: 18px;\n"
"    padding-left: 25px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(46, 47, 48);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:checked {\n"
"\n"
"    color: white;\n"
"    border-left: 2px solid rgb(239, 50, 104);\n"
"}\n"
"")
        self.btnMenu.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.paneleft)

        self.panelMid = QWidget(self.centralwidget)
        self.panelMid.setObjectName(u"panelMid")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.panelMid.sizePolicy().hasHeightForWidth())
        self.panelMid.setSizePolicy(sizePolicy)
        self.panelMid.setMinimumSize(QSize(650, 0))
        self.panelMid.setMaximumSize(QSize(16777215, 16777215))
        self.panelMid.setStyleSheet(u"background-color: rgb(250, 250, 250);")
        self.verticalLayout_3 = QVBoxLayout(self.panelMid)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.panelMenu = QFrame(self.panelMid)
        self.panelMenu.setObjectName(u"panelMenu")
        sizePolicy.setHeightForWidth(self.panelMenu.sizePolicy().hasHeightForWidth())
        self.panelMenu.setSizePolicy(sizePolicy)
        self.panelMenu.setMinimumSize(QSize(700, 0))
        self.panelMenu.setMaximumSize(QSize(1000, 16777215))
        self.panelMenu.setStyleSheet(u"background-color: rgb(235, 235, 235);\n"
"border-radius:0px;")
        self.verticalLayout_4 = QVBoxLayout(self.panelMenu)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget = QWidget(self.panelMenu)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setMinimumSize(QSize(650, 350))
        self.widget.setMaximumSize(QSize(16777215, 16777215))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.panelTimKiem = QWidget(self.widget)
        self.panelTimKiem.setObjectName(u"panelTimKiem")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.panelTimKiem.sizePolicy().hasHeightForWidth())
        self.panelTimKiem.setSizePolicy(sizePolicy1)
        self.panelTimKiem.setMinimumSize(QSize(600, 70))
        self.panelTimKiem.setMaximumSize(QSize(16777215, 70))
        self.panelTimKiem.setStyleSheet(u"background-color: Transparent;\n"
"")
        self.txtTimKiem = QLineEdit(self.panelTimKiem)
        self.txtTimKiem.setObjectName(u"txtTimKiem")
        self.txtTimKiem.setGeometry(QRect(20, 15, 551, 41))
        self.txtTimKiem.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"color: black;\n"
"font-size: 15px;\n"
"\n"
"\n"
"")
        self.pushButton = QPushButton(self.panelTimKiem)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(490, 15, 81, 41))
        self.pushButton.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(239, 50, 104);\n"
"border-radius: 10px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.lblCoffee_4 = QLabel(self.panelTimKiem)
        self.lblCoffee_4.setObjectName(u"lblCoffee_4")
        self.lblCoffee_4.setGeometry(QRect(50, 12, 309, 41))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lblCoffee_4.sizePolicy().hasHeightForWidth())
        self.lblCoffee_4.setSizePolicy(sizePolicy2)
        font2 = QFont()
        font2.setFamilies([u"UVN Bai Sau"])
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setItalic(True)
        self.lblCoffee_4.setFont(font2)
        self.lblCoffee_4.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"text-align: center;")
        self.lblCoffee_4.setTextFormat(Qt.TextFormat.PlainText)
        self.lblCoffee_4.setScaledContents(False)
        self.lblCoffee_4.setWordWrap(False)
        self.lblCoffee_4.setOpenExternalLinks(False)

        self.verticalLayout_2.addWidget(self.panelTimKiem)

        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy)
        self.widget_3.setMinimumSize(QSize(0, 250))
        self.widget_3.setMaximumSize(QSize(16777215, 150))
        self.widget_3.setSizeIncrement(QSize(0, 0))
        self.widget_3.setBaseSize(QSize(0, 0))
        self.widget_3.setStyleSheet(u"background-color: rgb(29, 30, 34);\n"
"border-radius: 15px;")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(9, 9, 9, 9)
        self.test = QWidget(self.widget_3)
        self.test.setObjectName(u"test")
        sizePolicy.setHeightForWidth(self.test.sizePolicy().hasHeightForWidth())
        self.test.setSizePolicy(sizePolicy)
        self.test.setMinimumSize(QSize(200, 232))
        self.test.setMaximumSize(QSize(288, 232))
        self.test.setStyleSheet(u"")

        self.horizontalLayout_3.addWidget(self.test)

        self.panelMidM = QWidget(self.widget_3)
        self.panelMidM.setObjectName(u"panelMidM")
        self.label_2 = QLabel(self.panelMidM)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 10, 311, 41))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(12)
        font3.setBold(True)
        font3.setHintingPreference(QFont.PreferFullHinting)
        self.label_2.setFont(font3)
        self.btnPlay = QPushButton(self.panelMidM)
        self.btnPlay.setObjectName(u"btnPlay")
        self.btnPlay.setGeometry(QRect(280, 180, 81, 41))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.btnPlay.sizePolicy().hasHeightForWidth())
        self.btnPlay.setSizePolicy(sizePolicy3)
        self.btnPlay.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btnPlay.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(239, 50, 104);\n"
"border-radius: 10px;\n"
"color: black;\n"
"}\n"
"QPushButton:hover{\n"
"background-color: rgb(239, 50, 104); \n"
"    color: white;\n"
"}\n"
"QPushButton:checked{\n"
" background-color: rgb(239, 50, 104);\n"
" color: white;\n"
"}")
        self.label_3 = QLabel(self.panelMidM)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 50, 401, 41))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setHintingPreference(QFont.PreferFullHinting)
        self.label_3.setFont(font4)

        self.horizontalLayout_3.addWidget(self.panelMidM)


        self.verticalLayout_2.addWidget(self.widget_3, 0, Qt.AlignmentFlag.AlignTop)

        self.widget_3.raise_()
        self.panelTimKiem.raise_()

        self.verticalLayout_4.addWidget(self.widget)

        self.menuMain = QWidget(self.panelMenu)
        self.menuMain.setObjectName(u"menuMain")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.menuMain.sizePolicy().hasHeightForWidth())
        self.menuMain.setSizePolicy(sizePolicy4)
        self.menuMain.setMinimumSize(QSize(0, 250))
        self.menuMain.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.menuMain)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self.menuMain)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 682, 2410))
        self.gridLayout = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName(u"gridLayout")
        self.menuWidget = QWidget(self.scrollAreaWidgetContents)
        self.menuWidget.setObjectName(u"menuWidget")
        self.verticalLayout = QVBoxLayout(self.menuWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.test8 = QWidget(self.menuWidget)
        self.test8.setObjectName(u"test8")
        self.test8.setMinimumSize(QSize(288, 232))
        self.test8.setMaximumSize(QSize(288, 232))
        self.test8.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.test8)

        self.test9 = QWidget(self.menuWidget)
        self.test9.setObjectName(u"test9")
        self.test9.setMinimumSize(QSize(288, 232))
        self.test9.setMaximumSize(QSize(288, 232))
        self.test9.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.test9)

        self.test10 = QWidget(self.menuWidget)
        self.test10.setObjectName(u"test10")
        self.test10.setMinimumSize(QSize(288, 232))
        self.test10.setMaximumSize(QSize(288, 232))
        self.test10.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.test10)

        self.test2 = QWidget(self.menuWidget)
        self.test2.setObjectName(u"test2")
        self.test2.setMinimumSize(QSize(288, 232))
        self.test2.setMaximumSize(QSize(288, 232))
        self.test2.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.test2)

        self.test7 = QWidget(self.menuWidget)
        self.test7.setObjectName(u"test7")
        self.test7.setMinimumSize(QSize(288, 232))
        self.test7.setMaximumSize(QSize(288, 232))
        self.test7.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.test7)

        self.test4 = QWidget(self.menuWidget)
        self.test4.setObjectName(u"test4")
        self.test4.setMinimumSize(QSize(288, 232))
        self.test4.setMaximumSize(QSize(288, 232))
        self.test4.setStyleSheet(u"background-color: rgb(255, 185, 242);")

        self.verticalLayout.addWidget(self.test4)

        self.test5 = QWidget(self.menuWidget)
        self.test5.setObjectName(u"test5")
        self.test5.setMinimumSize(QSize(288, 232))
        self.test5.setMaximumSize(QSize(288, 232))
        self.test5.setStyleSheet(u"background-color: rgb(255, 185, 242);")

        self.verticalLayout.addWidget(self.test5)

        self.test6 = QWidget(self.menuWidget)
        self.test6.setObjectName(u"test6")
        self.test6.setMinimumSize(QSize(288, 232))
        self.test6.setMaximumSize(QSize(288, 232))
        self.test6.setStyleSheet(u"background-color: rgb(255, 185, 242);")

        self.verticalLayout.addWidget(self.test6)

        self.test1 = QWidget(self.menuWidget)
        self.test1.setObjectName(u"test1")
        self.test1.setMinimumSize(QSize(288, 232))
        self.test1.setMaximumSize(QSize(288, 232))
        self.test1.setStyleSheet(u"background-color: rgb(255, 185, 242);")

        self.verticalLayout.addWidget(self.test1)

        self.test3 = QWidget(self.menuWidget)
        self.test3.setObjectName(u"test3")
        self.test3.setMinimumSize(QSize(288, 232))
        self.test3.setMaximumSize(QSize(288, 232))
        self.test3.setStyleSheet(u"background-color: rgb(255, 185, 242);")

        self.verticalLayout.addWidget(self.test3)


        self.gridLayout.addWidget(self.menuWidget, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.horizontalLayout_2.addWidget(self.scrollArea)


        self.verticalLayout_4.addWidget(self.menuMain)

        self.widget_8 = QWidget(self.panelMenu)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setMinimumSize(QSize(0, 0))
        self.widget_8.setMaximumSize(QSize(0, 16777215))
        self.widget_8.setStyleSheet(u"background-color: rgb(249, 244, 255);")

        self.verticalLayout_4.addWidget(self.widget_8)


        self.verticalLayout_3.addWidget(self.panelMenu)


        self.horizontalLayout.addWidget(self.panelMid)

        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy2.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy2)
        self.widget_2.setMinimumSize(QSize(300, 0))
        self.widget_2.setMaximumSize(QSize(300, 16777215))
        self.widget_2.setStyleSheet(u"background-color: rgb(247, 249, 255);")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")

        self.horizontalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblCoffee.setText(QCoreApplication.translate("MainWindow", u"MTU", None))
        self.btnHelp.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.btnPay.setText(QCoreApplication.translate("MainWindow", u"Refresh", None))
        self.btnRefresh.setText(QCoreApplication.translate("MainWindow", u"Pay", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Search", None))
        self.lblCoffee_4.setText(QCoreApplication.translate("MainWindow", u"C\u00e0 ph\u00ea \u0111\u1eadm \u2013 debug ch\u1eadm c\u0169ng th\u00e0nh nhanh!", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"H\u00c3Y CHO CON CH\u1ecaU \u0110AU KH\u1ed4 THAY EM", None))
        self.btnPlay.setText(QCoreApplication.translate("MainWindow", u"PLAY", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Lil Liem & ekkososa (feat. Kewwi, KIDDI) x Kidsai x Eren Ver", None))
    # retranslateUi

