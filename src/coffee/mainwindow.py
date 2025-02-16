import sys
from PySide6.QtWidgets import (QMainWindow, QFrame,
                               QVBoxLayout, QWidget,
                               QGraphicsDropShadowEffect, QButtonGroup)
from PySide6.QtGui import QColor, QIcon
from __ui.ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("anh/icon.png"))
        self.setWindowTitle("Quản lí cà phê")

        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(5)
        self.shadow.setYOffset(5)
        self.shadow.setColor(QColor(0, 0, 0, 180))
        self.ui.frame.setGraphicsEffect(self.shadow)
        self.buttons = [self.ui.btnHome, self.ui.btnMenu,
                        self.ui.btnDonHang, self.ui.btnKho,
                        self.ui.btnNhanvien, self.ui.btnKhachHang, self.ui.btnOder]
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)
        for btn in self.buttons:
            btn.setCheckable(True)
            self.buttonGroup.addButton(btn)
            self.buttons[0].setChecked(False)

