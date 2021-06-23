#implementar un sistema de gestión de tareas
#un usuario debe tener un nombre, una lista de tareas y una tarea en curso
#los elementos de la lista de tareas son de una clase Tarea
#la clase Tarea tiene los siguientes atributos:
    #descripción de la tarea
    #fecha límite de la tarea
#la clase usuario tiene los siguientes atributos:
    #nombre
    #tareaActual
    #listaTareas
#la clase usuario tiene los siguientes métodos:
    #agregar una tarea:
        #si el usuario no tiene tarea actual, la agrega como tarea actual
        #si el usuario ya tiene tarea actual, la agrega al final
        # de la lista de tareas pendientes
    #finalizar una tarea
        #saca la siguiente tarea de la lista y la pone en "tarea actual"

#1. hacer una clase Tarea
class Task:
    def __init__(self,description, dueDate):
        self.description = description
        self.dueDate = dueDate

    def __str__(self):
        return self.description + " - " + self.dueDate

#2. hacer la clase usuario
class User:
    def __init__(self,name):
        self.name=name
        self.currentTask = ''
        self.taskList = []

    def addTask(self):
        print("método para agregar una tarea")

    def endTask(self):
        print("método para finalizar una tarea")

#3. hacer la lógica de la aplicación

user = User("Daniel")

while True:
    operaciones = """
        Ingrese A para registrar una nueva tarea
        Ingrese F para finalizar la tarea actual
    """
    inputUsuario = input(operaciones)
    if inputUsuario == "A":
        #pedir al usuario la descripción de la tarea y la fecha límite
        #crear la nueva tarea
        #implementar el método addTask de la clase User
        print("agregar una nueva tarea")
    elif inputUsuario == "F":
        print("Finalizar la tarea actual")