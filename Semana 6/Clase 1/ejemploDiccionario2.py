#hacer un diccionario en el que se relacione
# un número a una letra del alfabeto
#1:A, 2:B, 3:C ... N:Z
#hacer una función para convertir una lista de números en una palabra
#se ingresará un string de números separados por espacios

#Ej. ingresa-> '1 2 3 4'
#    devuelve-> ['A', 'B', 'C', 'D']

#1. definir el diccionario con las relaciones entre números y letras

#2.crear una función para leer el string de números
    #en la función hacer un .split(' ') de la entrada
    #iterar cada dato que sale del split y revisar su valor en el diccionario
    #agregar cada valor a una lista
    #devolver la lista final

#1. crear el diccionario
diccionario = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'J',
    11:'K',
    12:'L',
    13:'M',
    14:'N',
    15:'O',
    16:'P',
    17:'Q',
    18:'R',
    19:'S',
    20:'T',
    21:'U',
    22:'V',
    23:'W',
    24:'X',
    25:'Y',
    26:'Z'
}

def convertirNumerosEnPalabras(texto):
    listaDeNumeros = texto.split(" ")
    print(listaDeNumeros)
    listaDeLetras = []
    for numero in listaDeNumeros:
        listaDeLetras.append(diccionario[int(numero)])
    return listaDeLetras


resultado = convertirNumerosEnPalabras('13 5 8 20 26 3')
print(resultado)
