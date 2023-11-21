#pedirle al usuario los ingresos
ingresos = float(input("Por favor digite los ingresos de la empresa: "))

#pedirle al usuario los costos
costos = float(input("Por favor digite los costos de la empresa: "))

#calcular la utilidad bruta ingresos - costos
utilidadBruta = ingresos - costos
print(f"La utilidad bruta de la empresa es: ${utilidadBruta} pesos")

#pedirle al usuario los gastos
gastos = float(input("Por favor digite los gastos de la empresa: "))

#calcular la utilidad operativa utilidad bruta - gastos
utilidadOperativa = utilidadBruta - gastos
print(f"La utilidad operativa de la empresa es ${utilidadOperativa} pesos")

#calcular el impuesto a la renta utilidad operativa * 30%
impuestoRenta = utilidadOperativa * 30 / 100
print(f"El impuesto de renta que debe pagar la empresa es ${impuestoRenta} pesos")

#calcular utilidad neta utilidad bruta - impuesto a la renta
utilidadNeta = utilidadOperativa - impuestoRenta
print(f"La utilidad neta de la empresa es ${utilidadNeta} pesos")