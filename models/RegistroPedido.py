    


class RegistroPedido:
    
    def __init__(self, con):
        self.con = con
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS registroPedido (
                        idRegistroPedido INTEGER PRIMARY KEY AUTOINCREMENT,
                        idProductoFK INTEGER NOT NULL,
                        idProveedorFK INTEGER NOT NULL,
                        idEmpleadoFK INTEGER NOT NULL,
                        cantidadProducto REAL NOT NULL,
                        fechaEntrega DATE DEFAULT (CURRENT_DATE),
                        FOREIGN KEY (idProductoFK) REFERENCES producto(idProducto),
                        FOREIGN KEY (idProveedorFK) REFERENCES proveedor(idProveedor),
                        FOREIGN KEY (idEmpleadoFK) REFERENCES empleado(idEmpleado)
                        )''')
        self.con.commit()
        cursor.close()

    def agregar(self, idProductoFK, idProveedorFK, idEmpleadoFK, cantidadProducto):       
        cursor = self.con.cursor()
        query = "INSERT INTO registroPedido (idProductoFK, idProveedorFK, idEmpleadoFK, cantidadProducto) VALUES (?, ?, ?, ?)"
        cursor.execute(query, (idProductoFK, idProveedorFK, idEmpleadoFK, cantidadProducto))
        self.con.commit() 
        cursor.close()

    def obtener(self, idRegistroPedido):
        cursor = self.con.cursor()
        query = "SELECT * FROM registroPedido WHERE idRegistroPedido = ?"
        cursor.execute(query, (idRegistroPedido,))
        data = cursor.fetchall()
        cursor.close()
        return data

    def actualizar(self, idRegistroPedido, idProductoFK, idProveedorFK, idEmpleadoFK, cantidadProducto, fechaEntrega):
        cursor = self.con.cursor()
        query = "UPDATE registroPedido SET idProductoFK = ?, idProveedorFK = ?, idEmpleadoFK = ?, cantidadProducto = ?, fechaEntrega = ? WHERE idRegistroPedido = ?"
        cursor.execute(query, (idProductoFK, idProveedorFK, idEmpleadoFK, cantidadProducto, fechaEntrega, idRegistroPedido))
        self.con.commit()     
        cursor.close()   

    def eliminar(self, idRegistroPedido):
        cursor = self.con.cursor()
        cursor.execute('''DELETE FROM registroPedido WHERE idRegistroPedido = ?''', (idRegistroPedido,))
        self.con.commit() 
        cursor.close()
    
    def obtener_registros(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM registroPedido"
        cursor.execute(query) 
        data = cursor.fetchall()
        cursor.close()
        return data