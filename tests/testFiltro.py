import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLineEdit, QTableView
from PyQt5.QtCore import Qt, QSortFilterProxyModel
from PyQt5.QtGui import QStandardItemModel, QStandardItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Configuración de la ventana principal
        self.setWindowTitle("Filtrado Reactivo de Datos en PyQt5")
        self.resize(600, 400)

        # Crear un widget central
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)
        self.layout = QVBoxLayout(self.central_widget)

        # Crear el QLineEdit para la entrada de texto
        self.filter_input = QLineEdit()
        self.filter_input.setPlaceholderText("Indique DNI o nombre")
        self.layout.addWidget(self.filter_input)

        # Crear el QTableView para mostrar los datos
        self.table_view = QTableView()
        self.layout.addWidget(self.table_view)

        # Configurar el modelo de la tabla
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(["ID", "Nombre", "Edad"])
        self.populate_data()

        # Configurar el modelo proxy de filtrado
        self.proxy_model = QSortFilterProxyModel()
        self.proxy_model.setSourceModel(self.model)
        self.proxy_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.proxy_model.setFilterKeyColumn(1)  # Filtrar por la columna "Nombre"
        self.proxy_model.setFilterKeyColumn(0)  # Filtrar por la columna "Nombre"

        # Conectar el proxy_model al QTableView
        self.table_view.setModel(self.proxy_model)

        # Conectar la señal de texto cambiado del QLineEdit a la función de filtrado
        self.filter_input.textChanged.connect(self.filter_data)

    def populate_data(self):
        # Rellenar la tabla con algunos datos de ejemplo
        data = [
            [1, "Alice", 30],
            [2, "Bob", 25],
            [3, "Charlie", 35],
            [4, "David", 40],
            [5, "Eve", 22]
        ]

        for row in data:
            items = [QStandardItem(str(field)) for field in row]
            self.model.appendRow(items)

    def filter_data(self, text):
        # Filtrar los datos en la tabla en función del texto ingresado
        self.proxy_model.setFilterRegExp(text)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
