from abc import ABC, abstractmethod
from datetime import datetime



class MedioPago(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def procesar_pago(self, monto:float):
        pass

    @abstractmethod
    def verificar_pago(self) ->bool:
        pass

    @abstractmethod
    def mostrar_medio(self) ->str:
        pass


class MercadoPago(MedioPago):
    def __init__(self, celular, email):
        super().__init__()
        self.celular = celular
        self.email = email

    def procesar_pago(self, monto:float):
        print(f'Procesando pago ${monto} con MercadoPago')

    def verificar_pago(self):
        # Logica de verificar con MP
        return True
    
    def mostrar_medio(self) ->str:
        return "Mercado Pago"


class TarjetaCredito(MedioPago):
    def __init__(self, numero:str, dni_titular:int, nombre_titular:str, fecha_vencimiento:datetime):
        super().__init__()
        self.numero = numero
        self.dni_titular = dni_titular
        self.nombre_titular = nombre_titular
        self.fecha_vencimiento = fecha_vencimiento

    def procesar_pago(self, monto: float):
        print(f'Procesando pago ${monto} con TarjetaCredito')

    def verificar_pago(self):
        # Logica de verificar con TC
        return True
    
    def mostrar_medio(self) ->str:
        return "Tarjeta de Credito"

class Uala(MedioPago):

    def __init__(self,email:str,nombre_titular:str):
        super().__init__()
        self.email = email
        self.nombre_titular = nombre_titular

    def procesar_pago(self, monto: float):
        print(f'Procesando pago ${monto} con Uala')

    def verificar_pago(self):
        # Logica de verificar con Uala
        return True
    
    def mostrar_medio(self) ->str:
        return "Uala"



# Clase procesadora de pagos
class ProcesadorPago:
    def __init__(self):
        pass

    @staticmethod
    def realizar_pago(metodo_pago:MedioPago, monto:float):
        metodo_pago.procesar_pago(monto)
        if metodo_pago.verificar_pago():
            print("Pago verificado con éxito.")
            return True
        
        return False