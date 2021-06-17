import numpy as np

# crear una lista simple
lista1 = np.array([1, 2, 3])
print(lista1)

# crear una matriz m x n de ceros
matrizCeros = np.zeros((5, 5))
print(matrizCeros)

# crear una matriz m x n de unos
matrizUnos = np.ones((4, 4))
print(matrizUnos)

# crear una matriz de m x n datos aleatorios entr 0 y 1
matrizAleatorios = np.random.random((5, 5))
print(matrizAleatorios)
matrizAleatoriosEnteros = np.random.randint(1, 100, (4, 4))
print(matrizAleatoriosEnteros)
