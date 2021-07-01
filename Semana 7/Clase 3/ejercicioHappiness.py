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
import csv

result = [["Pais","Region","Score","GDP","Social Support","Healthy Life","Freedom","Generosity","Corruption","Tipo","Indicador"]]

with open('happiness.csv',newline="") as happinessFile:
    happinessData = csv.reader(happinessFile,delimiter=";")
    
    for index,row in enumerate(happinessData):
        if index>0:
            ladderScore = float(row[2])
            gdp=float(row[6])
            socialSupport=float(row[7])
            healthyLife=float(row[8])
            freedom=float(row[9])
            generosity=float(row[10])
            corruption=float(row[11])

            promedio = (gdp+socialSupport+healthyLife+freedom+generosity+corruption)/6
            
            if ladderScore < 4:
                tipo = "infeliz"
            elif ladderScore>=4 and ladderScore<6:
                tipo="indiferente"
            else:
                tipo="feliz"

            result.append([row[0],row[1],ladderScore,gdp,socialSupport,healthyLife,freedom,generosity,corruption,tipo,promedio])
            
with open('resultadoHappiness.csv','w',newline="") as resultCSV:
    writer = csv.writer(resultCSV,delimiter=";")
    for fila in result:
        writer.writerow(fila)