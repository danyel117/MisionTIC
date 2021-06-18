import numpy as np

matrizEjemplo = np.array([[10, -234, 345, -90, 19],
                          [20, 36, -90, -32, 45],
                          [56, 13, 17, 65, 23],
                          [-14, -23, 35, 23, 21],
                          [-500, -32, 86, 32, 50]])

tamano = matrizEjemplo.shape
print(tamano)

sumatoriaDiagonalPPal = 0
productoriaDiagonalInversa = 1

for index, data in np.ndenumerate(matrizEjemplo):
    # identificar el valor de i y j de cada dato de la matriz
    i = index[0]
    j = index[1]

    # identificar si un dato está en la diagonal principal
    if i == j:
        print("diagonal ppal: ", data)
        if data > 20:
            # obtener la suma de los datos mayores a 20
            sumatoriaDiagonalPPal = sumatoriaDiagonalPPal + data

    # identificar si un dato está en la diagonal inversa
    if (tamano[0] - i - 1) == j:
        print("diagonal inversa", data)
        if data < 0:
            # obtener la productoria de los datos negativos
            productoriaDiagonalInversa = productoriaDiagonalInversa * data

print("sumatoria", sumatoriaDiagonalPPal)
print("producto", productoriaDiagonalInversa)
# sumar ambos resultados
print("resultado final", sumatoriaDiagonalPPal + productoriaDiagonalInversa)
