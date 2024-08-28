from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
from PyQt5.QtCore import QFile, QTextStream



class VistaAgregarProveedor(QDialog):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        self.setWindowTitle('Agregar Proveedor')
        self.setGeometry(150, 150, 400, 300)

        layout = QFormLayout()

        self.ruc_input = QLineEdit()
        self.nombre_input = QLineEdit()
        self.telefono_input = QLineEdit()


        layout.addRow(QLabel('RUC:'), self.ruc_input)
        layout.addRow(QLabel('Nombre:'), self.nombre_input)
        layout.addRow(QLabel('Teléfono:'), self.telefono_input)

        save_button = QPushButton('Guardar')
        save_button.clicked.connect(self.save_client)
        layout.addWidget(save_button)

        self.setLayout(layout)


    def save_client(self):
        
        ruc = self.ruc_input.text()
        nombre = self.nombre_input.text()
        telefono = self.telefono_input.text()

        if not (ruc and nombre and telefono):
            QMessageBox.warning(self, 'Advertencia', 'Todos los campos deben ser completados.')
            return

        if (self.controller.agregar_proveedor(ruc, nombre, telefono)):
            QMessageBox.information(self, 'Éxito', 'Proveedor agregado exitosamente.')
        else:
            QMessageBox.warning(self, 'Error', 'Proveedor duplicado.')

        self.accept()  # Cierra el diálogo y regresa a la ventana principal

    def load_styles(self):
        file = QFile("resources/css/vistaAgregarItem.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()