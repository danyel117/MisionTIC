import numpy as np
import math

matrizEjemplo = np.array([[10, -234, 345, -90, 19],
                          [20, 36, -90, -32, 45],
                          [56, 13, 17, 65, 23],
                          [-14, -23, 35, 23, 21],
                          [-500, -32, 86, 32, 50]])

contadorPerfectos = 0

for index, data in np.ndenumerate(matrizEjemplo):
    # identificar el valor de i y j de cada dato de la matriz
    i = index[0]
    j = index[1]

    # identificar si el elemento está en el triángulo inferior:
    if i >= j:
        print(data)
        # obtener la raíz cuadrada del dato si es mayor a 0
        if data > 0:
            raiz = math.sqrt(data)
            print(raiz)
            # identificar si la raiz es un numero natural
            if raiz.is_integer():
                contadorPerfectos = contadorPerfectos + 1

print("la cantidad de raices perfectas es:", contadorPerfectos)
