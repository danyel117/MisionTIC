import random

#hacer una clase que se llame CuentaBancaria.
#artibutos: 
# numero de la cuenta -> es aleatorio entre 1.000 y 10.000
# saldo
#métodos:
# retirar
# depositar

#ejercicio: agregar condición que saque error si el saldo es negativo
#ejercicio: cobrar una comisión del 4 pesos por cada 1000 cuando el monto de la consignación sea mayor a 10.000

#ejercicio opcional: crear una lista de cuentas y agregar la posibilidad de crear una cuenta nueva o eliminar una cuenta
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

    def consignar(self,monto):
        self.saldo = self.saldo + monto

    def consultarSaldo(self):
        print("Cuenta: ",self.numeroCuenta)
        print("Saldo: ",self.saldo)
        print("________________")


saldoInicial = float(input("Bienvenido al banco XYZ. Para crear su cuenta bancaria, ingrese el saldo inicial de la cuenta: "))
cuenta = CuentaBancaria(saldoInicial)
while True:
    operacion = input("Ingrese S para consultar el saldo, R para retirar y C para consignar: ")
    if operacion == "S":
        cuenta.consultarSaldo()
    elif operacion == "R":
        monto = float(input("Ingrese el monto que quiere retirar: "))
        cuenta.retirar(monto)
    elif operacion == "C":
        monto = float(input("Ingrese el monto que quiere consignar: "))
        cuenta.consignar(monto)
        print("Consignación exitosa")
    else:
        print("Operación incorrecta")
        