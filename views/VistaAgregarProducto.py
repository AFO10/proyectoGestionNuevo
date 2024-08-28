from PyQt5.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QFormLayout, QMessageBox
from PyQt5.QtCore import QFile, QTextStream



class VistaAgregarProducto(QDialog):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        self.setWindowTitle('Agregar Producto')
        self.setGeometry(150, 150, 400, 300)

        layout = QFormLayout()

        self.nombre_input = QLineEdit()
        self.precioVenta_input = QLineEdit()
        self.stock_input = QLineEdit()
        self.puntoReorden_input = QLineEdit()
        self.unidad_input = QLineEdit()
        self.tipo_input = QLineEdit()

        layout.addRow(QLabel('Nombre:'), self.nombre_input)
        layout.addRow(QLabel('Precio de venta:'), self.precioVenta_input)
        layout.addRow(QLabel('Stock:'), self.stock_input)
        layout.addRow(QLabel('Punto reorden:'), self.puntoReorden_input)
        layout.addRow(QLabel('Unidad:'), self.unidad_input)
        layout.addRow(QLabel('Tipo:'), self.tipo_input)

        save_button = QPushButton('Guardar')
        save_button.clicked.connect(self.save_product)
        layout.addWidget(save_button)

        self.setLayout(layout)

    def save_product(self):
        
        nombre = self.nombre_input.text()
        precioVenta = self.precioVenta_input.text()
        stock = self.stock_input.text()
        puntoReorden = self.puntoReorden_input.text()
        unidad = self.unidad_input.text()
        tipo = self.tipo_input.text()

        if not (nombre and precioVenta and stock and puntoReorden and unidad and tipo):
            QMessageBox.warning(self, 'Advertencia', 'Todos los campos deben ser completados.')
            return

        if (self.controller.agregar_producto(nombre, precioVenta, stock, puntoReorden, unidad, tipo)):
            QMessageBox.information(self, 'Éxito', 'Producto agregado exitosamente.')
        else:
            QMessageBox.warning(self, 'Error', 'Producto duplicado.')

        self.accept()  # Cierra el diálogo y regresa a la ventana principal

    def load_styles(self):
        file = QFile("resources/css/vistaAgregarItem.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()