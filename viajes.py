from typing import List
from transporte import Servicio

class Ciudad:
    def __init__(self,codigo:str, nombre:str,provincia:str):
        self.codigo = codigo
        self.nombre_ciudad = nombre
        self.nombre_provincia = provincia

class Itinerario:
    def __init__(self,serivicio: Servicio, ciudad_origen: Ciudad, ciudad_destino: Ciudad,paradas_itermedias:List):
        pass

class Unidad:
    def __init__(self,patente:str):
        self.patente = patente

class Asiento:
    def __init__(self,numero:int,ocupado:bool):
        self.numero_asiento = numero
        self.ocupado = ocupado