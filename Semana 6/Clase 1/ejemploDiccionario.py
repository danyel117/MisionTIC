#hacer un diccionario en el que se relacione
# cada letra del alfabeto a un número
#A:1, B:2, C:3 ... Z:n
#hacer una función para convertir una palabra en números
#la palabra que ingresará tendrá todas las letras separadas por un espacio

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
    pass

letra = input("Ingrese la letra que quiera revisar: ")
print(letra,diccionario[letra.upper()])