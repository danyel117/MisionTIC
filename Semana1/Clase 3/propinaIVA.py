#Paso1: Pedir el total de la factura
totalFactura = int(input("Por favor ingrese el valor total de la factura: "))

#Paso2: Pedir el porcentaje de propina que se quiere entregar
porcentajePropina = int(input("Por favor ingrese el porcentaje de propina que quiere entregar: "))

#Paso3: Calcular el valor del IVA del 19%
valorIVA = totalFactura * 19 / 100

#Paso4: Calcular el subtotal (total de la factura - valor del iva)
subtotal = totalFactura - valorIVA

#Paso5: Calcular el valor de la propina (subtotal * propina / 100)
valorPropina = subtotal * porcentajePropina / 100

#Paso6: mostrar el resultado
print(f"El valor total de la factura fue {totalFactura}")
print(f"El valor del IVA fue {valorIVA}")
print(f"El valor del subtotal fue {subtotal}")
print(f"El valor de la propina fue {valorPropina}")
print(f"El valor total de la compra mas la propina es ${totalFactura + valorPropina} pesos")