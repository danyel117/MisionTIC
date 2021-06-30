import csv

#alto si el valor de apertura fue mayor a 500
#bajo si el valor de apertura fue menor a 300
#medio si el valor estuvo entre 300 y 500

resultados = [["Fecha","Valor de Apertura", "Resultado"]]

with open('tesla.csv',newline="") as teslaCSV:
    reader = csv.reader(teslaCSV,delimiter=",")
    cont = 0 
    for row in reader:
        if cont == 0:
            print("títulos: ")
            print(row)
            cont = cont +1
        else:
            print(row)
            valorApertura = float(row[1])
            if valorApertura > 500:
                resultados.append([row[0],valorApertura,"Alto"])
            elif valorApertura < 300:
                resultados.append([row[0],valorApertura,"Bajo"])
            else:
                resultados.append([row[0],valorApertura,"Medio"])
            
with open('tesla_result.csv','w',newline="") as resultCSV:
    writer = csv.writer(resultCSV,delimiter="\t")
    for fila in resultados:
        writer.writerow(fila)
