from Cuenta import Cuenta

class CuentaJoven(Cuenta):

    tipo_cuenta = 'Cuenta de Ahorros Joven'.center(50, '-')
    print(tipo_cuenta)

    def __init__(self, titular='', edad = '', documento='', cantidad=0):
        super().__init__(titular, edad, documento, cantidad)
        self.__bonificacion = 0.5
        self.__edad = edad

    @property
    def bonificacion(self):
        return self.__bonificacion
    
    @bonificacion.setter
    def bonificacion(self, nuevo_valor):
        self.__bonificacion = nuevo_valor
    
    @property
    def edad(self):
        return self.__edad
    
    @edad.setter
    def edad(self, valor_nuevo):
        self.__edad = valor_nuevo

    def titular_valido(self, edad_titular):
        if edad_titular >= 18 and edad_titular <= 25:
            return True
        else:
            return False


    def __str__(self):
        return (f'{super().__str__()} | Bonificación: {self.__bonificacion} ')

  #  def cuenta_detalles(self):
   #     for cuenta in self.lista_cuentas:
    #        print (cuenta.__str__())

    
nueva_cuenta_joven = CuentaJoven()

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
        prueba = nueva_cuenta_joven.titular_valido(edad)
        if not prueba:
            print('Su edad no se encuentra en el rango de edad correspondiente para crear una cuenta de este tipo.')
            print('Rango de edad necesario: (18 - 25 años)')
        else:
            nueva = CuentaJoven(titular, edad, documento)
            nueva_cuenta_joven.agregar_cuenta(nueva)
            print('Cuenta añadida exitosamente.')
    
    elif operacion == 'I':
        documento = int(input('Ingrese el documento del titular de la cuenta: '))
        cuenta_encontrada = nueva_cuenta_joven.buscar_cliente(documento)
        if not cuenta_encontrada:
            print('Número de documento no asociado a ninguna cuenta.')
        else:
            valor_nuevo = int(input('Ingrese el valor a consignar a su cuenta: '))
            valor_nuevo_bonificacion = valor_nuevo * nueva_cuenta_joven.bonificacion / 100
            valor_nuevo += valor_nuevo_bonificacion
            nueva_cuenta_joven.ingresar_cantidad(valor_nuevo, cuenta_encontrada)

    elif operacion == 'R':
        documento = int(input('Ingrese el número de documento del titular de la cuenta: '))
        cuenta_encontrada = nueva_cuenta_joven.buscar_cliente(documento)
        if not cuenta_encontrada:
            print('Número de documento no asociado a ninguna cuenta.')
        else:
            valor_nuevo = int(input('Ingrese el valor a retirar de su cuenta: '))
            nueva_cuenta_joven.retirar_cantidad(valor_nuevo, cuenta_encontrada)
    
    elif operacion == 'C':
        nueva_cuenta_joven.cuenta_detalles()
    
    elif operacion == 'E':
        documento = int(input('Ingrese el número de documento del titular de la cuenta: '))
        cuenta_encontrada = nueva_cuenta_joven.buscar_cliente(documento)
        if not cuenta_encontrada:
            print('Número de documento no asociado a ninguna cuenta.')
        else:
            nueva_cuenta_joven.eliminar_cuenta(cuenta_encontrada.contador_i)
            print(f'Cuenta número: {cuenta_encontrada} eliminada de la base de datos.')    
 
    