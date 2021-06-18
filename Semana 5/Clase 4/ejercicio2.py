import numpy as np

matrizEjemplo = np.array([[10, -234, 345, -90, 19],
                          [20, 36, -90, -32, 45],
                          [56, 13, 17, 65, 23],
                          [-14, -23, 35, 23, 21],
                          [-500, -32, 86, 32, 50]])

vectorAReemplazar = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

for index, data in np.ndenumerate(matrizEjemplo):
    # identificar el valor de i y j de cada dato de la matriz
    i = index[0]
    j = index[1]

    # revisar si un elemento hace parte del triángulo superior
    if i <= j:
        # revisar si el dato es mayor a 30.
        # si sí, reemplazarlo por un dato del vector
        if data > 30:
            siguienteDatoAIngresar = vectorAReemplazar.pop(0)
            matrizEjemplo[i][j] = siguienteDatoAIngresar

print(matrizEjemplo)
