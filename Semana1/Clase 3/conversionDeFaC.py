#Paso1: pedir los °C
valorFahrenheit = int(input("Por favor ingrese el valor en Fahrenheit: "))

#Paso2: Aplicar fórmula de conversión entre F y °C
valorCentigrados = (valorFahrenheit - 32) * 5/9

#Paso3: mostrar el resultado
print(f'El valor en °C es: {valorCentigrados}')