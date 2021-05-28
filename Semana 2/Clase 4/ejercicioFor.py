
listOfNumbers = [-10, 50, 800, 9, 6, 23.5]
print(len(listOfNumbers))

# cont = 0
# for element in listOfNumbers:
#     cont = cont + 1
# print("el total de elementos en la lista es ", cont)

suma = 0
for number in listOfNumbers:
    suma = suma + number
print("la suma de los elementos en la lista es ", suma)
print("el promedio de los datos es", suma / len(listOfNumbers))