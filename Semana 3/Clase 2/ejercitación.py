#author Daniel Torres A.

#Hacer un juego de adivinanzas
#el número a adivinar es un aleatorio
# entre 0 y 20
# el código debe genear automáticamente el aleatorio
# y preguntarle al usuario con un input el numero que quiere adivinar
# el juego debe tener un máximo número de intentos.
# si me paso del máximo sin adivinar, pierdo
# si adivino, gano


#Adivinanzas
import random

list = []
def fillList(numElements, list):
	'''LLenamos la lista con N(int) numero de elementos '''
	for element in range(0,numElements):
		list.append(element)

def getRandomIntNumber(min,max):
	'''Obtenemos un entero aleatorio entre min y max '''
	randomNumber = random.randint(min,max)
	return randomNumber

def findElementInList(element,list):
	pos = list.index(element)
	#print(pos)
	return pos

def guessNumber(randomNum,list,retries):
	'''Adivina un numero contenido en la lista con [retries] intentos'''

	print("\n\n\n\n###################################################################################")
	print("Adivinanzas\n")
	print(f"Adivina un número entre [{min(list)} y {max(list)}]. Tienes {retries} intentos")

	guessed = -9999
	while(guessed != randomNum and retries != 0):
		print(f"\nIntentos restantes: {retries}")
		try:
			guessed = int(input("Cual es tu número?: "))
			pos = findElementInList(guessed,list)
		except:
			print("El dato que ingresaste no se encuentra en el rango")
		retries = retries - 1

	print("Felicitaciones" if retries != 0 else "Mejor suerte la proxima vez")

#configuracion
numberOfElements = 21 # entre 0 y 20 hay 21 elementos
retries = 3
#inicializacion
fillList(numberOfElements,list)
randomNumber = getRandomIntNumber(min(list),max(list))

#debug
print(list)
print(randomNumber)

#Inicio App
#guessNumber(randomNumber,list,retries)

#__________________________________________________________________________________________________________________

#hacer un juego de piedra papel o tijera contra
#el computador.  El computador escoge aleatoriamente piedra, papel o tijera
# y debe pedir al usuario su input
#el juego debe terminar cuando alguno de los dos gane 2 de 3 partidas
print("###################################################################################")
print("Piedra, Papel o Tijera\n")

opciones = ["R","T","P"] # lo agrego un ultimo elemento para no tener que hacer overlap del index
def gana(eleccion,random,opciones):
	''' Define si gana la eleccion sobre el computador : gana(1) pierde(-1) o empata(0) '''
	#numOptions = len(opciones)
	length = len(opciones)
	#obtengo la posicion del elemento elegido y verifico si gana o empata
	posEleccion = eleccion
	posRandom = random
	if posEleccion == posRandom :
		return 0 #empatan
	elif (0 if posEleccion + 1 == length else (posEleccion + 1)) == posRandom:
		return 1 #gana jugador,pirde computador
	else :
		return -1 # pierde jugador, gana computador


def juego(points,opciones):
	'''points: cuantos puntos debe acumular un jugador para ganar'''

	acumJugador = 0
	acumComputador = 0

	while acumComputador != points and acumJugador != points :
		#obtengo la opcione del computador
		computador = opciones[getRandomIntNumber(0,2)] 
		#debug
		print("El computador eligio ",computador)
		#enddebug

		computador = findElementInList(computador,opciones)
		#obtengo la opcione del jugador
		jugador = findElementInList(input("Elija Roca[R] | Papel [P] | Tijera [T]: ").upper(),opciones)
	
		#verifico si gana, empata o pierde
		result = gana(jugador,computador,opciones)

		print("El computador eligio  ",opciones[computador])
		print("El jugador eligio : " ,opciones[jugador])
		print("\n")
		
		if result > 0:
			acumJugador = acumJugador + 1
			print(f"Ganas. Computador lleva {acumComputador} | Jugador lleva {acumJugador} puntos")
		elif result < 0:
			acumComputador +=1
			print(f"Pierdes. Computador lleva {acumComputador} | Jugador lleva {acumJugador} puntos")
		else:
			print(f"Empate. Computador lleva {acumComputador} | Jugador lleva {acumJugador} puntos")
		print("\n")

	#fin del juego
	print("Perdiste" if acumJugador -points else " Ganaste")
	print(f"Resultados: Computador= {acumComputador} | Jugador ={acumJugador} puntos")


#Inicio App
print("\n\n\n\nJuego Roca, Papel y Tijera: Roca le gana a tijera, tijera le gana a papel y papel le gana a toca")
print("Gana 2 de 3 partidas contra el computador.\n")
juego(3,opciones)




#pruebas
#opciones = ["R","T","P"]
#print(gana(0,0,opciones))
#print(gana(0,1,opciones))
#print(gana(0,2,opciones))
#print(gana(1,0,opciones))
#print(gana(1,1,opciones))
#print(gana(1,2,opciones))
#print(gana(2,0,opciones))
#print(gana(2,1,opciones))
#print(gana(2,2,opciones))


		