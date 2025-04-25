from datetime import datetime
from transporte import Servicio
from viajes import Asiento

class Pasajero:
    def __init__(self,nombre:str,email:str,dni:int):
        self.nombre = nombre
        self.email = email
        self.dni = dni

    def obtener_nombre(self):
        return self.nombre
    def obtener_email(self):
        return self.email
    def obtener_dni(self):
        return self.dni

class Reserva:
    def __init__(self, servicio: Servicio, pasajero: Pasajero, asiento: Asiento, fecha_hora_reserva: datetime):
        self.fecha_reserva = fecha_hora_reserva
        self.servicio = servicio
        self.pasajero = pasajero
        self.asiento = asiento

    @staticmethod
    def realizar_reserva(servicio: Servicio, pasajero: Pasajero, numero_asiento: int):
        # Delegar la verificación del asiento a la unidad
        asiento = servicio.consultar_asiento(numero_asiento)
        if asiento is None:
            print(f"Error: El asiento {numero_asiento} no existe en este servicio.")
            return None

        if asiento.obtener_estado():
            print(f"Error: El asiento {numero_asiento} ya está ocupado.")
            return None
        
        # Crear la reserva
        asiento.marcar_ocupado()
        reserva = Reserva(servicio, pasajero, asiento, datetime.now())
        return reserva  


class Venta:
    def __init__(self,fecha_hora_venta:datetime):
        self.fecha_venta = fecha_hora_venta
