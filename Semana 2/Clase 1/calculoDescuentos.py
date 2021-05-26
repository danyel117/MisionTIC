
# precio de base de los huevos = 1800
# precio de base de las arepas = 5000

# si alguien compra mas de 10 canastas, el precio 1000

# si alguien compra mas de 10 canastas de huevos y ademas compra mas de 10 paquetes de arepas
# el precio de los huevos es 800 y el de las arepas es 2000

#paso 1: preguntar cuantos huevos quiere comprar la persona
cantidadHuevos = int(input("Digite la cantidad de canastas de huevos que quiere comprar: "))

#paso 2: preguntar si la persona quiere comprar arepas
quiereArepas = input("¿Usted desea llevar arepas? ").lower()

#paso 3: si la persona quiere comprar arepas, preguntarle cuántas
cantidadArepas = 0
if quiereArepas == "sí" or quiereArepas == "si":
    cantidadArepas = int(input("Digite la cantidad de paquetes de arepas que quiere comprar: "))

#paso 3: calcular el total de la compra
if cantidadArepas > 10 and cantidadHuevos > 10:
    precioHuevos = 800
    precioArepas = 2000
elif cantidadHuevos > 10:
    precioHuevos = 1000
    precioArepas = 5000
else:
    precioHuevos = 1800
    precioArepas = 5000


subTotal = precioHuevos * cantidadHuevos + precioArepas * cantidadArepas
print(f"El total de su compra es de ${subTotal} pesos")

# if subTotal > 50000 and (cantidadHuevos == 0 or cantidadArepas==0):
#     descuento = subTotal * 10 / 100
#     totalFinal = subTotal - descuento
# elif subTotal > 50000 and (cantidadHuevos>0 and cantidadArepas>0):
#     descuento = subTotal * 15 / 100
#     totalFinal = subTotal - descuento
# else:
#     descuento = 0
#     totalFinal = subTotal

# print(f"El descuento de la compra es de ${descuento} pesos")
# print(f"El total final de la compra es de ${totalFinal} pesos")


descuento = 0
if subTotal > 50000:
    if cantidadHuevos == 0 or cantidadArepas == 0:
        descuento = subTotal * 10 / 100
    else:
        descuento = subTotal * 15 / 100

total = subTotal - descuento


#Condiciones adicionales que se deben cumplir:
#1. si el total de la compra es mayor a 50.000, y solo estoy comprando un producto, dar un descuento adicional del 10%

#2. si el total de la compra es mayor a 50.000 y 
# además se están comprando huevos y arepas, el descuento no es 10% sino que es 15%

#mostrare al usuario el total de la compra y también el total del descuento
