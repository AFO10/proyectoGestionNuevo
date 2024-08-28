
class Producto:
    
    def __init__(self, con):
        self.con = con
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS producto (
                        idProducto INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL UNIQUE,
                        precioVenta REAL,
                        stock REAL,
                        puntoReorden REAL,
                        unidad TEXT,
                        tipo TEXT
                        )''')
        self.con.commit()
        cursor.close()

    def agregar(self, nombre, precioVenta, stock, puntoReorden, unidad, tipo):       
        cursor = self.con.cursor()
        query = "INSERT INTO producto (nombre, precioVenta, stock, puntoReorden, unidad, tipo) VALUES (?, ?, ?,?, ?, ?)"
        cursor.execute(query, (nombre, precioVenta, stock, puntoReorden, unidad, tipo))
        self.con.commit() 
        cursor.close()

    def obtener(self, nombre):
        cursor = self.con.cursor()
        query = "SELECT * FROM producto WHERE nombre = ?"
        cursor.execute (query, (nombre,))
        data = cursor.fetchall()
        cursor.close()
        return data

    def actualizar(self, nombre, precioVenta, stock, puntoReorden, unidad, tipo):
        cursor = self.con.cursor()
        query = "UPDATE producto SET precioVenta = ?, stock = ?, puntoReorden = ?, unidad = ?, tipo = ? WHERE nombre = ?"
        cursor.execute(query, (precioVenta, stock, puntoReorden, unidad, tipo, nombre))
        self.con.commit()     
        cursor.close()   

    def eliminar(self, nombre):
        cursor = self.con.cursor()
        cursor.execute ('''DELETE FROM producto WHERE nombre = ? ''', (nombre,))
        self.con.commit() 
        cursor.close()
    
    def obtener_registros(self):
        cursor = self.con.cursor()
        query = "SELECT nombre, precioVenta, stock, puntoReorden, unidad, tipo FROM producto"
        cursor.execute (query) 
        data = cursor.fetchall()
        cursor.close()
        return data