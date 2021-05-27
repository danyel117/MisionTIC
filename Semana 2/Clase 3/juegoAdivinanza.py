numeroIngresadoPorElUsuario = 0
numeroAEncontrar = 7

while numeroIngresadoPorElUsuario != numeroAEncontrar:
    numeroIngresadoPorElUsuario = int(input("Adivina cuál número está registrado como varibale: "))
    if numeroIngresadoPorElUsuario > numeroAEncontrar:
        print("El numero que estás buscando es menor al que ingresaste")
    elif numeroIngresadoPorElUsuario < numeroAEncontrar:
        print("El número que estás buscando es mayor al que ingresaste")

print("¡Correcto! El número que ingresaste es el correcto.")