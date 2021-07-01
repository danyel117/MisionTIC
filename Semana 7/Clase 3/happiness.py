import csv

#1. descargar el archivo happiness.csv, abrirlo con python e imprimir todas las filas
with open('happiness.csv',newline="") as happinessFile:
    happinessData = csv.reader(happinessFile,delimiter=";")
    for row in happinessData:
        #1. imprimir todas las filas
        # print(row)

        #2. imprimir solamente la información de colombia
        if row[0]=="Colombia":
            print("datos para Colombia")
            print(row)
        
        #3. imprimir solamente la infomación de latinoamérica
        if row[1]=="Latin America and Caribbean":
            print("Datos de latinoamérica")
            print(row)
        
        #4. calcular el promedio de ladder score para todos los países de latinoamérica
        
        

