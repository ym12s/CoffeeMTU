import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "src")))
from coffee.mainwindow import MainWindow
from PySide6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
