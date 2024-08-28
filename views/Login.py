import sys
import mysql.connector
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QSizePolicy, QHeaderView
from PyQt5.QtCore import QFile, QTextStream
from views.VistaPrincipal import VistaPrincipal

class Login(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        self.setWindowTitle('Login')
        self.setGeometry(100, 100, 400, 200)
        
        layout = QVBoxLayout()

        self.user_label = QLabel('Usuario:')
        self.user_entry = QLineEdit()
        layout.addWidget(self.user_label)
        layout.addWidget(self.user_entry)

        self.pass_label = QLabel('Contraseña:')
        self.pass_entry = QLineEdit()
        self.pass_entry.setEchoMode(QLineEdit.Password)
        layout.addWidget(self.pass_label)
        layout.addWidget(self.pass_entry)

        self.login_button = QPushButton('Ingresar')
        self.login_button.setObjectName('add_button')
        self.login_button.clicked.connect(self.login)
        layout.addWidget(self.login_button)

        self.setLayout(layout)

    def load_styles(self):
        file = QFile("resources/css/login.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()

    def login(self):
        if self.user_entry.text() == 'admin' and self.pass_entry.text() == 'admin':
            self.close()
            self.main_window = VistaPrincipal()
            self.main_window.show()
        else:
            QMessageBox.critical(self, 'Error de autenticación', 'Usuario o contraseña incorrectos')
