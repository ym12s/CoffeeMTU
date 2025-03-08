import sys
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
COFFEE_DIR = os.path.join(SRC_DIR, "coffee")
UI_DIR = os.path.join(SRC_DIR, "__ui")
UI_FILE = os.path.join(UI_DIR, "ui_mainwindow.py")
QRC_FILE = os.path.join(BASE_DIR, "resources_rc.py")
FORM_UI = os.path.join(UI_DIR, "form.ui")
RESOURCE_QRC = os.path.join(BASE_DIR, "resources.qrc")

if SRC_DIR not in sys.path:
    sys.path.append(SRC_DIR)
if COFFEE_DIR not in sys.path:
    sys.path.append(COFFEE_DIR)

if not os.path.exists(UI_FILE):
    try:
        subprocess.run(["pyside6-uic", FORM_UI, "-o", UI_FILE], check=True)
    except subprocess.CalledProcessError as e:
        print(f"LỖI: Không thể tạo {UI_FILE}. Chi tiết: {e}")
        sys.exit(1)

if not os.path.exists(QRC_FILE):
    try:
        subprocess.run(["pyside6-rcc", RESOURCE_QRC, "-o", QRC_FILE], check=True)
    except subprocess.CalledProcessError as e:
        print(f"LỖI: Không thể tạo {QRC_FILE}. Chi tiết: {e}")
        sys.exit(1)

if not os.path.exists(os.path.join(COFFEE_DIR, "mainwindow.py")):
    print(f"LỖI: Không tìm thấy mainwindow.py trong {COFFEE_DIR}")
    sys.exit(1)

try:
    from src.coffee.mainwindow import MainWindow
except ModuleNotFoundError as e:
    print(f"LỖI: Import thất bại! Kiểm tra lại module. Chi tiết: {e}")
    print(f"sys.path hiện tại: {sys.path}")
    sys.exit(1)
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon("src/ass/icon.ico"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())            
    
