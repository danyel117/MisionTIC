
class Persona:
    def __init__(self, nombre, documento, correo):
        self.nombre = nombre
        self.documento = documento
        self.correo = correo

    def __str__(self):
        return self.nombre + " " + self.documento


persona1 = Persona("daniel", "102234", "dsl@c.com")
persona2 = Persona("Susana", "234234", "s@c.com")
print(persona1)
print(persona2)
