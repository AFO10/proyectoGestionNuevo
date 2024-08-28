

from apis.apis import ApisNetPe
from models.Cliente import Cliente
from models.DetalleVenta import DetalleVenta
from models.Empleado import Empleado
from models.Producto import Producto
from models.Proveedor import Proveedor
from models.RegistroPedido import RegistroPedido
from models.Venta import Venta

from controllers.Database import bd_conectar



APIS_TOKEN = "apis-token-10051.AcFJQ4tDjkx2oEERMzQmnG7hITKRBWBn"


def test_api():

    api_consultas = ApisNetPe(APIS_TOKEN)

    ingresoDNI = input("Indique dni: ")
    persona = api_consultas.get_person(ingresoDNI)

    print(persona)
    if (persona != None):

        nombres = persona["nombres"]
        apellidoPaterno = persona["apellidoPaterno"]
        apellidoMaterno = persona["apellidoMaterno"]
        dni = persona["numeroDocumento"]

        con = bd_conectar()

        cliente = Cliente(con)

        cliente.agregar(dni,nombres,apellidoPaterno,apellidoMaterno,"")

        clientes = cliente.obtener_registros()
        for i in clientes:
            print(i)
    else:
        print("El DNI no es válido")


def eliminar():
    con = bd_conectar()

    cliente = Cliente(con)

    cliente.eliminar("15751586")


def muestraApiConexion():

    con = bd_conectar()

    cliente = Cliente(con)
    clientes = cliente.obtener_registros()
    for i in clientes:
        print(i)


test_api()