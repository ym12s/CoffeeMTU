import sys
import os
import json
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from PySide6.QtUiTools import QUiLoader
from coffee.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")

    # Thiết lập icon cho ứng dụng
    app.setWindowIcon(QIcon("src/__ass/icon.ico"))

    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
