matriz = [[10, -234, 345, -90, 19],
          [20, 36, -90, -32, 45],
          [56, 13, 17, 65, 23],
          [-14, -23, 35, 23, 21],
          [-500, -32, 86, 32, 50]]

# imprimir la matriz
print(matriz)

# acceder a cada elemento de la matriz
print(matriz[0][3])

matriz[3][2] = -500
print(matriz)


for i, row in enumerate(matriz):
    for j, item in enumerate(row):
        print(i, j, item)

# identificar si un elemento hace parte de la diagonal
for i, fila in enumerate(matriz):
    print("fila:", i, fila)
    for j, elemento in enumerate(fila):
        if i == j:
            print(f"el elemento {elemento} hace parte de la diagonal")
        print(i, j, elemento)

# contar cuántos números pares hay en la diagonal de la matriz
# identificar si un elemento hace parte de la diagonal
contadorParesDiagonales = 0
for i, fila in enumerate(matriz):
    print("fila:", i, fila)
    for j, elemento in enumerate(fila):
        if i == j:
            print(f"el elemento {elemento} hace parte de la diagonal")
            if elemento % 2 == 0:
                print(f"el elemento {elemento} es par")
                contadorParesDiagonales = contadorParesDiagonales + 1
        print(i, j, elemento)
print("el contador de pares diagonales es:", contadorParesDiagonales)
