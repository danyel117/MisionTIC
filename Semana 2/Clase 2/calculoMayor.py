#pedirle al usuario dos valores numéricos. Imprimir el mayor de ellos.

valor1 = float(input("Ingrese el valor #1"))
valor2 = float(input("Ingrese el valor #2"))

if valor1 > valor2:
    print("el primer dato es mayor que el segundo")
elif valor2 > valor1:
    print("el segundo dato es mayor que el primero")
else:
    print("Los valores son iguales. No hay ninguno mayor que el otro")