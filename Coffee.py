import sys
import subprocess
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.join(BASE_DIR, "src")
COFFEE_DIR = os.path.join(SRC_DIR, "coffee")
UI_FILE = os.path.join(SRC_DIR, "__ui", "ui_mainwindow.py")
QRC_FILE = os.path.join(BASE_DIR, "resources_rc.py")

sys.path.append(SRC_DIR)
sys.path.append(COFFEE_DIR)
if not os.path.exists(UI_FILE):
    subprocess.run(["pyside6-uic", os.path.join(SRC_DIR, "__ui", "form.ui"), "-o", UI_FILE], check=True)

if not os.path.exists(QRC_FILE):
    subprocess.run(["pyside6-rcc", os.path.join(BASE_DIR, "resources.qrc"), "-o", QRC_FILE], check=True)

try:
    from src.coffee.mainwindow import MainWindow
except ModuleNotFoundError as e:
    print(f"LỖI: Không tìm thấy mainwindow.py! Kiểm tra lại đường dẫn. Chi tiết: {e}")
    sys.exit(1)

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon("src/ass/icon.ico"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())            
