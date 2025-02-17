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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QMainWindow, QPushButton,
    QSizePolicy, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1270, 768)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: white;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.btnHome = QPushButton(self.centralwidget)
        self.buttonGroup = QButtonGroup(MainWindow)
        self.buttonGroup.setObjectName(u"buttonGroup")
        self.buttonGroup.addButton(self.btnHome)
        self.btnHome.setObjectName(u"btnHome")
        self.btnHome.setGeometry(QRect(220, 20, 101, 41))
        self.btnHome.setStyleSheet(u"")
        self.btnMenu = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnMenu)
        self.btnMenu.setObjectName(u"btnMenu")
        self.btnMenu.setGeometry(QRect(90, 20, 101, 41))
        self.btnMenu.setStyleSheet(u"")
        self.btnDonHang = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnDonHang)
        self.btnDonHang.setObjectName(u"btnDonHang")
        self.btnDonHang.setGeometry(QRect(350, 20, 101, 41))
        self.btnDonHang.setStyleSheet(u"")
        self.btnKho = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnKho)
        self.btnKho.setObjectName(u"btnKho")
        self.btnKho.setGeometry(QRect(480, 20, 101, 41))
        self.btnKho.setStyleSheet(u"")
        self.btnNhanvien = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnNhanvien)
        self.btnNhanvien.setObjectName(u"btnNhanvien")
        self.btnNhanvien.setGeometry(QRect(610, 20, 101, 41))
        self.btnNhanvien.setStyleSheet(u"")
        self.btnKhachHang = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnKhachHang)
        self.btnKhachHang.setObjectName(u"btnKhachHang")
        self.btnKhachHang.setGeometry(QRect(740, 20, 101, 41))
        self.btnKhachHang.setStyleSheet(u"")
        self.btnOder = QPushButton(self.centralwidget)
        self.buttonGroup.addButton(self.btnOder)
        self.btnOder.setObjectName(u"btnOder")
        self.btnOder.setGeometry(QRect(870, 20, 101, 41))
        self.btnOder.setStyleSheet(u"")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(110, 170, 120, 80))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.btnHome.setText(QCoreApplication.translate("MainWindow", u"HOME", None))
        self.btnMenu.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.btnDonHang.setText(QCoreApplication.translate("MainWindow", u"\u0110\u01a0N H\u00c0NG", None))
        self.btnKho.setText(QCoreApplication.translate("MainWindow", u"KHO", None))
        self.btnNhanvien.setText(QCoreApplication.translate("MainWindow", u"NH\u00c2N VI\u00caN", None))
        self.btnKhachHang.setText(QCoreApplication.translate("MainWindow", u"KH\u00c1CH H\u00c0NG", None))
        self.btnOder.setText(QCoreApplication.translate("MainWindow", u"ORDER ONLINE", None))
    # retranslateUi

