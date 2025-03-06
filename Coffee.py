import sys
<<<<<<< HEAD
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from coffee.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
=======
import subprocess
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
subprocess.run(["pyside6-uic", "src/__ui/form.ui", "-o", "src/__ui/ui_mainwindow.py"], check=True)
subprocess.run(["pyside6-rcc", "resources.qrc", "-o", "resources_rc.py"], check=True)

from PySide6.QtUiTools import QUiLoader
from src.coffee.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
>>>>>>> 078f5ca (Test)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
<<<<<<< HEAD
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
=======
    app.setWindowIcon(QIcon("src/ass/icon.ico"))
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())            
>>>>>>> 078f5ca (Test)
