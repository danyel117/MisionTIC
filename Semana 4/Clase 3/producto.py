import random
#4:
class Producto:
    def __init__(self,nombre,precio):
        self.nombre = nombre
        self.precio = precio
        self.referencia = "REF"+str(random.randint(1000,10000))
        self.inventario = random.randint(0,100)
