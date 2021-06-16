# definir una lista
lista = [1, 5, 2345, 213, -12, 234, 1, 10]
# _______0  1   2     3    4   5   6   7

# imprimir una lista
print(lista)

# acceder a un dato a través del índice
lista[2] = -50
print(lista)

# imprimir un dato específico
print(lista[4])

# agregar un dato al final de una lista
lista.append(17)
print(lista)

# agregar un dato en una posición específica
lista.insert(0, -500)
print(lista)

# eliminar datos de una lista según su valor
lista.remove(5)
print(lista)

# eliminar el primer dato de una lista, sea cual sea
lista.remove(lista[0])
print(lista)

# eliminar el último valor de la lista
lista.pop()
print(lista)

# eliminar un valor según su posición
lista.pop(2)
print(lista)

# organizar una lista
lista.sort()
print(lista)

# revisar si un elemento pertenece a la lista
print(-500 in lista)
print(1 in lista)

# revisar la longitud de la lista
print(len(lista))

# slicing
print(lista[1:4])
print(lista[:4])
print(lista[3:])


