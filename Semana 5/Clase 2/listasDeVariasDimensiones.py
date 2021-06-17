# lista de numeros
lista = [1, 54, 32, -10, 24]

# lista de textos
lista = ["Daniel", "Miguel", "Felipe", "Susana"]

# listas combinadas
lista = ["hola", 1, 334, "Daniel", 224, "dszfsdf"]

# listas de varias dimensiones
lista = [[1,    2,     3], 
         [4,    5,     6], 
         [987, -325, -927]]


for i in lista:
    for j in i:
        print(j)

for row in lista:
    for item in row:
        print(item)
