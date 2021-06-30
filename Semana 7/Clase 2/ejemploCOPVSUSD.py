import csv

riesgos = [["Fecha","Edad","Riesgo"]]
with open('dtcsv_mod.csv',newline="") as Data:
    csvReader = csv.reader(Data,delimiter=",")
    print(csvReader)
    cont = 0
    for fila in csvReader:
        print(cont)
        cont += 1
        try:
            edad = int(fila[7])
            if edad > 60:
                riesgos.append([fila[0],edad,"Alto Riesgo"])
            elif edad <=60 and edad >45:
                riesgos.append([fila[0],edad,"Alto Medio"])
            elif edad<=45 and edad >30:
                riesgos.append([fila[0],edad,"Alto Moderado"])
            elif edad<=30:
                riesgos.append([fila[0],edad,"Alto Leve"])
        except:
            print("error leyendo csv")


with open('resultado.csv','w',newline="") as resultCSV:
    writer = csv.writer(resultCSV,delimiter=",")
    for fila in riesgos:
        writer.writerow(fila)