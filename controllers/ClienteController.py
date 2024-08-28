
import sqlite3
from controllers.Database import bd_conectar
from models.Cliente import Cliente
from apis.apis import ApisNetPe


class ClienteController:
    def __init__(self, conexion):
        self.modelo = Cliente(conexion)

    def agregar_cliente(self, dni, nombres, apellidoPaterno, apellidoMaterno, telefono):
        try:
            self.modelo.agregar(dni, nombres, apellidoPaterno, apellidoMaterno, telefono)
            return True
        except sqlite3.IntegrityError:
            return False

    def obtener_cliente(self,dni):
        return self.modelo.obtener(dni)

    def actualizar_cliente(self, dni, nombres, apellidoPaterno, apellidoMaterno, telefono):
        self.modelo.actualizar(dni, nombres, apellidoPaterno, apellidoMaterno, telefono)


    def eliminar_cliente(self, dni):
        self.modelo.eliminar(dni)

    def obtener_todos_los_clientes(self):
        return self.modelo.obtener_registros()

