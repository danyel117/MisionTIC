#ejericio 5: mostrar si un estudiante está habilitado para 
# presentar el examen
# si el estudiante fue a mas del 75% de las clases 
# puede hacer el examen
# si el estudiante fue a menos del 75% de las clases, 
# solo puede hacer el examen
# si tiene excusa médica

totalClases = int(input("Ingrese el total de clases: "))
clasesAsistidas = int(input("Ingrese a cuántas de esas clases asistió el estudiante: "))

porcentajeAsistencia = clasesAsistidas / totalClases

if porcentajeAsistencia > 0.75:
    print("el estudiante puede asistir al examen")
else:
    tieneExcusa = input("¿El estudiante tiene excusa médica? ").lower()
    if tieneExcusa == "si" or tieneExcusa=="sí":
        print("el estudiante puede presentar el examen")
    else:
        print("el estudiante no puede presentar el examen, porque su porcentaje de asistencia es muy bajo.")
        print("el estudiante sólo asistió al {:.2f}% de las clases".format(porcentajeAsistencia*100))