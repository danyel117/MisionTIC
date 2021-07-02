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
        #obtener un promedio global de social support y generosity para todos los países
import csv

result = [["Pais","Region","Score","GDP","Social Support","Healthy Life","Freedom","Generosity","Corruption","Tipo","Indicador"]]

with open('happiness.csv',newline="") as happinessFile:
    happinessData = csv.reader(happinessFile,delimiter=";")
    sumaSocial = 0
    sumaGenerosity = 0
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
            
            sumaSocial = sumaSocial + socialSupport
            sumaGenerosity = sumaGenerosity + generosity 

            if ladderScore < 4:
                tipo = "infeliz"
            elif ladderScore>=4 and ladderScore<6:
                tipo="indiferente"
            else:
                tipo="feliz"

            result.append([row[0],row[1],ladderScore,gdp,socialSupport,healthyLife,freedom,generosity,corruption,tipo,promedio])

    print("suma de social support: ",sumaSocial)         
    print("suma de generosity: ",sumaGenerosity)
    promedioGlobalSocialGenerosity = (sumaSocial + sumaGenerosity)/2
    print("Promedio global: ",promedioGlobalSocialGenerosity)


with open('resultadoHappiness.csv','w',newline="") as resultCSV:
    writer = csv.writer(resultCSV,delimiter=";")
    for fila in result:
        writer.writerow(fila)

sumaFeliz=0
contadorFeliz=0

sumaIndiferente=0
contadorIndiferente=0

sumaInfeliz=0
contadorInfeliz=0


for row in result:
    if row[9]=="feliz":
        contadorFeliz = contadorFeliz + 1
        sumaFeliz = sumaFeliz + row[10]
    elif row[9]=="indiferente":
        contadorIndiferente = contadorIndiferente + 1
        sumaIndiferente = sumaIndiferente + row[10]
    elif row[9]=="infeliz":
        contadorInfeliz = contadorInfeliz + 1
        sumaInfeliz = sumaInfeliz + row[10]


promedioFeliz = sumaFeliz / contadorFeliz
print("el promedio para los países felices es de: ",promedioFeliz)

promedioIndiferente = sumaIndiferente / contadorIndiferente
print("el promedio para los países indiferentes es de: ",promedioIndiferente)

promedioInfeliz = sumaInfeliz / contadorInfeliz
print("el promedio para los países infelices es de: ",promedioInfeliz)


