from datetime import datetime

class Pasajero:
    def __init__(self,nombre:str,email:str,dni:int):
        self.nombre = nombre
        self.email = email
        self.dni = dni

class Reserva:
    def __init__(self,fecha_hora_reserva:datetime):
        self.fecha_reserva = fecha_hora_reserva

class Venta:
    def __init__(self,fecha_hora_venta:datetime):
        self.fecha_venta = fecha_hora_venta
