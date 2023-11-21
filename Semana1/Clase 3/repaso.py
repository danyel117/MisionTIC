#imprimir un texto simple
print("Buenos días")

#imprimir varios textos separados por espacios
print("texto1", "texto2")

#concatenar textos
primerTexto = "hola"
segundoTexto = "mundo"
holaMundo = primerTexto + " " +segundoTexto
print(holaMundo)

#formatear textos con variables
miEdad = 10
print(f"yo tengo {miEdad} años")

#nombramiento de variables
#manera 1: PascalCase
VariablePascalCase = "soy un variable con todas las iniciales mayusculas"

#manera 2: camelCase
variableCamelCase = "primera palabra todo minúscula y las siguientes palabras con la inicial mayúscula"

#manera 3: snake_case
variable_snake_case = "poner las palabras separadas por un _"

#Operaciones aritméticas
miEdad = 10
edadDeMiMama = 40

#operación de resta
diferenciaDeEdad = edadDeMiMama - miEdad
#operación de suma
sumaDeEdades = edadDeMiMama + miEdad

#operaciones de multiplicación y división
variable1 = 10
variable2 = 15.5
multiplicacion = variable1 * variable2
division = variable1 / variable2 #cuidado de no dividir por 0 porque sale un error


#jerarquía de las operaciones: potenciación > multiplicación y división > sumas y restas
variable1 = 10
variable2 = 50
variable3 = 20.7
variable4 = -10.1

#primero sumar v1 y v2, despues restar v3 y v4 y dividir esos dos resultados
resultado1 = (variable1 + variable2) / (variable3 - variable4)

#comando de input general de tipo texto
inputDelUsuario = input("por favor ingrese un valor: ")

#comando de input de tipo numerico
inputNumerico = int(input("Por favor ingrese un valor numerico"))
print(inputNumerico)

