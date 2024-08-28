
import sqlite3
from models.Producto import Producto


class ProductoController:
    def __init__(self, conexion):
        self.modelo = Producto(conexion)

    def agregar_producto(self, nombre, precioVenta, stock, puntoReorden, unidad, tipo):
        try:
            self.modelo.agregar(nombre, precioVenta, stock, puntoReorden, unidad, tipo)
            return True
        except sqlite3.IntegrityError:
            return False

    def obtener_producto(self,nombre):
        return self.modelo.obtener(nombre)

    def actualizar_producto(self, nombre, precioVenta, stock, puntoReorden, unidad, tipo):
        self.modelo.actualizar(nombre, precioVenta, stock, puntoReorden, unidad, tipo)

    def eliminar_producto(self, nombre):
        self.modelo.eliminar(nombre)

    def obtener_todos_los_productos(self):
        return self.modelo.obtener_registros()
