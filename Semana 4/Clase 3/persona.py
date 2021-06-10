class Persona:
    #init es el constructor de la clase
    def __init__(self, nombre, telefono, correo, documento): 
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo
        self.documento = documento

class Vendedor(Persona):
    def __init__(self, nombre, telefono, correo, documento, objetivoVentas, identificacionEmpresarial):
        super().__init__(nombre, telefono, correo, documento)
        self.objetivoVentas = objetivoVentas
        self.identificacionEmpresarial = identificacionEmpresarial
        self.acumuladoVentas = 0

    def imprimirNombre(self):
        print(self.nombre)

#hacer la clase Cliente
    #tiene todos los atributos de Persona mas:
        # total acumulado de compra
        # dirección de envío
        # correo de facturación



persona1 = Vendedor("Daniel","132","dsl@c.com","54",100000,"EMPLEADO001")
persona2 = Persona("Miguel","132","miguel@c.com","54")

print(persona1.nombre)
persona1.imprimirNombre()

print(persona2.nombre,persona2.correo)