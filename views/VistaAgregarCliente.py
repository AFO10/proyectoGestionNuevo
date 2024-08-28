from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
from PyQt5.QtCore import QFile, QTextStream


from apis.apis import ApisNetPe

APIS_TOKEN = "apis-token-10051.AcFJQ4tDjkx2oEERMzQmnG7hITKRBWBn"

class VistaAgregarCliente(QDialog):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        self.setWindowTitle('Agregar Cliente')
        self.setGeometry(150, 150, 400, 300)

        layout = QFormLayout()

        self.dni_input = QLineEdit()
        self.nombres_input = QLineEdit()
        self.apellidoPaterno_input = QLineEdit()
        self.apellidoMaterno_input = QLineEdit()
        self.telefono_input = QLineEdit()


        layout.addRow(QLabel('DNI:'), self.dni_input)
        layout.addRow(QLabel('Nombres:'), self.nombres_input)
        layout.addRow(QLabel('Apellido Paterno:'), self.apellidoPaterno_input)
        layout.addRow(QLabel('Apellido Materno:'), self.apellidoMaterno_input)
        layout.addRow(QLabel('Teléfono:'), self.telefono_input)

        consult_button = QPushButton("Consultar")
        consult_button.clicked.connect(self.consultar_api)
        layout.addWidget(consult_button)


        save_button = QPushButton('Guardar')
        save_button.clicked.connect(self.save_client)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def consultar_api(self):

        dni = self.dni_input.text()

        if not dni:
            QMessageBox.warning(self, 'Advertencia', 'El DNI debe ser completado.')
            return
        
        api_consultas = ApisNetPe(APIS_TOKEN)

        persona = api_consultas.get_person(dni)

        if (persona != None):
            nombres = persona["nombres"]
            apellidoPaterno = persona["apellidoPaterno"]
            apellidoMaterno = persona["apellidoMaterno"]

            self.nombres_input.setText(nombres)
            self.apellidoPaterno_input.setText(apellidoPaterno)
            self.apellidoMaterno_input.setText(apellidoMaterno)

        else:
            QMessageBox.warning(self, 'Error', 'DNI no válido.')

    def save_client(self):
        
        dni = self.dni_input.text()
        nombres = self.nombres_input.text()
        apellidoPaterno = self.apellidoPaterno_input.text()
        apellidoMaterno = self.apellidoMaterno_input.text()
        telefono = self.telefono_input.text()

        if not (dni and nombres and apellidoMaterno and apellidoPaterno and telefono):
            QMessageBox.warning(self, 'Advertencia', 'Todos los campos deben ser completados.')
            return

        if (self.controller.agregar_cliente(dni, nombres, apellidoPaterno, apellidoMaterno, telefono)):
            QMessageBox.information(self, 'Éxito', 'Cliente agregado exitosamente.')
        else:
            QMessageBox.warning(self, 'Error', 'Cliente duplicado.')

        self.accept()  # Cierra el diálogo y regresa a la ventana principal

    def load_styles(self):
        file = QFile("resources/css/vistaAgregarItem.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()