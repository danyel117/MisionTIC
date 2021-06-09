from producto import Producto

#1:
class Tienda:
    #2:
    def __init__(self,nombre,paginaWeb,direccion):
        self.nombre = nombre
        self.paginaWeb = paginaWeb
        self.direccion = direccion
        self.listaDeProductos = []
    #5:
    def agregarProducto(self,productoAAgregar):
        self.listaDeProductos.append(productoAAgregar)
    #8:
    def imprimirProductosEInventarios(self):
        for producto in self.listaDeProductos:
            print("Producto: ",producto.nombre)
            print("Inventario: ",producto.inventario)
            print("___________")



#3:
nombreTienda = input("Ingrese el nombre de la tienda a crear: ")
paginaWeb = input("Ingrese la página web de la tienda: ")
direccion = input("Ingrese la dirección de la tienda: ")
tienda = Tienda(nombreTienda,paginaWeb,direccion)


#7:
while True:
    operacion = input("Ingrese NP para crear un nuevo producto, I para imprimir los productos e inventarios: ")
    if operacion == "NP":
        #6:
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        productoCreado = Producto(nombre,precio)
        tienda.agregarProducto(productoCreado)
        print(tienda.listaDeProductos)
    elif operacion == "I":
        tienda.imprimirProductosEInventarios()


