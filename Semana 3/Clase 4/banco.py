import random

#hacer una clase que se llame CuentaBancaria.
#artibutos: 
# numero de la cuenta -> es aleatorio entre 1.000 y 10.000
# saldo
#métodos:
# retirar
# depositar

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

cuenta1 = CuentaBancaria(10000)
cuenta1.consultarSaldo()
cuenta1.retirar(500)
cuenta1.consultarSaldo()
cuenta1.consignar(20000)
cuenta1.consultarSaldo()