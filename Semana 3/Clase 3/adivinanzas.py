#Hacer un juego de adivinanzas
#el número a adivinar es un aleatorio
# entre 0 y 20
# el código debe genear automáticamente el aleatorio
# y preguntarle al usuario con un input el numero que quiere adivinar
# el juego debe tener un máximo número de intentos.
# si me paso del máximo sin adivinar, pierdo
# si adivino, gano

import random

def GuessTheNumber(maxRetries):
    #numero a adivinar
    numberToGuess = random.randint(0,20)

    #numero maximo de intentos
    maxGuess = maxRetries

    #contador de intentos del usuario
    contUserGuess = 0

    won = False

    while contUserGuess < maxGuess and not won:
        userInput = int(input("Adivina el número entre 0 y 20: "))
        if userInput == numberToGuess:
            print("¡Has ganado!")
            won = True
            return won
        else:
            print("Respuesta Incorrecta")
            contUserGuess = contUserGuess + 1
            print(f"Te quedan {maxGuess - contUserGuess} intentos")

    if contUserGuess == maxGuess:
        print(f"¡Has perdido! El número a encontrar era {numberToGuess}")
    
    return won

result = GuessTheNumber(5)

print(result)




