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

    def addTask(self,newTask):
        #revisar si el usuario ya tiene una "tarea actual"
        if self.currentTask == '':
            self.currentTask = newTask
        else:
            self.taskList.append(newTask)

    def printTasks(self):
        print("tarea actual",self.currentTask)
        print("lista de tareas: ")
        for task in self.taskList:
            print(task)

    def endTask(self):
        if len(self.taskList)>0:
            self.currentTask = self.taskList.pop(0)
        else:
            self.currentTask = ''
        print("método para finalizar una tarea")

#3. hacer la lógica de la aplicación
user = User("Daniel")

while True:
    operaciones = """
        Ingrese A para registrar una nueva tarea
        Ingrese F para finalizar la tarea actual
        Ingrese I para imprimir la lista de tareas
    """
    inputUsuario = input(operaciones)
    if inputUsuario == "A":
        #pedir al usuario la descripción de la tarea y la fecha límite
        description = input("Por favor ingrese la descripción de la tarea: ")
        date = input("Por favor ingrese la fecha de la tarea: ")
        #crear la nueva tarea
        newTask = Task(description,date)
        #implementar el método addTask de la clase User
        user.addTask(newTask)
    elif inputUsuario == "I":
        user.printTasks()
    elif inputUsuario == "F":
        user.endTask()
        print("Finalizar la tarea actual")