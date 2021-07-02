import pandas as pd

#leer un csv
dfHappiness = pd.read_csv('happiness.csv',delimiter=";")

#imprimir un dataframe
print(dfHappiness)

#visualizar las 5 primeras filas
print(dfHappiness.head())

#visualizar las 5 ultimas filas
print(dfHappiness.tail())

#describir el dataframce
print(dfHappiness.describe())
#enviar la descripción a csv
dfHappiness.describe().to_csv('description.csv')

#ordenar el dataframe segun una columna
print(dfHappiness.sort_values(by="Ladder score"))

#obtener una columna del dataframe
print(dfHappiness["Generosity"])

#obtener un rango de columnas
print(dfHappiness[0:3])

#utilizar el comando .loc para obtener una ubicación específica en el dataframe
print(dfHappiness.loc[0,"Generosity"])
print(dfHappiness.loc[5:10,"Generosity"])

#mostrar varias columnas
nuevoDF = dfHappiness[["Country name","Ladder score","Generosity"]]

#filtrar los países que tienen generosity positivo
filtro = nuevoDF[nuevoDF["Generosity"]>0]
print(filtro)

#hacer filtros por dos condiciones
condicion1 = nuevoDF["Generosity"]>0
condicion2 = nuevoDF["Ladder score"]>7
filtro = nuevoDF[condicion1 & condicion2]
print(filtro)

#iterar un dataframe
lista = []
for indice,dato in dfHappiness.iterrows():
    print(dato["Freedom to make life choices"])
    if dato["Freedom to make life choices"]>0.5:
        lista.append("Alta libertad")
    else:
        lista.append("Baja libertad")
dfHappiness["Tipo de libertad"] = lista
dfHappiness.to_csv('resultado_libertad.csv',sep=";")



