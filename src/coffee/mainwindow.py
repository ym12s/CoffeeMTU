import sys
import json
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.stdout.reconfigure(encoding="utf-8")
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QButtonGroup, QLabel, QWidget,
                                QLineEdit, QVBoxLayout, QHBoxLayout
                                )
from PySide6.QtGui import QIcon, QPixmap, QAction, QPainter, QPainterPath
from PySide6.QtCore import QSize, Qt, QTimer
from src.__ui.ui_mainwindow import Ui_MainWindow
from src.coffee.Ym12 import ym12s

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("Quản lí cà phê")  
        QTimer.singleShot(5, self.diChuyenBtn)
        self.formload()
        self.themAnh()
    def formload (self):
        self.anh = ym12s("src/__ass/ym12.png", self.ui.test)
        self.anh.setGeometry(0, 0, self.ui.test.width(), self.ui.test.height())
        
        self.ui.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.centralwidget.layout().setSpacing(0)
        self.ui.panelMid.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.panelMid.layout().setSpacing(0)
        search_action = QAction(QIcon("src/__ass/search.png"), "", self)
        self.ui.txtTimKiem.addAction(search_action, QLineEdit.ActionPosition.LeadingPosition)
        self.ui.btnMenu.setIcon(QIcon("src/__ass/menu-button-white.png"))
        self.ui.btnMenu.setIconSize(QSize(20, 20))
        self.ui.btnPay.setIcon(QIcon("src/__ass/refresh-buttons-white.png"))
        self.ui.btnPay.setIconSize(QSize(20, 20))
        self.ui.btnRefresh.setIcon(QIcon("src/__ass/card-White.png"))
        self.ui.btnRefresh.setIconSize(QSize(20, 20))
        self.ui.btnHelp.setIcon(QIcon("src/__ass/help-web-button.png"))
        self.ui.btnHelp.setIconSize(QSize(20, 20))

        self.buttons = [self.ui.btnMenu, self.ui.btnRefresh,
                        self.ui.btnPay, self.ui.btnHelp]

        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)
        for btn in self.buttons:
            btn.setCheckable(True)
            self.buttonGroup.addButton(btn)
        self.buttons[0].setChecked(True)
    def themAnh(self):
        anhFolder = os.path.join(os.getcwd(), "src", "ass")
        self.anh = []
        for i in range(10):
            dcAnh = os.path.join(anhFolder, f"name{i+1}.png")
            print(f"Ảnh thứ [{i+1}] tải lên 100%")

            if not os.path.exists(dcAnh):
                print(f"Không tìm thấy ảnh tại: {dcAnh}")
                continue

            widgetAnh = f'test{i+1}'
            if not hasattr(self.ui, widgetAnh):
                print(f"Không tìm thấy widget: {widgetAnh}")
                continue

            pixmap = QPixmap(dcAnh)
            if pixmap.isNull():
                print(f"Không thể tải ảnh tại: {dcAnh}")
                continue

            label = ym12s(dcAnh, getattr(self.ui, widgetAnh))
            label.setGeometry(0, 0, label.parent().width(), label.parent().height())
            label.parent().resizeEvent = self.capNhatSizeAnh
            self.anh.append(label)
    def resizeEvent(self, event):
        self.diChuyenBtn()
        super().resizeEvent(event)
    def diChuyenBtn(self):
        panelLeftW = self.ui.paneleft.width()
        panelLeftH = self.ui.paneleft.height()

        panelMidW = self.ui.panelMidM.width()
        panelMidH= self.ui.panelMidM.height()

        btnHelpW = self.ui.btnHelp.width()
        btnHelpH = self.ui.btnHelp.height()

        btnPlayW = self.ui.btnPlay.width()
        btnPlayH = self.ui.btnPlay.height()
        
        x1 = (panelLeftW - btnHelpW) // 2  
        y1 = panelLeftH - btnHelpH - 10 
        self.ui.btnHelp.move(x1, y1)

        x2 = (panelMidW - btnPlayW) - 5 
        y2 = (panelMidH - btnPlayH) // 1 
        self.ui.btnPlay.move(x2, y2)    
    def capNhatSizeAnh(self, event):
        for i in self.anh:
            i.setGeometry(0, 0, i.parent().width(), i.parent().height())
    def loadCSS(self):
        try:
            with open("src/__ui/style.json", "r", encoding="utf-8") as f:
                styles = json.load(f)
                css = "\n".join([f"{selector} {{ {rules} }}" for selector, rules in styles.items()])
                self.setStyleSheet(css)
        except Exception as e:
            print("Lỗi khi load CSS:", e)