
import sqlite3
from models.Proveedor import Proveedor

class ProveedorController:
    def __init__(self, conexion):
        self.modelo = Proveedor(conexion)

    def agregar_proveedor(self, ruc, nombre, telefono):
        try:
            self.modelo.agregar(ruc, nombre, telefono)
            return True
        except sqlite3.IntegrityError:
            return False

    def obtener_proveedor(self,ruc):
        return self.modelo.obtener(ruc)

    def actualizar_proveedor(self, ruc, nombre, telefono):
        self.modelo.actualizar(ruc, nombre, telefono)

    def eliminar_proveedor(self, ruc):
        self.modelo.eliminar(ruc)

    def obtener_todos_los_proveedors(self):
        return self.modelo.obtener_registros()