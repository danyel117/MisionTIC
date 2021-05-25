#paso1: pedirle al usuario su peso
peso = int(input("Por favor ingrese su peso en kg: "))

#paso2: pedirle al usuario su estatura
estatura = float(input("Por favor ingrese su estatura en m: "))

#paso3: calcular el IMC
imc = peso / (estatura ** 2)

#paso4: mostrar el IMC dependiendo del caso


if imc < 18.5:
    print("Usted tiene una condición de peso inferior al normal")
elif imc >= 18.5 and imc < 25:
    print("Usted tiene una condición de peso normal")
elif imc>=25 and imc < 30:
    print("Usted tiene un peso superior al normal")
else:
    print("Usted tiene sobrepeso")
    
print(f"Su índice de masa corporal es de {imc} kg/m2")
