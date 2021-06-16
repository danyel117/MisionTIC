# hacer una clase navegador con una lista de paginas visitadas
# hacer un método para navegar a una nueva página
# hacer un método para conocer el historial completo
# hacer un método para regresar a la página anterior
# cuando el navegador va hacia la página anterior,
# pierde la información de la página actual

# 1. crear una clase Navegador, que tenga dos atributos:
# página actual
# lista de páginas


class Navegador:
    def __init__(self, paginaInicial):
        self.paginaActual = paginaInicial
        self.listaDePaginas = []

    # 2. método para navegar a una nueva página
    def navegar(self):
        # pedir la url de la página a la que se quiera navegar
        url = input("Ingrese la página a la quiera navegar: ")
        # agregar la página actual al stack
        self.listaDePaginas.append(self.paginaActual)
        # actualizar la página actual del navegador
        self.paginaActual = url

    #3. método para regresar a la página anterior
    def regresar(self):
        # obtener la última página a la que se había navegado
        ultimaPagina = self.listaDePaginas.pop()
        self.paginaActual = ultimaPagina


navegador = Navegador("www.google.com")

while True:
    operaciones = """
        Ingrese N para navegar a una nueva página
        Ingrese H para conocer el historial completo
        Ingrese B para regresar a la página anterior
    """
    inputUsuario = input(operaciones)
    if inputUsuario == "N":
        navegador.navegar()
    elif inputUsuario == "H":
        print("Página actual: ", navegador.paginaActual)
        print("Historial anterior: ", navegador.listaDePaginas)
    elif inputUsuario == "B":
        navegador.regresar()
        print("Página actual: ", navegador.paginaActual)
