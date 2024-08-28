import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QHBoxLayout, QWidget, QLineEdit, QPushButton, QTableView, QMessageBox, QLabel, QGroupBox, QFormLayout
from PyQt5.QtCore import Qt, QSortFilterProxyModel, QFile, QTextStream
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from controllers.ClienteController import ClienteController
from controllers.Database import bd_conectar
from controllers.ProductoController import ProductoController


class VentaWindow(QMainWindow):
    def __init__(self, conexion):
        super().__init__()
        self.conexion = conexion
        self.dniCliente = None
        self.dniEmpleado = None
        self.init_ui()
        self.load_styles()

    def init_ui(self):
        # Configuración de la ventana principal
        self.setWindowTitle("Sistema de Ventas")
        self.resize(800, 600)

        # Crear el widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.main_layout = QVBoxLayout(self.central_widget)

        # Sección de búsqueda de cliente (utilizando QGroupBox para colapsar)
        self.client_groupbox = QGroupBox("Seleccionar Cliente")
        self.client_groupbox_layout = QVBoxLayout()
        self.client_groupbox.setLayout(self.client_groupbox_layout)
        
        # Layout de búsqueda de clientes
        self.client_search_input = QLineEdit()
        self.client_search_input.setPlaceholderText("Buscar por DNI o nombre")
        self.client_search_input.textChanged.connect(self.filter_clients)

        self.client_table = QTableView()
        self.client_table.setSelectionBehavior(QTableView.SelectRows)
        self.client_table.setSelectionMode(QTableView.SingleSelection)

        # Crear el modelo de clientes
        self.client_model = QStandardItemModel()
        self.client_model.setHorizontalHeaderLabels(["DNI", "Nombres","Apellido Paterno", "Apellido Materno", "Teléfono"])
        self.populate_clients()

        # Crear un proxy model para filtrar la lista de clientes
        self.client_proxy_model = QSortFilterProxyModel()
        self.client_proxy_model.setSourceModel(self.client_model)
        self.client_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.client_proxy_model.setFilterKeyColumn(1)  # Filtrar por la columna "Nombre"
        self.client_proxy_model.setFilterKeyColumn(0)  # Filtrar por la columna "DNI"
        self.client_table.setModel(self.client_proxy_model)

        # Añadir widgets a la sección de búsqueda de clientes
        self.client_groupbox_layout.addWidget(self.client_search_input)
        self.client_groupbox_layout.addWidget(self.client_table)

        self.client_search_button = QPushButton("Seleccionar Cliente")
        self.client_search_button.clicked.connect(self.select_client)
        self.client_groupbox_layout.addWidget(self.client_search_button)

        # Añadir el groupbox de clientes al layout principal
        self.main_layout.addWidget(self.client_groupbox)

        # Mostrar cliente seleccionado
        self.selected_client_label = QLabel("Cliente seleccionado: Ninguno")
        self.main_layout.addWidget(self.selected_client_label)

        # Sección de compra (se activa tras seleccionar cliente)
        self.purchase_layout = QVBoxLayout()

        # Filtro y tabla de productos disponibles
        self.product_search_input = QLineEdit()
        self.product_search_input.setPlaceholderText("Buscar producto...")
        self.product_search_input.setEnabled(False)
        self.purchase_layout.addWidget(self.product_search_input)

        self.product_table = QTableView()
        self.product_table.setEnabled(False)
        self.purchase_layout.addWidget(self.product_table)

        # Botón para añadir el producto seleccionado a la lista de venta
        self.add_product_button = QPushButton("Añadir Producto a la Venta")
        self.add_product_button.setEnabled(False)
        self.add_product_button.clicked.connect(self.add_product_to_sale)
        self.purchase_layout.addWidget(self.add_product_button)

        # Tabla para mostrar productos seleccionados para la venta
        self.sale_table = QTableView()
        self.sale_model = QStandardItemModel()
        self.sale_model.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio", "SubTotal"])
        self.sale_table.setModel(self.sale_model)
        self.purchase_layout.addWidget(self.sale_table)

        # Botón para finalizar la venta
        self.finish_sale_button = QPushButton("Finalizar Venta")
        self.finish_sale_button.setEnabled(False)
        self.finish_sale_button.clicked.connect(self.finalize_sale)
        self.purchase_layout.addWidget(self.finish_sale_button)

        self.main_layout.addLayout(self.purchase_layout)

        # Configurar modelo y proxy para productos disponibles
        self.product_model = QStandardItemModel()
        self.product_model.setHorizontalHeaderLabels(["Producto", "Precio", "Stock Disponible", "Punto de Reorden", "Unidad", "Tipo"])
        self.populate_products()

        self.product_proxy_model = QSortFilterProxyModel()
        self.product_proxy_model.setSourceModel(self.product_model)
        self.product_proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.product_proxy_model.setFilterKeyColumn(1)  # Filtrar por la columna "Nombre"
        self.product_table.setModel(self.product_proxy_model)

        # Conectar el filtrado de productos con la entrada de búsqueda
        self.product_search_input.textChanged.connect(self.filter_products)

    def populate_clients(self):
        # Rellenar la tabla de clientes con datos de ejemplo

        clienteController = ClienteController(self.conexion)
        clients = clienteController.obtener_todos_los_clientes()

        for client in clients:
            items = [QStandardItem(str(field)) for field in client]
            self.client_model.appendRow(items)

    def populate_products(self):
        # Rellenar la tabla de productos con datos de ejemplo

        productoController = ProductoController(self.conexion)
        products = productoController.obtener_todos_los_productos()

        for product in products:
            items = [QStandardItem(str(field)) for field in product]
            self.product_model.appendRow(items)

    def filter_clients(self, text):
        # Filtrar la lista de clientes según el texto ingresado
        self.client_proxy_model.setFilterRegExp(text)

    def select_client(self):
        # Seleccionar el cliente de la tabla y activar la sección de compra
        selected_indexes = self.client_table.selectionModel().selectedRows()
        if selected_indexes:
            index = selected_indexes[0]
            client_name = self.client_proxy_model.data(self.client_proxy_model.index(index.row(), 1))
            self.dniCliente = self.client_proxy_model.data(self.client_proxy_model.index(index.row(), 0))
            self.selected_client_label.setText(f"Cliente seleccionado: {client_name}")
            self.activate_purchase_section()

            # Ocultar la sección de selección de cliente
            self.client_groupbox.setVisible(False)
        else:
            QMessageBox.warning(self, "Error", "Debe seleccionar un cliente antes de continuar.")

    def activate_purchase_section(self):
        # Activar la sección de compra después de seleccionar un cliente
        self.product_search_input.setEnabled(True)
        self.product_table.setEnabled(True)
        self.add_product_button.setEnabled(True)
        self.finish_sale_button.setEnabled(True)

    def filter_products(self, text):
        # Filtrar la lista de productos según el texto ingresado
        self.product_proxy_model.setFilterRegExp(text)

    def add_product_to_sale(self):
        # Añadir el producto seleccionado a la lista de venta
        selected_indexes = self.product_table.selectionModel().selectedRows()
        if selected_indexes:
            for index in selected_indexes:
                product_name = self.product_proxy_model.data(self.product_proxy_model.index(index.row(), 1))
                product_price = float(self.product_proxy_model.data(self.product_proxy_model.index(index.row(), 2)))

                # Añadir una fila a la tabla de venta
                row = [QStandardItem(product_name), QStandardItem("1"), QStandardItem(f"{product_price:.2f}"), QStandardItem(f"{product_price:.2f}")]
                self.sale_model.appendRow(row)
        else:
            QMessageBox.warning(self, "Error", "Debe seleccionar un producto antes de añadirlo a la venta.")

    def finalize_sale(self):
        # Finalizar la venta (puede añadir lógica para guardar en base de datos, etc.)
        total = 0.0
        for row in range(self.sale_model.rowCount()):
            total += float(self.sale_model.item(row, 3).text())

        QMessageBox.information(self, "Venta Finalizada", f"El total de la venta es: ${total:.2f}")
        self.sale_model.clear()
        self.sale_model.setHorizontalHeaderLabels(["Producto", "Cantidad", "Precio Unitario", "Total"])
        self.client_search_input.clear()
        self.product_search_input.clear()
        self.product_search_input.setEnabled(False)
        self.product_table.setEnabled(False)
        self.add_product_button.setEnabled(False)
        self.finish_sale_button.setEnabled(False)
        self.selected_client_label.setText("Cliente seleccionado: Ninguno")
        # Mostrar la sección de selección de cliente nuevamente
        self.client_groupbox.setVisible(True)

    def load_styles(self):
        file = QFile("resources/css/vistaAgregarItem.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VentaWindow(bd_conectar())
    window.show()
    sys.exit(app.exec_())
