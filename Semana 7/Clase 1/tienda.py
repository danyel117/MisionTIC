#1. crear una clase Tienda que tenga los siguientes atributos:
    #nombre
    #direccion
    #telefono
    #lista de productos
    #lista de clientes
    #histórico de ventas
class Tienda:
    def __init__(self, nombre,direccion,telefono):
        self.nombre=nombre
        self.direccion=direccion
        self.telefono=telefono
        self.productos=[]
        self.clientes=[]
        self.ventas=[]

#2. crear una clase Producto que tenga los siguientes atributos:
    #nombre
    #precio

class Producto:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio

#3. crear una clase Cliente que tenga los siguientes atributos:
    #nombre
    #documento
    #lista de compras
class Cliente:
    def __init__(self,nombre,documento):
        self.nombre=nombre
        self.documento=documento
        self.compras=[]

#4. crear una clase Venta que tenga los siguientes atributos:
    #fecha
    #lista de productos y cantidades
    #cliente
class Venta:
    def __init__(self,cliente,fecha):
        self.cliente=cliente
        self.fecha=fecha
        self.productos=[]