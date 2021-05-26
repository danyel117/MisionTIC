# ejercicio4: hacer un sistema de calificaciones
    #pedir la calificación de un examen del usuario (0-5)
    #0 - 3: imprimir "insuficiente" (3 no incluido)
    #3 - 4: imprimir "aceptable" (4 no incluido)
    #4 - 4.6: imprimir "sobresaliente" (4.6 no incluido)
    #4.6 - 5: imprimir "excelente"
    #en cualquier otro rango, imprimir "calificación inválida"

calificacion = float(input("por favor ingrese la calificación: "))

if calificacion >= 0 and calificacion <= 5:
    #calculo del tipo de calificacion
    if calificacion >=0 and calificacion <3:
        print("la calificación es insuficiente")
    elif calificacion >= 3 and calificacion <4:
        print("la calificación es aceptable")
    elif calificacion >= 4 and calificacion < 4.6:
        print("la calificación es sobresaliente")
    else:
        print("la calificación es excelente")
else:
    print("La calificación es inválida")
