import random

#hacer una función que reciba un número N
#y devuelva una lista con N números aleatorios
# entre 0 y 100
def BuildListOfRandomNumbers(amountOfRandomNumbers,inferiorRange,superiorRange):
    listOfRandomNumbers = []
    for randomNumber in range(0,amountOfRandomNumbers):
        listOfRandomNumbers.append(random.randint(inferiorRange,superiorRange))
    return listOfRandomNumbers

#buscar si un numero x está en la lista de aleatorios.
#en caso de que el numero esté, devolver la posición del numero
def searchNumberInRandomList(numberToFind,listToSearch):
    found = False
    for index,element in enumerate(listToSearch):
        if element == numberToFind:
            return index
    return found

randomList = BuildListOfRandomNumbers(50,0,100)
found = searchNumberInRandomList(17,randomList)
print(randomList)
print(found)


