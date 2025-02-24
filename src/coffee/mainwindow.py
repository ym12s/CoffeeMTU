import sys
import json
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.stdout.reconfigure(encoding="utf-8")
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QButtonGroup, QLabel, QWidget,
                                QLineEdit, QVBoxLayout,
                                QGraphicsScene, QGraphicsPixmapItem, QGraphicsView)
from PySide6.QtGui import QIcon, QPixmap, QAction, QPainter, QPainterPath
from PySide6.QtCore import QSize, Qt, QTimer
from src.__ui.ui_mainwindow import Ui_MainWindow
from src.coffee.Ym12 import ym12s


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowIcon(QIcon("src/__ass/icon.ico"))
        self.setWindowTitle("Quản lí cà phê")
        
        QTimer.singleShot(0, self.update_button_position)
        self.add_images()
    def add_images(self):
        print(f"✅ self.menuWidget: {self.ui.menuWidget}")  # Debug kiểm tra
        image_dir = os.path.join(os.getcwd(), "src", "ass")
        for i in range(10):
            image_path = os.path.join(image_dir, f"name{i+1}.png")
            print(f"Loading image: {image_path}")

            pixmap = QPixmap(image_path)
            if pixmap.isNull():
                print(f"Không thể load ảnh: {image_path}")
                continue

            label = QLabel(self.ui.menuWidget)
            label.setPixmap(pixmap.scaled(100, 100))
            label.setFixedSize(100, 100)
            label.move(i * 110, 0)

                
        self.anh = [ym12s("src/__ass/ym12.png", self.ui.test),
                    ym12s("src/__ass/matcha.jpg", self.ui.test1),
                    ym12s("src/__ass/cf.jpg", self.ui.test2)]
        for i in self.anh:
            i.setGeometry(0, 0, i.parent().width(), i.parent().height())
        self.ui.test.resizeEvent = self.update_image_size
        self.ui.test1.resizeEvent = self.update_image_size
        self.ui.test2.resizeEvent = self.update_image_size
        
        self.move_widget_up(10)
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
        
    def resizeEvent(self, event):
        self.update_button_position()
        super().resizeEvent(event)

    def update_button_position(self):
        panelLeftW = self.ui.paneleft.width()
        panelLeftH = self.ui.paneleft.height()

        panelMidW = self.ui.panelMidM.width()
        panelMidH= self.ui.panelMidM.height()

        btnHelpW = self.ui.btnHelp.width()
        btnHelpH = self.ui.btnHelp.height()

        btnPlayW = self.ui.btnPlay.width()
        btnPlayH = self.ui.btnPlay.height()
        
        x1 = (panelLeftW - btnHelpW) // 2  
        y1 = panelLeftH - btnHelpH - 10  # Cách bottom 10px
        self.ui.btnHelp.move(x1, y1)

        x2 = (panelMidW - btnPlayW) - 5 
        y2 = (panelMidH - btnPlayH) // 1  # Đặt giữa panelMidM
        self.ui.btnPlay.move(x2, y2)
        
        
    def move_widget_up(self, offset=10):
        x, y, w, h = self.ui.test.geometry().getRect() 
        self.ui.test.setGeometry(x, y - offset, w, h)      
        
    def update_image_size(self, event):
        for i in self.anh:
            i.setGeometry(0, 0, i.parent().width(), i.parent().height())


    def load_styles(self):
        try:
            with open("src/__ui/style.json", "r", encoding="utf-8") as f:
                styles = json.load(f)
                css = "\n".join([f"{selector} {{ {rules} }}" for selector, rules in styles.items()])
                self.setStyleSheet(css)
        except Exception as e:
            print("Lỗi khi load CSS:", e)
