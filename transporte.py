from datetime import datetime
from viajes import Unidad

class Argentur:
    def __init__(self, sistema_activo:float):
        self.sistema_activo = sistema_activo

class Servicio:
    def __init__(self, unidad:Unidad,fecha_partida:datetime, fecha_llegada:datetime, calidad:str,precio:float):
        self.unidad = unidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.calidad = calidad
        self.precio = precio