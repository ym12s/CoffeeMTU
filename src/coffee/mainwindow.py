import sys
import json
<<<<<<< HEAD
sys.stdout.reconfigure(encoding="utf-8")
from PySide6.QtWidgets import (QMainWindow, QButtonGroup)
from PySide6.QtGui import QIcon
from src.__ui.ui_mainwindow import Ui_MainWindow
=======
import os
import faulthandler
import subprocess
import sqlite3
faulthandler.enable()
subprocess.run(["pyside6-uic", "src/__ui/form.ui", "-o", "src/__ui/ui_mainwindow.py"], check=True)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
sys.stdout.reconfigure(encoding="utf-8")
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QButtonGroup, QLabel, QWidget,
                                QLineEdit,  QGraphicsDropShadowEffect,
                                QInputDialog, QMessageBox
                                )
from PySide6.QtGui import QIcon, QPixmap, QAction, QPainter, QPainterPath, QColor
from PySide6.QtCore import QSize, Qt, QTimer
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from datetime import datetime 
from src.__ui.ui_mainwindow import Ui_MainWindow
from src.coffee.Ym12 import ym12s
from src.coffee.Ym12Circle import ym12c
from src.YAi import yai
from src.coffee.YSql import get_connection, DB_PATH
>>>>>>> 078f5ca (Test)

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
<<<<<<< HEAD
        self.setWindowIcon(QIcon("src/__ass/icon.ico"))
        self.setWindowTitle("Quản lí cà phê")

        self.load_styles()  # Gọi đúng hàm

        self.buttons = [self.ui.btnHome, self.ui.btnMenu,
                        self.ui.btnDonHang, self.ui.btnKho,
                        self.ui.btnNhanvien, self.ui.btnKhachHang, self.ui.btnOder]
=======
        self.resize(1260,820)
        self.timer = QTimer()
        QTimer.singleShot(100, self.formload)
        self.setWindowTitle("Quản lí cà phê")  
        
        
        
        self.matkhau = "123"
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(DB_PATH)
        self.database.open()
        
        self.loadMenu()
        self.shadowWidget()
        self.btnClick()
        self.loadDataBase()
        
        self.ui.comboBoxDB.currentTextChanged.connect(self.loadTable) 
        
        # self.timer.timeout.connect(self.smScroll)
        # self.autoScroll()
        # self.diemSrcoll = 0
       
    def autoScroll(self):
        self.diemSrcoll = self.ui.scrollMenu.verticalScrollBar().value()
        self.timer.start(2) 
    def smScroll(self):
        scrollbar = self.ui.scrollMenu.verticalScrollBar()
        scrollbarMax = scrollbar.maximum()

        if self.diemSrcoll <  scrollbarMax:
            self.diemSrcoll += 0.1
            scrollbar.setValue(self.diemSrcoll)
        else:
            self.timer.stop()    
    def AIRespone(self):
        self.user_message = self.ui.textEdit.toPlainText().strip()
        if not self.user_message:
            return

        self.ui.textEdit.append(f"Bạn: {self.user_message}")
        self.ui.textEdit.clear()

        self.thread = yai(self.user_message)
        self.thread.response_signal.connect(self.display_response)
        self.thread.start()
    def AIDisplay(self, response):
        self.ui.textEdit_2.append(f"AI: {response}")
        self.uitextEdit_2.append("Theo dõi Facebook của Khang tại: https://www.facebook.com/nilah.2004")
    def formload (self):
        
        self.ui.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.centralwidget.layout().setSpacing(0)
        self.buttons = [self.ui.btnMenu, self.ui.btnContart,
                        self.ui.btnCart, self.ui.btnAI]
>>>>>>> 078f5ca (Test)
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)
        for btn in self.buttons:
            btn.setCheckable(True)
            self.buttonGroup.addButton(btn)
<<<<<<< HEAD
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

