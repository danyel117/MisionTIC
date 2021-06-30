import json
import csv
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
    #definir un método para agregar un nuevo producto
    def agregarProducto(self,producto):
        self.productos.append(producto)
        self.convertirProductosADiccionario()
    
    def imprimirProductos(self):
        for producto in self.productos:
            print(producto)

    def convertirProductosADiccionario(self):
        diccProductos={"productos":[]}
        for producto in self.productos:
            diccProductos["productos"].append({"nombre":producto.nombre,"precio":producto.precio})
            # diccProductos["productos"].append(producto.__dict__)
        with open('productos.json','w') as jsonFile:
            json.dump(diccProductos,jsonFile)
            jsonFile.close()

    def convertirDiccionarioAProductos(self):
        with open('productos.json') as jsonFile:
            diccionarioProductos = json.load(jsonFile)
            jsonFile.close()
        for producto in diccionarioProductos["productos"]:
            nuevoProducto = Producto(producto["nombre"],producto["precio"])
            self.productos.append(nuevoProducto)

    #definir un método para agregar un nuevo cliente
    def agregarCliente(self,cliente):
        self.clientes.append(cliente)
        self.convertirClientesADiccionario()
    
    def imprimirClientes(self):
        for cliente in self.clientes:
            print(cliente)

    def convertirClientesADiccionario(self):
        diccClientes = {"clientes":[]}
        for cliente in self.clientes:
            diccClientes["clientes"].append({"nombre":cliente.nombre,"documento":cliente.documento})
        
        with open('clientes.json','w') as jsonFile:
            json.dump(diccClientes,jsonFile)
            jsonFile.close()

    def convertirDiccionarioAClientes(self):
        with open('clientes.json') as jsonFile:
            diccionarioClientes = json.load(jsonFile)
        for cliente in diccionarioClientes["clientes"]:
            nuevoCliente = Cliente(cliente["nombre"],cliente["documento"])
            self.clientes.append(nuevoCliente)

    #hacer métodos para buscar un producto y un cliente
    def buscarProducto(self,nombreProducto):
        for producto in self.productos:
            if producto.nombre == nombreProducto:
                return producto
        return False 
    
    def buscarCliente(self,documento):
        for cliente in self.clientes:
            if cliente.documento == documento:
                return cliente
        return False

    #agregar métodos para crear e imprimir una nueva venta
    def agregarVenta(self,venta):
        self.ventas.append(venta)
        self.convertirVentasACSV()
    
    def imprimirVentas(self):
        for venta in self.ventas:
            print(venta)

    def convertirVentasACSV(self):
        diccVentas = []
        columnas = ["fecha","cliente","producto","cantidad"]
        for venta in self.ventas:
            diccVentas.append({"fecha":venta.fecha,"cliente":venta.cliente.documento,"producto":venta.producto.nombre,"cantidad":venta.cantidad})
        print(diccVentas)
        with open('ventas.csv','w') as csvFile:
            writer = csv.DictWriter(csvFile,columnas)
            writer.writeheader()
            writer.writerows(diccVentas)


#2. crear una clase Producto que tenga los siguientes atributos:
    #nombre
    #precio
class Producto:
    def __init__(self,nombre, precio):
        self.nombre=nombre
        self.precio=precio
    
    def __str__(self):
        return self.nombre + " - " + str(self.precio)

#3. crear una clase Cliente que tenga los siguientes atributos:
    #nombre
    #documento
    #lista de compras
class Cliente:
    def __init__(self,nombre,documento):
        self.nombre=nombre
        self.documento=documento
        self.compras=[]

    def __str__(self):
        return self.nombre + " - " + self.documento
    

#4. crear una clase Venta que tenga los siguientes atributos:
    #fecha
    #lista de productos y cantidades
    #cliente
class Venta:
    def __init__(self,cliente,fecha,producto,cantidad):
        self.cliente=cliente
        self.fecha=fecha
        self.producto = producto
        self.cantidad = cantidad
    
    def __str__(self):
        return self.cliente.documento + " - " + self.producto.nombre + " - " + str(self.cantidad)


#crear la lógica de la aplicación
tienda = Tienda("Tienda MisionTIC","calle 123","321")

try:
    tienda.convertirDiccionarioAProductos()
except:
    print("No existe el archivo de productos. Inicializando desde 0")

try:
    tienda.convertirDiccionarioAClientes()
except:
    print("No existe el archivo de clientes. Inicializando desde 0")

while True:
    instrucciones="""
        ingrese P para agregar un nuevo producto a la tienda
        ingrese IP para imprimir los productos de la tienda
        ingrese C para agregar un nuevo cliente a la tienda
        ingrese IC para imprimir los clientes de la tienda
        ingrese V para generar una venta
        ingrese IV para imprimir las ventas
    """
    operacion = input(instrucciones)
    if operacion == "P":
        nombreProducto=input("ingrese el nombre del producto: ")
        precioProducto=float(input("Ingrese el precio del producto: "))
        nuevoProducto = Producto(nombreProducto,precioProducto)
        tienda.agregarProducto(nuevoProducto)
    elif operacion == "IP":
        tienda.imprimirProductos()
        tienda.convertirProductosADiccionario()
    elif operacion == "C":
        nombreCliente = input("ingrese el nombre del cliente: ")
        documentoCliente = input("ingrese el documento del cliente: ")
        nuevoCliente = Cliente(nombreCliente,documentoCliente)
        tienda.agregarCliente(nuevoCliente)
    elif operacion == "IC":
        tienda.imprimirClientes()
    elif operacion == "V":
        nombreProducto = input("ingrese el nombre del producto: ")
        productoEncontrado=tienda.buscarProducto(nombreProducto)
        print(productoEncontrado)
        documentoCliente = input("ingrese el documento del cliente: ")
        clienteEncontrado=tienda.buscarCliente(documentoCliente)
        print(clienteEncontrado)
        cantidad = input("Ingrese la cantidad de producto que desea comprar: ")
        nuevaVenta = Venta(clienteEncontrado,"30/06/2021",productoEncontrado,cantidad)
        tienda.agregarVenta(nuevaVenta)
    elif operacion == "IV":
        tienda.imprimirVentas()