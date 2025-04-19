from datetime import datetime
from viajes import Unidad, Itinerario



class Servicio:
    def __init__(self, id_servicio:int, unidad:Unidad,fecha_partida:datetime, fecha_llegada:datetime, calidad:str,precio:float, itinerario:Itinerario):
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

    def mostrar_itinerario(self):
        print('Itinerario: ')
        print(f'''
            - Origen: {self.itinerario.obtener_ciudad_origen()}
            - Paradas Itermedias: {self.itinerario.obtener_paradas()}
            - Destino: {self.itinerario.obtener_ciudad_destino()}
            '''
        )



class Argentur:
    def __init__(self, sistema_activo: float):
        self.sistema_activo = sistema_activo
        self.servicios = []

    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)

    def mostrar_servicios(self):

        print('===================================')
        print('SERVICIOS DISPONIBLES')
        print('===================================')
        for servicio in self.servicios:
    #Agregar logica de Asientos disponibles en (UNIDAD)
            print(f'Servicio ID: {servicio.obtener_id()}')
            servicio.mostrar_itinerario()
            print(f'''
            - Calidad del Servicio: {servicio.obtener_calidad()}
            - Fechas disponibles: 
                - Salida: {servicio.obtener_fecha_partida()}
                - LLegada: {servicio.obtener_fecha_llegada()}
        ---------------------------------------------------------''')




