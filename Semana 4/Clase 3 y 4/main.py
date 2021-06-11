# 10:
from tienda import Tienda
from producto import Producto
from vendedor import Vendedor
from cliente import Cliente


# 3:
nombreTienda = input("Ingrese el nombre de la tienda a crear: ")
paginaWeb = input("Ingrese la página web de la tienda: ")
direccion = input("Ingrese la dirección de la tienda: ")
tienda = Tienda(nombreTienda, paginaWeb, direccion, 80000)

# 7:
while True:
    instrucciones = """
        Ingrese NP para crear un nuevo producto, 
        I para imprimir los productos e inventarios
        V para ejecutar una venta
        TV para revisar el total de ventas
        NV para crear un nuevo vendedor
        NC para crear un nuevo cliente
    """
    operacion = input(instrucciones)

    if operacion == "NP":
        # 6:
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        productoCreado = Producto(nombre, precio)
        tienda.agregarProducto(productoCreado)
    elif operacion == "I":
        tienda.imprimirProductosEInventarios()
    elif operacion == "V":
        # 12: buscar un vendedor
        docVendedor = input("Por favor ingrese el documento del vendedor: ")
        vendedorEncontrado = tienda.buscarVendedorPorDocumento(docVendedor)

        # 13: buscar un cliente
        docCliente = input("Por favor ingrese el documento del cliente: ")
        clienteEncontrado = tienda.buscarClientePorDocumento(docCliente)

        # 9:
        nombreProducto = input(
            "Ingrese el nombre del producto que quiere comprar: ")
        productoEncontrado = tienda.buscarProductoPorNombre(nombreProducto)
        if not productoEncontrado:
            print("El producto no fue encontrado")
        elif not vendedorEncontrado:
            print("El vendedor no fue encontrado")
        elif not clienteEncontrado:
            print("El cliente no fue encontrado")
        else:
            cantidadAComprar = int(input("Ingrese la cantidad a comprar: "))
            if productoEncontrado.inventario >= cantidadAComprar:
                total = productoEncontrado.precio * cantidadAComprar
                print(
                    f"Venta Exitosa, el total de la venta es: ${total} pesos")
                productoEncontrado.inventario = productoEncontrado.inventario - cantidadAComprar
                tienda.totalVentas = tienda.totalVentas + total

                # 12: acumular totales en el vendedor
                vendedorEncontrado.acumular(total)
                vendedorEncontrado.revisarObjetivo()

                # 13: acumular totales en el cliente
                clienteEncontrado.acumular(total)
                aplicaDescuento = clienteEncontrado.revisarDescuento(
                    tienda.rangoDescuento)

                if aplicaDescuento:
                    total = total*90/100
                    print("El cliente obtuvo un descuento del 10%")
                    print(f"Lo que debe pagar es {total}")

                print(
                    f"El total de ventas realizadas en el día es de: ${tienda.totalVentas} pesos")
            else:
                print("No hay inventario suficiente de la referencia que desea comprar")
    elif operacion == "TV":
        tienda.mostrarTotalDeVentas()
    elif operacion == "NV":
        nombre = input("Ingrese el nombre del nuevo vendedor: ")
        telefono = input("Ingrese el teléfono del nuevo vendedor: ")
        correo = input("Ingrese el correo del nuevo vendedor: ")
        documento = input("Ingrese el documento del nuevo vendedor: ")
        objetivo = int(input("Ingrese el objetivo del nuevo vendedor: "))
        docEmpresarial = input(
            "Ingrese el docEmpresarial del nuevo vendedor: ")
        nuevoVendedor = Vendedor(
            nombre, telefono, correo, documento, objetivo, docEmpresarial)
        tienda.agregarVendedor(nuevoVendedor)
    elif operacion == "NC":
        nombre = input("Ingrese el nombre del nuevo cliente: ")
        telefono = input("Ingrese el teléfono del nuevo cliente: ")
        correo = input("Ingrese el correo del nuevo cliente: ")
        documento = input("Ingrese el documento del nuevo cliente: ")
        direccion = input("Ingrese la dirección de envío: ")
        correoFacturacion = input("Ingrese el correo de facturación: ")
        nuevoCliente = Cliente(nombre, telefono, correo,
                               documento, direccion, correoFacturacion)
        tienda.agregarCliente(nuevoCliente)
