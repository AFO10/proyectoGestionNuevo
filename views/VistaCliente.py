from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton, QLabel, QLineEdit, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QSizePolicy, QHeaderView
from PyQt5.QtCore import QFile, QTextStream

from controllers.ClienteController import ClienteController

from views.VistaAgregarCliente import VistaAgregarCliente

class VistaCliente(QWidget):
    def __init__(self, conexion):
        super().__init__()
        self.table_windows = []
        self.controller = ClienteController(conexion)
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        self.setWindowTitle('Clientes')
        self.setGeometry(100, 100, 800, 400)

        layout = QVBoxLayout()

        dataCliente = self.controller.obtener_todos_los_clientes()
        columns = ["DNI", "Nombres", "Apellido Paterno", "Apellido Materno", "Teléfono"]

        table = QTableWidget()
        table.setRowCount(len(dataCliente))
        table.setColumnCount(len(columns))
        table.setHorizontalHeaderLabels(columns)

        header = table.horizontalHeader()
        for col in range(len(columns)):
            header.setSectionResizeMode(col, QHeaderView.Stretch)

        table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        for row_idx, row_data in enumerate(dataCliente):
            for col_idx, item in enumerate(row_data):
                table.setItem(row_idx, col_idx, QTableWidgetItem(str(item)))

        layout.addWidget(table)

        button_layout = QHBoxLayout()

        add_button = QPushButton('Agregar')
        edit_button = QPushButton('Editar')
        delete_button = QPushButton('Eliminar')

        add_button.setObjectName('add_button')
        edit_button.setObjectName('edit_button')
        delete_button.setObjectName('delete_button')

        add_button.clicked.connect(self.agregarCliente)
        # edit_button.clicked.connect(self.edit_item)
        # delete_button.clicked.connect(self.delete_item)

        button_layout.addWidget(add_button)
        button_layout.addWidget(edit_button)
        button_layout.addWidget(delete_button)
        
        layout.addLayout(button_layout)

        close_button = QPushButton('Cerrar')
        close_button.setObjectName('close_button')
        close_button.clicked.connect(self.close)
        layout.addWidget(close_button)

        self.setLayout(layout)

    def load_styles(self):
        file = QFile("resources/css/vistaTabla.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()

    def agregarCliente(self):
        self.add_client_window = VistaAgregarCliente(self, self.controller)
        self.add_client_window.exec_()