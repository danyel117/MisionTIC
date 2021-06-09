import random
from persona import Persona

#ejercicio opcional: crear una lista de cuentas y agregar la posibilidad 
# de crear una cuenta nueva o eliminar una cuenta
    #cuando se vaya a retitar o a consignar, se debe ingresar el número de la cuenta

# ejercicio opcional: crear una clase persona y a la clase cuenta agregarle una persona pidiéndole su cédula. 
#Hay que construir una lista de personas. Si la persona no existe, se debe crear.

class CuentaBancaria:
    def __init__(self,saldoInicial,personaPropietaria):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial
        self.propietario = personaPropietaria
    def retirar(self, monto):
        if monto > self.saldo:
            print("Fondos insuficientes")
        else:
            self.saldo = self.saldo - monto
            print("Retiro Exitoso")
    def consignar(self, monto):
        if monto > 10000:
            comision = monto * 4 / 1000
            monto = monto - comision
            print("La comisión por la consignación es de: ", comision)
            self.saldo = self.saldo + monto
        else:
            self.saldo = self.saldo + monto
    def consultarSaldo(self):
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo: ",self.saldo)
        print("________________")

def buscarCuentas(mensajeOperacion, listaDeCuentas):
    #pedir el número de la cuenta al usuario
    numCuentaABuscar = int(input(mensajeOperacion))
    #buscar la cuenta del usuario. Cuando se encuentre, imprimir el saldo
    for cuentaIteracion in listaDeCuentas:
        if cuentaIteracion.numeroCuenta == numCuentaABuscar:
            return cuentaIteracion
    return False

def buscarPersona(cedula,listaDePersonas):
    for persona in listaDePersonas:
        if persona.documento == cedula:
            return persona
    return False

listaDeCuentas = []
listaDePersonas = []

while True:
    operacion = input("Ingrese N para crear una nueva cuenta, S para consultar el saldo, R para retirar y C para consignar: ").upper()
    if operacion == "N":
        saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
        
        #por hacer:
        #1. pedirle la cédula al usuario.
        cedula  = input("Por favor ingrese su cédula: ")
        #2. buscar el usuario. Si existe, asociar la cuenta a ese usuario.
        personaEncontrada = buscarPersona(cedula,listaDePersonas)
        #3. si no existe, preguntar la info personal de la persona, crear la persona y asociar la nueva cuenta a esa persona
        if not personaEncontrada:
            #crear una nueva persona
            nuevaPersona = Persona("Daniel",48, 23434, "dsl@c.com","sfdsf","Colombiano","ingeniero","1065377193")
            listaDePersonas.append(nuevaPersona)
            #crear una nueva cuenta bancaria y asociarla a la persona recientemente creada
            nuevaCuenta = CuentaBancaria(saldoInicial, nuevaPersona)
            listaDeCuentas.append(nuevaCuenta)
        else:
            #crear una nueva cuenta bancaria y asociarla a la persona recientemente creada
            nuevaCuenta = CuentaBancaria(saldoInicial, personaEncontrada)
            listaDeCuentas.append(nuevaCuenta)

        print("Cuenta creada con éxito. El número de la cuenta es ", nuevaCuenta.numeroCuenta)
    elif operacion == "S":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere consultar",listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada")
        else:
            resultadoBusqueda.consultarSaldo()
    elif operacion == "R":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta de la quiere retirar", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada")
        else:
            monto = float(input("Ingrese el monto que quiere retirar: "))
            resultadoBusqueda.retirar(monto)
    elif operacion == "C":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta a la quiere consignar", listaDeCuentas)
        if not resultadoBusqueda:
            print("Cuenta no encontrada")
        else:
            monto = float(input("Ingrese el monto que quiere consignar: "))
            resultadoBusqueda.consignar(monto)
            print("Consignación exitosa")
    else:
        print("Operación incorrecta")
        