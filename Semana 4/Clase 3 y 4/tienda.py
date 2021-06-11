from producto import Producto

# 1:


class Tienda:
    # 2:
    def __init__(self, nombre, paginaWeb, direccion, rangoDescuento):
        self.nombre = nombre
        self.paginaWeb = paginaWeb
        self.direccion = direccion
        self.listaDeProductos = []
        self.listaDeVendedores = []
        self.listaDeClientes = []
        self.rangoDescuento = rangoDescuento
        self.totalVentas = 0
    # 5:

    def agregarProducto(self, productoAAgregar):
        self.listaDeProductos.append(productoAAgregar)
    # 8:

    def imprimirProductosEInventarios(self):
        for producto in self.listaDeProductos:
            print("Producto: ", producto.nombre)
            print("Inventario: ", producto.inventario)
            print("___________")

    # 9:
    def buscarProductoPorNombre(self, nombreProductoABuscar):
        for producto in self.listaDeProductos:
            if producto.nombre == nombreProductoABuscar:
                return producto
        return False

    def mostrarTotalDeVentas(self):
        print(
            f"El total de ventas acumuladas al momento es de: ${self.totalVentas} pesos")

    def agregarVendedor(self, vendedor):
        self.listaDeVendedores.append(vendedor)

    def buscarVendedorPorDocumento(self, documento):
        for vendedor in self.listaDeVendedores:
            if vendedor.documento == documento:
                return vendedor
        return False

    def agregarCliente(self, cliente):
        self.listaDeClientes.append(cliente)

    def buscarClientePorDocumento(self, documento):
        for cliente in self.listaDeClientes:
            if cliente.documento == documento:
                return cliente
        return False
