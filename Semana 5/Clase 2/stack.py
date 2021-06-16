listaEjemplo = [1, 10, -500, 800, -1234, -543, 123, 45]

print(listaEjemplo)

# primera forma:
# sacar el último dato de la posición 0
# ingresar un dato nuevo de la posición 0
# retirar el dato del elemento 0
datoRetirado = listaEjemplo.pop(0)
print(listaEjemplo)
# agregar un dato en la posición 0
listaEjemplo.insert(0, -500)
print(listaEjemplo)


def retirarDatos(lista):
    elementoRetirado = lista.pop(0)
    return lista


def agregarDato(lista, dato):
    lista.insert(0, dato)
    return lista


print("______________________")

# segunda forma:
# retirar el último dato de la lista
# agregar un dato nuevo al final de la lista
listaEjemplo = [-30, 45, 86, 97, -231, -925, 456]
print(listaEjemplo)
# retirar un dato del final de la lista
elementoRetirado = listaEjemplo.pop()
print(elementoRetirado)
print(listaEjemplo)
# argegar un dato al final de la lista
listaEjemplo.append(600)
print(listaEjemplo)


def retirarDato(lista):
    lista.pop()
    return lista


def agregarDato(lista, dato):
    lista.append(dato)
    return lista
