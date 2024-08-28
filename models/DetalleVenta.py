
class DetalleVenta:
    
    def __init__(self, con):
        self.con = con
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS detalleVenta (
                        idDetalleVenta INTEGER PRIMARY KEY AUTOINCREMENT,
                        idVentaFK INTEGER NOT NULL,
                        idProductoFK INTEGER NOT NULL,
                        cantidadVenta REAL NOT NULL,
                        FOREIGN KEY (idVentaFK) REFERENCES venta(idVenta),
                        FOREIGN KEY (idProductoFK) REFERENCES producto(idProducto)
                        )''')
        self.con.commit()
        cursor.close()

    def agregar(self, idVentaFK, idProductoFK, cantidadVenta):       
        cursor = self.con.cursor()
        query = "INSERT INTO detalleVenta (idVentaFK, idProductoFK, cantidadVenta) VALUES (?, ?, ?)"
        cursor.execute(query, (idVentaFK, idProductoFK, cantidadVenta))
        self.con.commit() 
        cursor.close()

    def obtener(self, idDetalleVenta):
        cursor = self.con.cursor()
        query = "SELECT * FROM detalleVenta WHERE idDetalleVenta = ?"
        cursor.execute(query, (idDetalleVenta,))
        data = cursor.fetchall()
        cursor.close()
        data = cursor.fetchall()
        cursor.close()
        return data

    def actualizar(self, idDetalleVenta, idVentaFK, idProductoFK, cantidadVenta):
        cursor = self.con.cursor()
        query = "UPDATE detalleVenta SET idVentaFK = ?, idProductoFK = ?, cantidadVenta = ? WHERE idDetalleVenta = ?"
        cursor.execute(query, (idVentaFK, idProductoFK, cantidadVenta, idDetalleVenta))
        self.con.commit()     
        cursor.close()   

    def eliminar(self, idDetalleVenta):
        cursor = self.con.cursor()
        cursor.execute('''DELETE FROM detalleVenta WHERE idDetalleVenta = ?''', (idDetalleVenta,))
        self.con.commit() 
        cursor.close()
    
    def obtener_registros(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM detalleVenta"
        cursor.execute(query) 
        data = cursor.fetchall()
        cursor.close()
        return data