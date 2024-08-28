class Venta:
    
    def __init__(self, con):
        self.con = con
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS venta (
                        idVenta INTEGER PRIMARY KEY AUTOINCREMENT,
                        idEmpleadoFK INTEGER NOT NULL,
                        idClienteFK INTEGER NOT NULL,
                        fecha TEXT DEFAULT (CURRENT_DATE),
                        FOREIGN KEY (idEmpleadoFK) REFERENCES empleado(idEmpleado),
                        FOREIGN KEY (idClienteFK) REFERENCES cliente(idCliente)
                        )''')
        self.con.commit()
        cursor.close()

    def agregar(self, idEmpleadoFK, idClienteFK):       
        cursor = self.con.cursor()
        query = "INSERT INTO venta (idEmpleadoFK, idClienteFK) VALUES (?, ?)"
        cursor.execute(query, (idEmpleadoFK, idClienteFK))
        self.con.commit() 
        cursor.close()

    def obtener(self, idVenta):
        cursor = self.con.cursor()
        query = "SELECT * FROM venta WHERE idVenta = ?"
        cursor.execute(query, (idVenta,))
        data = cursor.fetchall()
        cursor.close()
        return data

    def actualizar(self, idVenta, idEmpleadoFK, idClienteFK):
        cursor = self.con.cursor()
        query = "UPDATE venta SET idEmpleadoFK = ?, idClienteFK = ? WHERE idVenta = ?"
        cursor.execute(query, (idEmpleadoFK, idClienteFK, idVenta))
        self.con.commit()     
        cursor.close()   

    def eliminar(self, idVenta):
        cursor = self.con.cursor()
        cursor.execute('''DELETE FROM venta WHERE idVenta = ?''', (idVenta,))
        self.con.commit() 
        cursor.close()
    
    def obtener_registros(self):
        cursor = self.con.cursor()
        query = "SELECT * FROM venta"
        cursor.execute(query) 
        data = cursor.fetchall()
        cursor.close()
        return data