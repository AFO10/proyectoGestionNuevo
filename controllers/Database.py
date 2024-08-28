import sqlite3

# CONTROLADOR DE LA BASE DE DATOS

def bd_conectar():
    try:
        conn = sqlite3.connect('resources/database.db')
        print("Conexión establecida exitosamente")
        return conn
    except sqlite3.Error as e:
        print(f"Error al conectar con la base de datos: {e}")
        return None
    