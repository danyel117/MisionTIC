#hacer un diccionario en el que se relacione
# cada letra del alfabeto a un número
#A:1, B:2, C:3 ... Z:n
#hacer una función para convertir una palabra en números
#la palabra que ingresará tendrá todas las letras separadas por un espacio

#ejemplo: 
# entrada -> H O L A
# salida  -> 8 15 12 1

diccionario = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    'I':9,
    'J':10,
    'K':11,
    'L':12,
    'M':13,
    'N':14,
    'O':15,
    'P':16,
    'Q':17,
    'R':18,
    'S':19,
    'T':20,
    'U':21,
    'V':22,
    'W':23,
    'X':24,
    'Y':25,
    'Z':26,
}

def convertirLetrasANumeros(texto):
    listaLetras = texto.split(" ")
    print(listaLetras)
    listaNumeros = []
    for letra in listaLetras:
        listaNumeros.append(diccionario[letra])
    return listaNumeros

resultado = convertirLetrasANumeros("D A N I E L")
print(resultado)

