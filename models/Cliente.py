import sqlite3

class Cliente:
    def __init__(self, con):
        self.con = con
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS cliente (
                        idCliente INTEGER PRIMARY KEY AUTOINCREMENT,
                        dni TEXT NOT NULL UNIQUE,
                        nombres TEXT NOT NULL,
                        apellidoPaterno TEXT NOT NULL,
                        apellidoMaterno TEXT NOT NULL,  
                        telefono TEXT 
                        )''')
        self.con.commit()
        cursor.close()

    def agregar(self, dni, nombres, apellidoPaterno, apellidoMaterno, telefono):       
        cursor = self.con.cursor()
        query = "INSERT INTO cliente (dni, nombres, apellidoPaterno, apellidoMaterno, telefono) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(query, (dni, nombres, apellidoPaterno, apellidoMaterno, telefono))
        self.con.commit() 
        cursor.close()

    def obtener(self, dni):
        cursor = self.con.cursor()
        query = "SELECT * FROM cliente WHERE dni = ?"
        cursor.execute (query, (dni,))
        data = cursor.fetchall()
        cursor.close()
        return data

    def actualizar(self, dni, nombres, apellidoPaterno, apellidoMaterno, telefono):
        cursor = self.con.cursor()
        query = "UPDATE cliente SET nombres = ?, apellidoPaterno = ?, apellidoMaterno = ?, telefono = ? WHERE dni = ?"
        cursor.execute(query, (nombres, apellidoPaterno, apellidoMaterno, telefono, dni))
        self.con.commit()     
        cursor.close()   

    def eliminar(self, dni):
        cursor = self.con.cursor()
        cursor.execute ('''DELETE FROM cliente WHERE dni = ? ''', (dni,))
        self.con.commit() 
        cursor.close()
    
    def obtener_registros(self):
        cursor = self.con.cursor()
        query = "SELECT dni, nombres, apellidoPaterno, apellidoMaterno, telefono FROM cliente"
        cursor.execute (query) 
        data = cursor.fetchall()
        cursor.close()
        return data