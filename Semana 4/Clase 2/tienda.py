#1:
class Tienda:
    #2:
    def __init__(self,nombre,paginaWeb,direccion):
        self.nombre = nombre
        self.paginaWeb = paginaWeb
        self.direccion = direccion
        self.listaDeProductos = []


#3:
nombreTienda = input("Ingrese el nombre de la tienda a crear: ")
paginaWeb = input("Ingrese la página web de la tienda: ")
direccion = input("Ingrese la dirección de la tienda: ")
tienda = Tienda(nombreTienda,paginaWeb,direccion)



