from controllers.Database import bd_conectar

from models.Cliente import Cliente
from models.DetalleVenta import DetalleVenta
from models.Empleado import Empleado
from models.Producto import Producto
from models.Proveedor import Proveedor
from models.RegistroPedido import RegistroPedido
from models.Venta import Venta

def test_bd():
    
    conn = bd_conectar()

    if conn:
                # Crear instancias con la conexión
        cliente = Cliente(conn)
        empleado = Empleado(conn)
        proveedor = Proveedor(conn)
        producto = Producto(conn)
        venta = Venta(conn)
        detalle_venta = DetalleVenta(conn)
        registro_pedido = RegistroPedido(conn)


        cliente.agregar("73359663","PAULO CESAR", "ROJAS", "SANCHEZ","989144561")
        print(cliente.obtener_registros())

        print(empleado.obtener_registros())

        print(proveedor.obtener_registros())

        print(producto.obtener_registros())

        print(venta.obtener_registros())

        print(detalle_venta.obtener_registros())

        print(registro_pedido.obtener_registros())


        conn.close()
        print("Conexión cerrada.")