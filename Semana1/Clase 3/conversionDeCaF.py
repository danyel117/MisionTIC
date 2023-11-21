#Paso1: pedir los °C
valorCentigrados = int(input("Por favor ingrese el valor en °C: "))

#Paso2: Aplicar fórmula de conversión entre °C y F
valorFahrenheit = (valorCentigrados * 9/5) + 32

#Paso3: mostrar el resultado
print(f'El valor en Fahrenheit es: {valorFahrenheit}')