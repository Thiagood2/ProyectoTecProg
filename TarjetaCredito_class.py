from Mediopago_class import MedioPago

class TarjetaCredito(MedioPago):
    def __init__(self, numero, dni_titular, nombre_titular, fecha_vencimiento):
        self.numero = numero
        self.dni_titular = dni_titular
        self.nombre_titular = nombre_titular
        self.fecha_nacimiento = fecha_vencimiento



