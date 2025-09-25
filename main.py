from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
    QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
    QTableWidgetItem)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
import mysql.connector
import sys



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Main Window
        self.setWindowTitle("Surveyor")
        self.setMinimumSize(600, 400)


        # Table Layout
        self.table = QTableWidget(self)
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("Name", "Age", "Gender", "City"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())