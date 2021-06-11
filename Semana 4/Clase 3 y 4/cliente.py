from persona import Persona


class Cliente(Persona):
    def __init__(self, nombre, telefono, correo, documento, direccionEnvio, correoFacturacion):
        super().__init__(nombre, telefono, correo, documento)
        self.direccionEnvio = direccionEnvio
        self.correoFacturacion = correoFacturacion
        self.acumuladoCompra = 0

    def acumular(self, monto):
        self.acumuladoCompra = self.acumuladoCompra + monto

    def revisarDescuento(self, rangoDescuento):
        if self.acumuladoCompra >= rangoDescuento:
            return True
        else:
            return False
