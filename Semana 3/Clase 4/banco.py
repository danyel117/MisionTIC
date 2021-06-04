import random

#hacer una clase que se llame CuentaBancaria.
#artibutos: 
# numero de la cuenta -> es aleatorio entre 1.000 y 10.000
# saldo
#métodos:
# retirar
# depositar

#ejercicio: agregar condición que saque error si el saldo es negativo

class CuentaBancaria:
    def __init__(self,saldoInicial):
        self.numeroCuenta = random.randint(1000,10000)
        self.saldo = saldoInicial

    def retirar(self, monto):
        self.saldo = self.saldo - monto

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
        print("Retiro Exitoso")
    elif operacion == "C":
        monto = float(input("Ingrese el monto que quiere consignar: "))
        cuenta.consignar(monto)
        print("Consignación exitosa")
    else:
        print("Operación incorrecta")
        