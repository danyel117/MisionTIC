import json

class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

p1 = Persona("Daniel","Saldarriaga")
#convertir la instancia de una clase en un diccionario
print(p1.__dict__)

