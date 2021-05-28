listOfGrades=[
    1,
    2.4,
    4.5,
    2.4,
    4.3,
    3.8,
    3.1,
    3,
    2.7,
    4.5,
    5,
    2.1,
    1.8,
    2.4,
    4.3
]

contInsuficiente = 0
contAceptable = 0
contSobresaliente = 0
sumaInsuficiente = 0
sumaAceptable = 0
sumaSobresaliente = 0
for grade in listOfGrades:
    if grade < 3:
        contInsuficiente = contInsuficiente + 1
        sumaInsuficiente = sumaInsuficiente + grade
    elif grade >= 3 and grade < 4:
        contAceptable = contAceptable + 1
        sumaAceptable = sumaAceptable + grade
    else:
        contSobresaliente = contSobresaliente + 1
        sumaSobresaliente = sumaSobresaliente + grade

print("La cantidad de los insuficientes es", contInsuficiente)
print("La cantidad de los aceptables es", contAceptable)
print("La cantidad de los sobresalientes es", contSobresaliente)

print("la suma de los insuficientes es", sumaInsuficiente)
print("la suma de los aceptables es", sumaAceptable)
print("la suma de los sobresalientes es", sumaSobresaliente)

print("El promedio de los insuficientes es", sumaInsuficiente / contInsuficiente)
print("El promedio de los aceptables es", sumaAceptable / contAceptable)
print("El promedio de los sobresalientes es", sumaSobresaliente / contSobresaliente)