import json

ejemploDiccionario = {
    "lenguaje": "Python",
    "idioma":"Español",
    "programador":"Daniel Saldarriaga",
    "fecha":"29/06/2021",
    "usuarios":[
        {"nombre":"Carlos","correo":"c@c.com"},
        {"nombre":"Felipe","correo":"f@f.com"},
        {"nombre":"Maria","correo":"m@m.com"}
    ]
}

#acceder a los datos del dicccionario
print(ejemploDiccionario["usuarios"][0]["correo"])

#guardar un diccionario como JSON en un archivo en el PC
with open('miPrimerJSON.json','w') as jsonFile:
    json.dump(ejemploDiccionario,jsonFile)
    jsonFile.close()


#leer un archivo .json y obtener la información en un diccionario
with open('miSegundoJSON.json') as jsonFile:
    diccionarioProductos = json.load(jsonFile)
    jsonFile.close()

print(diccionarioProductos["productos"][3]["nombre"])
