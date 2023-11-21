import random
class Cuenta():

    tipo_cuenta = 'Cuenta de Ahorros'.center(50, '-')
    print(tipo_cuenta)
    contador_i = -2

    @classmethod
    def contador_indice(cls):
        cls.contador_i += 1
        return cls.contador_i


    @classmethod
    def generar_siguiente_valor(cls):
        cls.contador = random.randint(1,1000)
        return cls.contador

    def __init__(self, titular= '', edad= '', documento= '', cantidad = 0):
        self.__titular = titular
        self.__edad = edad
        self.__documento = documento
        self.__cantidad = cantidad
        self.id_cuenta = Cuenta.generar_siguiente_valor()
        self.contador_i = Cuenta.contador_indice()
        self.lista_cuentas = []

    @property
    def titular(self):
        return self.__titular
    
    @titular.setter
    def tiular(self, valor_nuevo):
        self.__titular = valor_nuevo

    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor_nuevo):
        self.__edad = valor_nuevo

    @property
    def documento(self):
        return self.__documento
    
    @documento.setter
    def documento(self, valor_nuevo):
        self.__documento = valor_nuevo

    @property
    def cantidad(self):
       return self.__cantidad
    
    @cantidad.setter
    def cantidad(self, valor_nuevo):
        self.__cantidad = valor_nuevo

    def ingresar_cantidad(self, valor_nuevo, persona_nueva):
        if valor_nuevo >= 0:
            persona_nueva.__cantidad += valor_nuevo
            print('Consignación exitosa.')
            print(f'Saldo actual: {persona_nueva.__cantidad}')

        else:
            self.__cantidad = 0
            print(f'Dato ingresado invalido {valor_nuevo}')

    def retirar_cantidad(self, valor_nuevo, persona_nueva):
        if valor_nuevo <= persona_nueva.__cantidad:
            persona_nueva.__cantidad -= valor_nuevo
            print('Retiro exitoso.')
            print(f'Saldo actual: {persona_nueva.__cantidad}')

        else:
            print(f'Dato ingresado invalido {valor_nuevo}')

    def buscar_cliente(self, documento_nuevo):
        for cuenta in self.lista_cuentas:
            if cuenta.__documento == documento_nuevo:
                return cuenta
        else:
            return False
    
    def titular_valido(self, edad_titular):
        if edad_titular >= 26:
            return True
        else:
            return False
    
    def agregar_cuenta(self, valor_nuevo):
        self.lista_cuentas.append(valor_nuevo)

    def eliminar_cuenta(self, valor_nuevo):
        self.lista_cuentas.remove(self.lista_cuentas[valor_nuevo])

    def __str__(self):
        return f'Número de cuenta: {self.id_cuenta} | Titular de la cuenta: {self.__titular} | Edad: {self.__edad} | Documento: {self.__documento} | Saldo disponible: ${self.__cantidad}'
    
    def cuenta_detalles(self):
        for cuenta in self.lista_cuentas:
            #print (f'Número de cuenta: {cuenta.id_cuenta} |  Titular de la cuenta: {cuenta.__titular} | Edad: {cuenta.__edad} | Documento: {cuenta.__documento} | Saldo disponible: ${cuenta.__cantidad}')
            print (cuenta.__str__())


nueva_cuenta = Cuenta()


while True:

    instrucciones = '''
    Ingrese A para registrar una nueva cuenta
    Ingrese I para ingresar dinero a su cuenta
    Ingrese R para retirar dinero de su cuenta
    Ingrese C para imprimir los detalles de la cuenta
    Ingrese E para eliminar una cuenta
    
    '''

    operacion = input(instrucciones)

    if operacion == 'A':
        titular = input('Ingrese el nombre del titular de la cuenta: ')
        documento = int(input('Ingrese el documento del titular de la cuenta: '))
        edad = int(input('Ingrese la edad del titular de la cuenta: '))
        prueba = nueva_cuenta.titular_valido(edad)
        if not prueba:
            print('Su edad no se encuentra en el rango de edad correspondiente para crear una cuenta de este tipo.')
            print('Rango de edad necesario: (26+)')
        else:
            nueva = Cuenta(titular, edad, documento)
            nueva_cuenta.agregar_cuenta(nueva)
            print('Cuenta añadida exitosamente.')
    
    elif operacion == 'I':
        documento = int(input('Ingrese el documento del titular de la cuenta: '))
        cuenta_encontrada = nueva_cuenta.buscar_cliente(documento)
        if not cuenta_encontrada:
            print('Número de documento no asociado a ninguna cuenta.')
        else:
            valor_nuevo = int(input('Ingrese el valor a consignar a su cuenta: '))
            nueva_cuenta.ingresar_cantidad(valor_nuevo, cuenta_encontrada)
    
    elif operacion == 'R':
        documento = int(input('Ingrese el número de documento del titular de la cuenta: '))
        cuenta_encontrada = nueva_cuenta.buscar_cliente(documento)
        if not cuenta_encontrada:
            print('Número de documento no asociado a ninguna cuenta.')
        else:
            valor_nuevo = int(input('Ingrese el valor a retirar de su cuenta: '))
            nueva_cuenta.retirar_cantidad(valor_nuevo, cuenta_encontrada)
    
    elif operacion == 'C':
        nueva_cuenta.cuenta_detalles()

    elif operacion == 'E':
        documento = int(input('Ingrese el número de documento del titular de la cuenta: '))
        cuenta_encontrada = nueva_cuenta.buscar_cliente(documento)
        if not cuenta_encontrada:
            print('Número de documento no asociado a ninguna cuenta.')
        else:
            nueva_cuenta.eliminar_cuenta(cuenta_encontrada.contador_i)
            print(f'Cuenta número: {cuenta_encontrada} eliminada de la base de datos.')

    
    
    break    