=======
        self.buttons[0].setChecked(True)
        self.buttons[0].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))  
        self.buttons[1].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))  
        self.buttons[2].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))  
        self.buttons[3].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3)) 
        
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            if btn:
                btn.clicked.connect(self.btnClick)
        self.ui.btnXGH.clicked.connect(self.xoagiohang)    
    def xacnhanMK(self, topLeft, bottomRight, roles):
        kq, ok = QInputDialog.getText(self, "Xác nhận", "Nhập mật khẩu để chỉnh sửa:", QLineEdit.Password)
        if ok and kq == self.password:
            QMessageBox.information(self, "Thành công", "Bạn có thể chỉnh sửa dữ liệu.")
        else:
            QMessageBox.warning(self, "Sai mật khẩu", "Không thể chỉnh sửa!")
            self.model.revertAll() 
    def loadDataBase(self):
       query = self.database.exec("SELECT name FROM sqlite_master WHERE type='table'")
       tbls = []
       while query.next():
            tbls.append(query.value(0))
            
       self.ui.comboBoxDB.addItems(tbls)
       
       if tbls:
          self.loadTable(tbls[0])    
    def loadTable(self, tblDB):
        self.modes = None
        if tblDB:
            self.models = QSqlTableModel(self, self.database)
            self.models.setTable(tblDB)
            #return
            self.models.select()
            self.models.dataChanged.connect(self.xacnhanMK)
            self.ui.tblDB.setModel(self.models)
    
    def btnClick(self) -> None:
        btn = self.sender()
        if not btn:
            return
        btnName = btn.objectName()
        idMon = int(btnName.replace("btnAdd", ""))

        conn = get_connection()
        tro = conn.cursor()
        tro.execute("SELECT idMon, hinhAnh, tenMon, giaMon FROM tb_Mon WHERE idMon = ?", (idMon,))
        row = tro.fetchone()
        conn.close()

        if not row:
            return
        idMon, hinhAnh, tenMon, giaMon = row
        if not hinhAnh:
            return
        for i in range(1,16):
            lblName  = f'lbname{i}'
            lbname = getattr(self.ui, lblName, None)
            
            lblGia   = f'lbgia{i}'
            lbgia  = getattr(self.ui, lblGia,None)

            pwg = f'pwg{i}'
            widget = getattr(self.ui, pwg, None)

            if widget is None:
                continue
            
            if not hasattr(widget, "daCoAnh"):
                widget.daCoAnh = False
                
            if not hasattr(widget, "ImgID"):
                widget.ImgID = None

            if widget.ImgID == idMon:
                return
            
            if not widget.daCoAnh and widget.ImgID != idMon:
                lable = ym12c(hinhAnh,widget)
                lable.setGeometry(0,0,lable.parent().width(),lable.parent().height())
                lable.parent().resizeEvent = self.capNhatSizeAnh
                lbname.setText("Món: "+tenMon)
                lbgia.setText("Đơn giá: "+str(giaMon))
                widget.daCoAnh = True
                widget.ImgID = idMon
                break
    def xoagiohang (self):
        for i in range(1, 16):
            pwb = f'pwg{i}'
            lbl  = f'lbname{i}' 
            lblGia   = f'lbgia{i}'
            lbgia  = getattr(self.ui, lblGia,None) 
            lbname = getattr(self.ui, lbl, None)
            widget = getattr(self.ui, pwb, None)
            
            if widget:
                widget.daCoAnh = False
                widget.ImgID = None

                for j in widget.findChildren(QWidget):
                    j.deleteLater()
            if lbname:
                lbname.setText("")
                lbgia.setText("")
    def shadowWidget(self):
        
        self.a = []  
        wG = [ self.ui.wg1, self.ui.wg2, 
               self.ui.wg3, self.ui.wg4, self.ui.wg5
               , self.ui.wg6, self.ui.wg7, self.ui.wg8
               , self.ui.wg9, self.ui.wg10, self.ui.wg11,
               self.ui.wg12,self.ui.wg13,self.ui.wg14,self.ui.wg15,
               self.ui.pwg1,self.ui.pwg2,self.ui.pwg3,
               self.ui.pwg4,self.ui.pwg5,self.ui.pwg6,
               self.ui.pwg7,self.ui.pwg8,self.ui.pwg9,
               self.ui.pwg10,self.ui.pwg11,self.ui.pwg12,
               self.ui.pwg13,self.ui.pwg14,self.ui.pwg15
               ]
        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(3)
        shadow1.setXOffset(5)
        shadow1.setYOffset(0)
        shadow1.setColor(QColor(0,0,0,180))
        self.ui.WgPWG.setGraphicsEffect(shadow1)
        for j in wG:
            shadow = QGraphicsDropShadowEffect()
            shadow.setBlurRadius(10)
            shadow.setXOffset(0)
            shadow.setYOffset(0)
            shadow.setColor(QColor(0, 0, 0, 180))
            j.setGraphicsEffect(shadow)
            self.a.append(shadow)
    def loadMenu(self):
        conn = get_connection()
        tro  = conn.cursor()
        tro.execute("SELECT tenMon, hinhAnh From tb_Mon")
        dataMenu = tro.fetchall()
        conn.close()
        self.lbMenu = {}
        self.lblMenu = []
        for ind, (tenMon, hinhAnh) in enumerate(dataMenu, start=1):
            lbName = f"lblCost{ind}"
            wgName = f"wb{ind}"
            lbCost = getattr(self.ui, lbName,None)
            wb     = getattr(self.ui,wgName,None ) 
            if lbCost:
               self.lbMenu[ind] = lbCost
               self.lbMenu[ind].setText(tenMon) 
            if hasattr(self.ui,wgName):
                label = ym12s(hinhAnh,wb)
                label.setGeometry(0, 0, label.parent().width(), label.parent().height())
                label.parent().resizeEvent = self.capNhatSizeAnh         
                self.lblMenu.append(label)
                       
        #       
    def capNhatSizeAnh(self, event):
        for i in self.lblMenu:
            i.setGeometry(0, 0, i.parent().width(), i.parent().height())    
    def resizeEvent(self, event):
        super().resizeEvent(event)
    def loadCSS(self):
        try:
            with open("src/__ui/style.json", "r", encoding="utf-8") as f:
                styles = json.load(f)
            for widget, rules in styles.get("widgetStyles", {}).items():
                self.applyStyles(widget, rules)
        
            for label, rules in styles.get("labelStyles", {}).items():
                self.applyStyles(label, rules)
            
            for button, rules in styles.get("buttonStyles", {}).items():
                self.applyStyles( button, rules)
        except Exception as e:
            print("Lỗi khi load CSS:", e)
        print(f"Read file CSS: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")  
        
>>>>>>> 078f5ca (Test)
