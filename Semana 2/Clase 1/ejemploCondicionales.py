
numeroAEncontrar = 7

numeroIngresadoPorElUsuario = int(input("Adivina cuál número está registrado como varibale: "))

if numeroIngresadoPorElUsuario > numeroAEncontrar:
    print("El numero que estás buscando es menor al que ingresaste")
elif numeroIngresadoPorElUsuario < numeroAEncontrar:
    print("El número que estás buscando es mayor al que ingresaste")
# elif numeroIngresadoPorElUsuario == numeroAEncontrar:
else:
    print("¡Correcto! El número que ingresaste es el correcto.")
