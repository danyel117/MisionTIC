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

#hacer filtros con Pandas
# print(dfHappiness[:,])




