
import mysql.connector
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QPushButton, QMessageBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QSizePolicy, QHeaderView
from PyQt5.QtCore import QFile, QTextStream

from views.VistaProveedor import VistaProveedor
from views.VistaCliente import VistaCliente
from views.VistaEmpleado import VistaEmpleado
from views.VistaPedido import VistaPedido
from views.VistaProducto import VistaProducto
from views.VistaRealizarVenta import VistaRealizarVenta
from views.VistaVenta import VistaVenta

from controllers.Database import bd_conectar

class VistaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.con = bd_conectar()
        self.init_ui()
        self.load_styles()
        self.open_windows = []

    def init_ui(self):
        self.setWindowTitle('Menú Principal')
        self.setGeometry(100, 100, 800, 600)

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()

        buttons = [
            ('Cliente', self.show_cliente),
            ('Proveedor', self.show_proveedor),
            ('Empleado', self.show_empleado),
            ('Producto', self.show_producto),
            ('Venta', self.show_venta),
            ('Entregas', self.show_pedido),
            ('Realizar Venta', self.realizar_venta),
            ('Cerrar Sesión', self.close)
        ]

        for text, func in buttons:
            button = QPushButton(text)
            button.clicked.connect(func)
            layout.addWidget(button)
            if text == 'Cerrar Sesión':
                button.setObjectName('logout_button')
            else:
                button.setObjectName('menu_button')

        central_widget.setLayout(layout)

    def show_cliente(self):
        cliente_window = VistaCliente(self.con)
        self.open_window(cliente_window)

    def show_proveedor(self):
        proveedor_window = VistaProveedor(self.con)
        self.open_window(proveedor_window)

    def show_empleado(self):
        empleado_window = VistaEmpleado(self.con)
        self.open_window(empleado_window)

    def show_producto(self):
        producto_window = VistaProducto(self.con)
        self.open_window(producto_window)

    def show_venta(self):
        venta_window = VistaVenta(self.con)
        self.open_window(venta_window)

    def show_pedido(self):
        pedido_window = VistaPedido(self.con)
        self.open_window(pedido_window)

    def realizar_venta(self):
        realizar_venta_window = VistaRealizarVenta(self.con)
        self.open_window(realizar_venta_window)


    def open_window(self,window_class):
        window = window_class
        window.show()
        self.open_windows.append(window)


    def load_styles(self):
        file = QFile("resources/css/vistaPrincipal.css")
        if file.open(QFile.ReadOnly | QFile.Text):
            stream = QTextStream(file)
            self.setStyleSheet(stream.readAll())
        file.close()