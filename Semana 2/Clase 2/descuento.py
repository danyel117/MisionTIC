valorCompra = float(input("Por favor ingrese el valor de la compra: "))

if valorCompra > 100000:
    descuento = valorCompra * 10 / 100
    print(f"el valor del descuento es {descuento}")
else:
    descuento = 0

valorTotal = valorCompra - descuento
print(f"El total de la compra es {valorTotal}")