class Proveedor:
    
    def __init__(self, con):
        self.con = con
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS proveedor (
                        idProveedor INTEGER PRIMARY KEY AUTOINCREMENT,
                        ruc TEXT NOT NULL UNIQUE,
                        nombre TEXT NOT NULL,
                        telefono TEXT
                        )''')
        self.con.commit()
        cursor.close()

    def agregar(self, ruc, nombre, telefono):       
        cursor = self.con.cursor()
        query = "INSERT INTO proveedor (ruc, nombre, telefono) VALUES (?, ?, ?)"
        cursor.execute(query, (ruc, nombre,telefono))
        self.con.commit() 
        cursor.close()

    def obtener(self, nombre):
        cursor = self.con.cursor()
        query = "SELECT * FROM proveedor WHERE nombre = ?"
        cursor.execute (query, (nombre,))
        data = cursor.fetchall()
        cursor.close()
        return data

    def actualizar(self, ruc, nombre, telefono):
        cursor = self.con.cursor()
        query = "UPDATE proveedor SET nombre = ?, telefono = ? WHERE ruc = ?"
        cursor.execute(query, (nombre, telefono,ruc))
        self.con.commit()     
        cursor.close()   

    def eliminar(self, ruc):
        cursor = self.con.cursor()
        cursor.execute ('''DELETE FROM proveedor WHERE ruc = ? ''', (ruc,))
        self.con.commit() 
        cursor.close()
    
    def obtener_registros(self):
        cursor = self.con.cursor()
        query = "SELECT ruc, nombre, telefono FROM proveedor"
        cursor.execute (query) 
        data = cursor.fetchall()
        cursor.close()
        return data