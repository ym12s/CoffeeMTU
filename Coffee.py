import sys
import subprocess
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
subprocess.run(["pyside6-uic", "src/__ui/form.ui", "-o", "src/__ui/ui_mainwindow.py"], check=True)
from PySide6.QtUiTools import QUiLoader
from src.coffee.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    app.setWindowIcon(QIcon("src/__ass/icon.ico"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
