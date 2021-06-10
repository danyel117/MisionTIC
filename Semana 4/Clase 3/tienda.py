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
    
    def buscarProductoPorNombre(self,nombreProductoABuscar):
        for producto in self.listaDeProductos:
            if producto.nombre == nombreProductoABuscar:
                return producto
        return False



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
    elif operacion == "I":
        tienda.imprimirProductosEInventarios()
    elif operacion == "V":
        nombreProducto = input("Ingrese el nombre del producto que quiere comprar: ")
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)
        if not productoEncontrado:
            print("El producto no fue encontrado")
        else:
            cantidadAComprar = int(input("Ingrese la cantidad a comprar: "))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar
                print(f"Venta Exitosa, el total de la venta es: ${total} pesos")
                productoEncontrado.inventario -= cantidadAComprar
            else:
                print("No hay inventario suficiente de la referencia que desea comprar")


