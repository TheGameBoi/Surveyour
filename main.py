import mysql.connector
from PyQt6.QtWidgets import (QComboBox, QMessageBox, QPushButton, QLabel, QLineEdit, QGridLayout, QApplication,
        QMainWindow, QGridLayout, QWidget, QTableWidget, QToolBar, QTextEdit, QStatusBar,
        QTableWidgetItem, QDialog)
from PyQt6.QtGui import QIcon, QAction
from PyQt6.QtCore import Qt
import sys



class DatabaseConnection:
    def __init__(self, host='localhost', user='root', password='pythoncourse', database='mydatabase'):
        self.host = host
        self.user = user
        self.password = password
        self.database = database

    def connect(self):
        connection = mysql.connector.connect(host=self.host, user=self.user, password=self.password, database=self.database)
        return connection



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
        new_survey.triggered.connect(self.survey)

        # Toolbar
        toolbar = QToolBar(self)
        toolbar.setMovable(True)
        self.addToolBar(toolbar)
        toolbar.addAction(new_survey)

    def survey(self):
        dialog = SurveyDialog()
        dialog.exec()

    def load_data(self):
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        result = cursor.execute("SELECT * FROM survey")
        self.table.setRowCount(0)
        for row_number, row_data in enumerate(result):
            self.table.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.table.setItem(row_number, column_number, QTableWidgetItem(str(data)))
        connection.close()


class SurveyDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Data")
        self.setFixedSize(500, 100)

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
        add.clicked.connect(self.submit)

        # Cancel Button
        cancel = QPushButton("Cancel")
        cancel.clicked.connect(self.close)


        # Setting Layout
        layout.addWidget(self.name, 0, 0, 1, 1)
        layout.addWidget(self.age, 0, 3)
        layout.addWidget(self.gender, 0, 2)
        layout.addWidget(self.city, 0, 1)
        layout.addWidget(add, 2, 1)
        layout.addWidget(cancel, 2, 2)
        self.setLayout(layout)


    def submit(self):
        name = self.name.text()
        age = self.age.text()
        gender = self.gender.text()
        city = self.city.text()
        connection = DatabaseConnection().connect()
        cursor = connection.cursor()
        cursor.execute("INSERT INTO people (name, age, gender, city) VALUES (%s, %s, %s, %s)",
                       (name, age, gender, city))
        connection.commit()
        cursor.close()
        connection.close()

    def cancel(self):
        self.close()

app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())