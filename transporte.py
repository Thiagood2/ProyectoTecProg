from datetime import datetime
from viajes import Unidad, Itinerario


class Servicio:
    def __init__(self, id_servicio:str, unidad:Unidad,fecha_partida:datetime, fecha_llegada:datetime, calidad:str,precio:float, itinerario:Itinerario):
        self.id = id_servicio
        self.unidad = unidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.calidad = calidad
        self.precio = precio
        self.itinerario = itinerario

    def obtener_id(self):
        return self.id
    def obtener_unidad(self):
        return self.unidad
    def obtener_fecha_partida(self):
        return self.fecha_partida
    def obtener_fecha_llegada(self):
        return self.fecha_llegada
    def obtener_calidad(self):
        return self.calidad
    def obtener_precio(self):
        return self.precio


    def obtener_ciudad_origen(self):
        return self.itinerario.obtener_ciudad_origen()

    def obtener_ciudad_destino(self):
        return self.itinerario.obtener_ciudad_destino()

    def obtener_paradas(self):
        return self.itinerario.obtener_paradas()

    def obtener_lugares_disponibles(self):
        asientos_disponibles = self.unidad.calcular_asientos_libres()
        return asientos_disponibles




class Argentur:
    def __init__(self, sistema_activo: bool):
        self.sistema_activo = sistema_activo
        self.servicios = []

    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)

    def obtener_servicios_disponibles(self):
        return [s for s in self.servicios if len(s.obtener_lugares_disponibles()) > 0]












