import numpy as np
#calcular el max y el min y las posiciones de los elementos en rojo

matrizEjemplo = np.array([[10, -234, 345, -90, 19],
                          [20, 36, -90, -32, 45],
                          [56, 13, 17, 65, 23],
                          [-14, -23, 35, 23, 21],
                          [-500, -32, 86, 32, 50]])

maximo = matrizEjemplo.min()
posicionMax = (0, 0)
minimo = matrizEjemplo.max()
posicionMin = (0, 0)
for index, data in np.ndenumerate(matrizEjemplo):
    i = index[0]
    j = index[1]
    if i+j >= 4 and (i+j) % 2 == 0:
        if data >= maximo:
            maximo = data
            posicionMax = index
        if data <= minimo:
            minimo = data
            posicionMin = index


print(maximo, posicionMax)
print(minimo, posicionMin)
