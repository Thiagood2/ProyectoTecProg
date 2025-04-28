from datetime import datetime,timedelta
from transporte import Servicio, Argentur
from viajes import Asiento
from pagos import MedioPago, ProcesadorPago
class Pasajero:
    def __init__(self,nombre:str,email:str,dni:int):
        self.nombre = nombre
        self.email = email
        self.dni = dni
        self.reservas = []
        self.reservas_pagadas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)

    def obtener_reservas(self):
        return self.reservas 
    
    def obtener_reservas_pagas(self):
        return self.reservas_pagadas
    
    def agregar_reserva_pagada(self, reserva):
        self.reservas_pagadas.append(reserva)
    
    def eliminar_reserva_propia(self, reserva):
        if reserva in self.reservas:
            self.reservas.remove(reserva)
        else:
            print("Reserva no encontrada.")   

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
        self.fecha_expiracion = (fecha_hora_reserva + timedelta(minutes=30))   # Expira en 30 minutos

    def obtener_precio_reserva(self):
        return self.servicio.obtener_precio()
    
    def obtener_id_servicio(self):
        return self.servicio.obtener_id()

    def obtener_nombre_servicio(self):
        return self.servicio.obtener_id()
    
    def obtener_destino_servicio(self):
        return self.servicio.obtener_ciudad_destino()
    
    def estado_expirado(self) -> bool:
        return datetime.now() > self.fecha_expiracion

    def obtener_tiempo_restante(self) -> str:
        resultado_expiracion = "Expirada"

        if self.estado_expirado():
            return resultado_expiracion
        
        tiempo_restante = self.fecha_expiracion - datetime.now()

        minutos_restantes = int(tiempo_restante.total_seconds() // 60) #Pasaje a minutos

        resultado_expiracion = f' {minutos_restantes} minutos'
        
        return resultado_expiracion

    def eliminar(self):
        if self.estado_expirado():
            self.pasajero.eliminar_reserva_propia(self)
            self.asiento.marcar_disponible()
            return
        
        self.pasajero.eliminar_reserva_propia(self)
        self.pasajero.agregar_reserva_pagada(self)

    def obtener_fecha_reserva(self):
        return self.fecha_reserva.strftime("%d/%m/%Y %H:%M") #Formato de fecha
    
    def obtener_fecha_expiracion(self):
        return self.fecha_expiracion
    
    def obtener_asiento(self):
        return self.asiento.obtener_numero_asiento()

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
        pasajero.agregar_reserva(reserva)
        return reserva  


class Venta:
    def __init__(self,empresa: Argentur, reserva: Reserva, fecha_hora_venta:datetime, medio_pago: MedioPago):
        self.fecha_venta = fecha_hora_venta
        self.reserva = reserva  
        self.medio_pago = medio_pago
        empresa.agregar_venta(self)

    def obtener_fecha_venta(self):
        return self.fecha_venta
    
    def obtener_destino(self):
        return self.reserva.obtener_destino_servicio()
    
    def obtener_precio_venta(self):
        return self.reserva.obtener_precio_reserva()
    
    def obtener_medio_pago(self):
        return self.medio_pago.mostrar_medio()
    
    @staticmethod
    def realizar_venta(empresa:Argentur,reserva:Reserva, fecha_hora:datetime,medio_pago:MedioPago):
        # Delegar la verificación del pago al medio de pago
        if not ProcesadorPago.realizar_pago(medio_pago,reserva.obtener_precio_reserva()):
            print("Error: El pago no fue procesado.")
            return None
        
        # Crear la venta
        venta = Venta(empresa,reserva, fecha_hora, medio_pago)
        reserva.eliminar()
        return venta