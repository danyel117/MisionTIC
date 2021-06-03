

class Persona:
    #init es el constructor de la clase
    def __init__(self, nombre, edad, telefono, correo, direccion, nacionalidad, profesion): 
        self.nombre = nombre
        self.edad = edad
        self.telefono = telefono
        self.correo = correo
        self.direccion = direccion
        self.nacionalidad = nacionalidad
        self.profesion = profesion


persona1 = Persona("Daniel",50, 3117191377, "dsl@c.com","sdf","colombiano","ingeniero")
persona2 = Persona("Jon",45,"234345","jon@snow.com","winterfell","ingles","guerrero")
print(persona1.telefono)
print(persona2.telefono)