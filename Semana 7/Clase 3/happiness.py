import csv

#1. descargar el archivo happiness.csv, abrirlo con python e imprimir todas las filas
with open('happiness.csv',newline="") as happinessFile:
    happinessData = csv.reader(happinessFile,delimiter=";")
    #1. imprimir todas las filas
    # for row in happinessData:
    #     print(row)

    #2. imprimir solamente la información de colombia
    # for row in happinessData:
    #     if row[0]=="Colombia":
    #         print("datos para Colombia")
    #         print(row)

    #3. imprimir solamente la infomación de latinoamérica
    # for row in happinessData:
    #     if row[1]=="Latin America and Caribbean":
    #         print("Datos de latinoamérica")
    #         print(row)
            
    #4. calcular el promedio de ladder score para todos los países de latinoamérica
    # suma = 0
    # contador = 0
    # for row in happinessData:
    #     if row[1]=="Latin America and Caribbean":
    #         suma = suma + float(row[2])
    #         contador = contador + 1

    # promedio = suma / contador
    # print("el valor del promedio del ladder score es: ", promedio)

    #5. calcular el país de asia con el "social support" más alto
    # maximo=0
    # pais=""
    # for row in happinessData:
    #     if "Asia" in row[1]:
    #         if float(row[7])>maximo:
    #             maximo=float(row[7])
    #             pais=row[0]
    # print(f"el país de asia con el soporte social mas alto es: {pais} con {maximo}")

    #obtener la lista de países del mundo que tengan un índice de generosidad positivo
    #esa lista de países se debe guardar en un csv nuevo y luego se debe calcular
    #el promedio del Healthy life expectancy de esos países
    resultados = [["Pais","Generosity","Healthy life expectancy"]]
    cont = 0
    for row in happinessData:
        if cont>0:
            generosity=float(row[10])
            if generosity>0:
                healthyLife=float(row[8])
                resultados.append([row[0],generosity,healthyLife])
        cont = cont + 1

    #obtener el siguiente cálculo del ladder score:
        #países con ladder score inferior a 4 se consideran infelices
        #países con ladder score entre 4 y 6 se consideran indiferentes
        #países con ladder score mayor a 6 se consideran felices
        #obtener para cada país su tipo
        #para cada país obtener el promedio de:
        #promeidoIndicadores: Logged GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices
        #  Generosity y Perceptions of corruption
        #obtener el promedio del indicador para los países infelices, indiferentes y felices
        #obtener un csv de resultado con las siguientes columnas:
        #  pais, region, ladder score, Logged GDP per capita, Social support, Healthy life expectancy, Freedom to make life choices
        #  Generosity, Perceptions of corruption, tipo de felicidad, indicador promedio

suma = 0
contador = 0
# contadorFilas = 0
# for fila in resultados:
#     print("fila resultado")
#     print(fila)
#     if contadorFilas>0:
#         suma = suma + fila[2]
#         contador = contador + 1
#     contadorFilas = contadorFilas + 1

for index, fila in enumerate(resultados):
    if index > 0:
        suma = suma + fila[2]
        contador = contador + 1
promedio = suma / contador
print("promedio de healthy life expectancy en países con generosity positivo: ", promedio)

with open('resultado.csv','w',newline="") as resultCSV:
    writer = csv.writer(resultCSV,delimiter="\t")
    for fila in resultados:
        writer.writerow(fila)
