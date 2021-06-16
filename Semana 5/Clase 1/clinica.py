# implementar un sistema de turnos en una clínica

# crear una clase "Clinica" que tenga como atributos un nombre
# y una lista de pacientes

# crear una clase Paciente que tenga los atributos nombre, documento y turno

# la clase Clinica tiene un método para ingresar un nuevo paciente. El paciente
# que ingresa, debe ingresar al final de la fila.

# la clase clínica tiene un método para "atender" un nuevo paciente. Se debe
# atender primero al primer paciente que ingresa.

# la clínica solo puede tener 10 pacientes en espera
# cuando ingresa un nuevo paciente, se debe verificar que haya espacio.

# si ya hay 10 pacientes en espera, se debe sacar un mensaje de error.

# TAREA: asignarle un turno a un paciente. El turno es un consecutivo
# que se da en orden de llegada. empieza en 0 y aumenta de 1 en 1, y es
# un texto compuesto por la palabra TURNO y el número de llegada de la persona.
# agregar un método que permita buscar un paciente por documento y que retorne
# su turno.
# adicionalmente, cuando el turno llega a 9, debe reiniciar en 0.


# 1. hacer una clase Clinica y una clase Paciente
class Clinica:
    def __init__(self, nombre):
        self.nombre = nombre
        self.contadorTurnos = 0
        self.listaPacientes = []

    # 2. agregar un método para ingresar pacientes
    def ingresarPaciente(self):
        nombre = input("Ingrese el nombre del paciente: ")
        documento = input("Ingrese el documento del paciente: ")
        # 4. revisar que haya menos de 10 pacientes
        if len(self.listaPacientes) < 10:
            if self.contadorTurnos == 10:
                self.contadorTurnos = 0
            pacienteAIngresar = Paciente(
                nombre, documento, "TURNO" + str(self.contadorTurnos))
            self.listaPacientes.append(pacienteAIngresar)
            self.contadorTurnos = self.contadorTurnos + 1
        else:
            # mostrar un error si se quiere ingresar mas de 10 pacientes
            print("Lo sentimos, la clínica está llena y ya tiene 10 pacientes")

    # 3. agregar un método para atender pacientes
    def atenderPaciente(self):
        pacienteAtendido = self.listaPacientes.pop(0)
        print("Por favor que siga el paciente ", pacienteAtendido.nombre,
              " con documento ", pacienteAtendido.documento)

    def buscarPaciente(self, documentoABuscar):
        for paciente in self.listaPacientes:
            if paciente.documento == documentoABuscar:
                return paciente
        return False

# 1. hacer una clase Clinica y una clase Paciente


class Paciente:
    def __init__(self, nombre, documento, turno):
        self.nombre = nombre
        self.documento = documento
        self.turno = turno

    def __str__(self):
        return self.nombre + " " + self.documento + " " + self.turno


clinica = Clinica("Clinica MisionTIC")

while True:
    operaciones = """
        Ingrese P para registrar un nuevo paciente
        Ingrese A para atender un nuevo paciente
        Ingrese L para listar todos los pacientes
        Ingrese B para buscar un paciente por su documento
    """
    inputUsuario = input(operaciones)

    if inputUsuario == "P":
        clinica.ingresarPaciente()
    elif inputUsuario == "A":
        clinica.atenderPaciente()
    elif inputUsuario == "L":
        print("El total de pacientes es: ", len(clinica.listaPacientes))
        for paciente in clinica.listaPacientes:
            print(paciente)
    elif inputUsuario == "B":
        documentoABuscar = input(
            "Por favor ingrese el documento de la persona: ")
        pacienteEncontrado = clinica.buscarPaciente(documentoABuscar)
        if not pacienteEncontrado:
            print("Paciente no encontrado")
        else:
            print(
                f"El paciente {pacienteEncontrado.nombre} tiene el turno {pacienteEncontrado.turno}")
