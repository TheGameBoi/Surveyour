from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
        QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
        QTableWidgetItem, QDialog)
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


        new_survey = QAction("New Survey", self)



        # Toolbar
        toolbar = QToolBar(self)
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(new_survey)




class SurveyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Data")
        self.setFixedSize(600, 400)

        # Grid layout
        layout = QGridLayout()

        # Name
        self.name = QLineEdit()
        self.name.setPlaceholderText("Name")

        # Age
        self.age = QLineEdit()
        self.age.setPlaceholderText("Age")

        # Gender
        self.gender = QLineEdit()
        self.gender.setPlaceholderText("Gender")

        # City
        self.city = QLineEdit()
        self.city.setPlaceholderText("City")

        # Submit Button
        add = QPushButton("Submit")


        # Setting Layout
        self.setLayout(layout)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())