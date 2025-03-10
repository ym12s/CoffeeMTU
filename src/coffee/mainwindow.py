import sys
import json
import os
import faulthandler
import subprocess
import sqlite3
faulthandler.enable()

COFFEE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(COFFEE_DIR, "..") 

sys.path.append(SRC_DIR)
sys.stdout.reconfigure(encoding="utf-8")

UI_FILE = os.path.join(SRC_DIR, "__ui", "ui_mainwindow.py")
if not os.path.exists(UI_FILE):
    subprocess.run(["pyside6-uic", os.path.join(SRC_DIR, "__ui", "form.ui"), "-o", UI_FILE], check=True)
from PySide6.QtWidgets import (QApplication, QMainWindow,
                                QButtonGroup, QLabel, QWidget,
                                QLineEdit,  QGraphicsDropShadowEffect,
                                QInputDialog, QMessageBox
                                )
from PySide6.QtGui import (QIcon, QPixmap, QAction, QPainter,
                            QPainterPath, QColor,QPalette)
from PySide6.QtCore import QSize, Qt, QTimer,QEasingCurve,QVariantAnimation,Signal
from PySide6.QtSql import QSqlDatabase, QSqlTableModel
from datetime import datetime 
from reportlab.pdfgen import canvas
from src.__ui.ui_mainwindow import Ui_MainWindow
print("sys.path:", sys.path)
print("Tồn tại mainwindow.py:", os.path.exists("src/coffee/mainwindow.py"))
from src.coffee.Ym12 import ym12s
from src.coffee.Ym12Circle import ym12c
from src.coffee.YAi import yai
from src.coffee.YSql import get_connection, DB_PATH
from PySide6.QtWidgets import QLineEdit

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resize(1320,820)
        self.timer = QTimer()
        QTimer.singleShot(100, self.formload)
        self.setWindowTitle("...")  
        self.giohang = []
        self.matkhau = "123"
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName(DB_PATH)
        self.database.open()
        
        self.loadMenu()
        self.shadowWidget()
        self.btnClick()
        self.loadDataBase()
        self.ui.comboBoxDB.currentTextChanged.connect(self.loadTable) 
        self.ui.btnMua_3.clicked.connect(self.thanhtoan)
        self.ui.btnAddDB.clicked.connect(self.themrowtable)
        self.ui.pushButton1.clicked.connect(self.AIRespone)

        # self.timer.timeout.connect(self.smScroll)
        # self.diemSrcoll = 0
    def kiemtralogin(self):
        username = self.ui.txtUser.text().strip()
        password = self.ui.txtPass.text().strip()
        
        users = self.login(username,password)
        if users:
             self.fullname = users[0]
             self.idNhanVien = users[1]
             for button in self.buttonGroup.buttons(): 
                button.setVisible(True)
             self.ui.wdLOGIN.setVisible(False)
             self.buttons[0].setChecked(True)
             self.ui.lblWelcome.setText(f"WELCOME {self.fullname} COFFEE MTU ❤")
            #  self.autoScroll()
        else: 
            self.setStyleSheet("""
            QMessageBox {
                background-color: #333;
                color: white;
                font-size: 14px;
            }""")
            QMessageBox.critical(self, "Thất bại", "Sai tài khoản hoặc mật khẩu!")
    def login(self, username, password):# -> Any:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT fullname,idNhanVien FROM tb_User WHERE username = ? AND password = ?"
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        conn.close()
        return user
    def tongtien(self):
        tongTien = 0
        for i in range(1, 16):
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            lblGia = getattr(self.ui, f'lbgia{i}', None)

            if spinBoxSL and lblGia:
                soluong = spinBoxSL.value()
                giaMon = self.giagoc.get(i, 0)
                tongTien += soluong * giaMon
        if self.giohang:
            self.ui.lbThanhtien_3.setText(f"{tongTien:,.0f} VND".replace(",", "."))
            return tongTien
    def hoadon(self):
        thanhTien = self.tongtien()
        
        if thanhTien == 0:
            return
        idnhanvien = self.idNhanVien
        
        conn = get_connection()
        tro = conn.cursor()
        tro.execute("""INSERT INTO tb_DonHang (idNhanVien, trangThaiDH, tongTien)
        VALUES (?, ?, ?)""",(idnhanvien, "Chờ xử lý", thanhTien))
        tro.execute("SELECT idDonHang FROM tb_DonHang ORDER BY idDonHang DESC LIMIT 1")
        self.idDonHang = tro.fetchone()[0]
        for item in self.giohang:
            if item["idMon"] == self.idMon: 
                item["soLuong"] = self.spinBoxSL.value()
                break

        for item in self.giohang:
            idMon = item["idMon"]
            giaMon = item["giaMon"]
            soLuong = item["soLuong"]
            thanhTien = soLuong * giaMon
            tro.execute("""INSERT INTO tb_ChiTietDonHang (idDonHang, idMon, soLuong, thanhTien, giaMon)
                        VALUES (?, ?, ?, ?, ?)""",
                        (self.idDonHang, idMon, soLuong, thanhTien ,giaMon))
        conn.commit()
        conn.close()
        
        self.setStyleSheet("""
            QMessageBox {
                background-color: #333;
                color: white;
                font-size: 14px;
            }""")
        QMessageBox.information(self, "Thành công", "Khởi tạo đơn hàng thành công!")
        self.ui.lbThanhtien_3.setText("0 VND")
        return self.idDonHang
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
        self.tinnhanUser = self.ui.lineEdit.text().strip()
        if not self.tinnhanUser:
            return
        self.ui.textBrowser.append(f"Bạn: {self.tinnhanUser}")
        self.ui.lineEdit.clear()

        self.thread = yai(self.tinnhanUser)
        self.thread.tinHieuPhanHoi.connect(self.AIDisplay)
        self.thread.start()

    def AIDisplay(self, phanHoi):
        txtDisplay = self.ui.textBrowser.toPlainText().split("\n")
        
        if not txtDisplay or not txtDisplay[-1].startswith("AI:"):
            self.ui.textBrowser.append(f"AI: {phanHoi}")
        else:
            txtDisplay[-1] = f"AI: {phanHoi}"
            self.ui.textBrowser.setPlainText("\n".join(txtDisplay)) 
    def formload (self):
        
        self.ui.btnLogin.clicked.connect(self.kiemtralogin)
        self.ui.lbThanhtien_3.setText("0")
        self.ui.centralwidget.layout().setContentsMargins(0, 0, 0, 0)
        self.ui.centralwidget.layout().setSpacing(0)
        self.buttons = [self.ui.btnMenu, self.ui.btnOrder,
                        self.ui.btnExit, self.ui.btnAI, self.ui.btnAdmin]
        self.buttonGroup = QButtonGroup(self)
        self.buttonGroup.setExclusive(True)

       
        for btn in self.buttons:
            btn.setCheckable(True)
            self.buttonGroup.addButton(btn)
       
        for self.button in self.buttonGroup.buttons():
            self.button.setVisible(False)
        self.buttons[0].setChecked(False)
        self.buttons[0].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))  
        self.buttons[1].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))  
        self.buttons[2].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(5))  
        self.buttons[3].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4)) 
        self.buttons[4].toggled.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2)) 
        
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            if btn:
                btn.clicked.connect(self.btnClick)
            if spinBoxSL and spinBoxSL.value() == 0:
                spinBoxSL.setVisible(False)
            
                
        self.ui.btnXGH_3.clicked.connect(self.xoagiohang)    
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
            # self.models.dataChanged.connect(self.xacnhanMK)
            self.ui.tblDB.setModel(self.models)
    def themrowtable(self):
        if not self.models:
          return
        row = self.models.rowCount()
        self.models.insertRow(row) 
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

        if not row or not row[1]:
            return
        self.idMon, hinhAnh, tenMon, giaMon = row
        
        for i in range(1,16):
            lblName  =  getattr(self.ui, f'lbname{i}', None)
            self.spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
            lblGia = getattr(self.ui, f'lbgia{i}', None)
            pwg = getattr(self.ui, f'pwg{i}', None)
            
            if not pwg:
                continue
            
            if not hasattr(pwg, "daCoAnh"):
                pwg.daCoAnh = False
            
            if not hasattr(pwg, "ImgID"):
                pwg.ImgID = None
                
            if pwg.ImgID == self.idMon:
                return
            
            if self.spinBoxSL and lblGia:
                self.spinBoxSL.valueChanged.connect(lambda value, idx=i: self.capnhatgia(idx))  
                self.spinBoxSL.valueChanged.connect(lambda: self.tongtien()) 
                
            if not hasattr(self, 'giagoc'):
              self.giagoc = {}
            
            
            if not pwg.daCoAnh :
                self.tongtien()
                
                lable = ym12c(hinhAnh,pwg)
                lable.setGeometry(0,0,lable.parent().width(),lable.parent().height())
                lable.parent().resizeEvent = self.capNhatSizeAnh
                
                lblName.setText("Món: "+tenMon)
                lblGia.setText("Đơn giá: "+str(giaMon))
                
                self.spinBoxSL.setVisible(True)
                self.giagoc[i] = giaMon
                self.giohang.append({"idMon": idMon, "tenMon": tenMon, "giaMon": giaMon, "soLuong": 1})
                
                self.spinBoxSL.setValue(1)
                pwg.daCoAnh = True
                pwg.ImgID = self.idMon
                btn.setText("Đã vào giỏ")
                self.tongtien()
                break
    def thanhtoan(self):
        if self.giohang:
            fullname = self.fullname
            idNhanVien = self.idNhanVien
            idDonHang = self.hoadon()
            if idDonHang:
             print(idDonHang,idNhanVien,fullname)
             self.xoagiohang()
       
    def capnhatgia(self,i):
        spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
        lblGia = getattr(self.ui, f'lbgia{i}', None)
        
        if not lblGia or not spinBoxSL:
            return
        if not hasattr(self, 'giagoc'):
            self.giagoc = {}
        giaMon = self.giagoc.get(i, 0)  
        soLuong = spinBoxSL.value()
        tongGia = soLuong * giaMon
        lblGia.setText("Đơn giá: "+str(tongGia))
    def xoagiohang (self):
        if self.giohang:
            for i in range(1, 16):
                lblName  =  getattr(self.ui, f'lbname{i}', None)
                spinBoxSL = getattr(self.ui, f'spinBox{i}', None)
                pwg = getattr(self.ui, f'pwg{i}', None)
                lblGia = getattr(self.ui, f'lbgia{i}', None)
                if pwg:
                    pwg.daCoAnh = False
                    pwg.ImgID = None
                    lblGia.setText("")
                    self.ui.wdLOGIN.setVisible(False)
                    for j in pwg.findChildren(QWidget):
                        j.deleteLater()
                        
                if spinBoxSL and spinBoxSL.setVisible(False):
                    spinBoxSL.setVisible(True)
                    spinBoxSL.setValue(0)
                    
                if lblGia:
                    lblGia.setText("")
                    
                if lblName:
                    lblName.setText("")
            self.ui.lbThanhtien_3.setText("0 VND") 
            self.giagoc.clear()
        for i in range(1,50):
            btn = getattr(self.ui, f"btnAdd{i}",None)
            if btn:
                btn.setText("Add to Cart")
                self.ui.wdLOGIN.setVisible(False)
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
               self.ui.pwg13,self.ui.pwg14,self.ui.pwg15,self.ui.wgThanhToan,self.ui.btnAddDB,
               self.ui.btnXoaDB,self.ui.btnRong,self.ui.WgPWG,self.ui.wdLOGIN,
               self.ui.btnLogin,self.ui.lblLogin,self.ui.wdbtn,
               self.ui.wdtile,self.ui.wdtool
               
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
                       
        label = ym12c(hinhAnh,self.ui.wg511)
        label.setGeometry(0, 0, label.parent().width(), label.parent().height())
        label.parent().resizeEvent = self.capNhatSizeAnh         
        self.lblMenu.append(label)       
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
