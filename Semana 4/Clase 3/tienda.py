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
    
    #9:
    def buscarProductoPorNombre(self,nombreProductoABuscar):
        for producto in self.listaDeProductos:
            if producto.nombre == nombreProductoABuscar:
                return producto
        return False
