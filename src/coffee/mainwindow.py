import sys
import json
sys.stdout.reconfigure(encoding="utf-8")
from PySide6.QtWidgets import (QMainWindow, QButtonGroup)
from PySide6.QtGui import QIcon
from src.__ui.ui_mainwindow import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/__ass/icon.ico"))
        self.setWindowTitle("Quản lí cà phê")

        self.load_styles()  # Gọi đúng hàm

        self.buttons = [self.ui.btnHome, self.ui.btnMenu,
                        self.ui.btnDonHang, self.ui.btnKho,
                        self.ui.btnNhanvien, self.ui.btnKhachHang, self.ui.btnOder]
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)
        for btn in self.buttons:
            btn.setCheckable(True)
            self.buttonGroup.addButton(btn)
        self.buttons[0].setChecked(False)

    def load_styles(self):
        try:
            with open("src/__ui/style.json", "r", encoding="utf-8") as f:
                styles = json.load(f)
                css = "\n".join([f"{selector} {{ {rules} }}" for selector, rules in styles.items()])
                self.setStyleSheet(css)
        except Exception as e:
            print("Lỗi khi load CSS:", e)


            # self.shadow = QGraphicsDropShadowEffect()
            # self.shadow.setBlurRadius(20)
            # self.shadow.setXOffset(5)
            # self.shadow.setYOffset(5)
            # self.shadow.setColor(QColor(0, 0, 0, 180))
            # self.ui.frame.setGraphicsEffect(self.shadow)

