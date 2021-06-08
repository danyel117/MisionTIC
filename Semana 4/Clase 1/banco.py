import random

#ejercicio opcional: crear una lista de cuentas y agregar la posibilidad 
# de crear una cuenta nueva o eliminar una cuenta
    #cuando se vaya a retitar o a consignar, se debe ingresar el número de la cuenta

# ejercicio opcional: crear una clase persona y a la clase cuenta agregarle una persona pidiéndole su cédula. 
#Hay que construir una lista de personas. Si la persona no existe, se debe crear.

class CuentaBancaria:
    def __init__(self,saldoInicial):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial
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
    numCuenta = int(input(mensajeOperacion))
    #buscar la cuenta del usuario. Cuando se encuentre, imprimir el saldo
    for cuenta in listaDeCuentas:
        if cuenta.numeroCuenta == numCuenta:
            return [True,cuenta]
    return [False]

listaDeCuentas = []

while True:
    operacion = input("Ingrese N para crear una nueva cuenta, S para consultar el saldo, R para retirar y C para consignar: ").upper()
    if operacion == "N":
        saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
        cuenta = CuentaBancaria(saldoInicial)
        listaDeCuentas.append(cuenta)
        print("Cuenta creada con éxito. El número de la cuenta es ", cuenta.numeroCuenta)
    elif operacion == "S":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta que quiere consultar",listaDeCuentas)
        if resultadoBusqueda[0]:
            cuenta = resultadoBusqueda[1]
            cuenta.consultarSaldo()
        else:
            print("Cuenta no encontrada")
    elif operacion == "R":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta de la quiere retirar", listaDeCuentas)
        if resultadoBusqueda[0]:
            monto = float(input("Ingrese el monto que quiere retirar: "))
            cuenta = resultadoBusqueda[1]
            cuenta.retirar(monto)
        else:
            print("Cuenta no encontrada")
    elif operacion == "C":
        resultadoBusqueda = buscarCuentas("Por favor ingrese la cuenta a la quiere consignar", listaDeCuentas)
        if resultadoBusqueda[0]:
            monto = float(input("Ingrese el monto que quiere consignar: "))
            cuenta = resultadoBusqueda[1]
            cuenta.consignar(monto)
            print("Consignación exitosa")
        else:
            print("Cuenta no encontrada")
    else:
        print("Operación incorrecta")
        