class Itinerario:
    pass

class Ciudad:
    def __init__(self,codigo:str, nombre:str,provincia:str):
        self.codigo = codigo
        self.nombre_ciudad = nombre
        self.nombre_provincia = provincia

class Unidad:
    def __init__(self,patente:str):
        self.patente = patente

class Asiento:
    def __init__(self,numero:int,ocupado:bool):
        self.numero_asiento = numero
        self.ocupado = ocupado