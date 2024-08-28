import sqlite3
from models.Empleado import Empleado

class EmpleadoController:
    def __init__(self, conexion):
        self.modelo = Empleado(conexion)

    def agregar_empleado(self, dni, nombres, apellidoPaterno, apellidoMaterno, telefono):
        try:
            self.modelo.agregar(dni, nombres, apellidoPaterno, apellidoMaterno, telefono)
            return True
        except sqlite3.IntegrityError:
            return False

    def obtener_empleado(self,dni):
        return self.modelo.obtener(dni)

    def actualizar_empleado(self, dni, nombres, apellidoPaterno, apellidoMaterno, telefono):
        self.modelo.actualizar(dni, nombres, apellidoPaterno, apellidoMaterno, telefono)

    def eliminar_empleado(self, dni):
        self.modelo.eliminar(dni)

    def obtener_todos_los_empleados(self):
        return self.modelo.obtener_registros()