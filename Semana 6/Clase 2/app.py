from flask import Flask, render_template, url_for

app = Flask(__name__)

class Task:
    def __init__(self,description, dueDate):
        self.description = description
        self.dueDate = dueDate

    def __str__(self):
        return self.description + " - " + self.dueDate
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

    def endTask(self):
        if len(self.taskList)>0:
            self.currentTask = self.taskList.pop(0)
        else:
            self.currentTask = ''

@app.route("/")
def index():
    print("hola soy un print")
    return render_template('index.html')

@app.route("/ruta2")
def ruta2():
    return "hola, soy la ruta 2"

@app.route("/usuario")
def usuario():
    return "hola, ruta de usuarios"


if __name__=="__main__":
    app.run(debug=True)
