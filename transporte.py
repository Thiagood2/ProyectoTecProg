from datetime import datetime
from viajes import Unidad, Itinerario
from collections import defaultdict

class Servicio:
    def __init__(self, id_servicio:str, unidad:Unidad,fecha_partida:datetime, fecha_llegada:datetime, calidad:str,precio:float, itinerario:Itinerario):
        self.id = id_servicio
        self.unidad = unidad
        self.fecha_partida = fecha_partida
        self.fecha_llegada = fecha_llegada
        self.calidad = calidad
        self.precio = precio
        self.itinerario = itinerario
        self.reservas = []

    def agregar_reserva(self, reserva):
        self.reservas.append(reserva)
    def obtener_reservas(self):
        return self.reservas
    def obtener_id(self):
        return self.id
    def obtener_unidad(self):
        return self.unidad
    def obtener_fecha_partida(self):
        return self.fecha_partida.strftime("%d/%m/%Y %H:%M")
    def obtener_fecha_llegada(self):
        return self.fecha_llegada.strftime("%d/%m/%Y %H:%M")
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
        return self.unidad.calcular_asientos_libres()

    def consultar_asiento(self, numero_asiento:int):
        return self.unidad.consultar_asiento_disponible(numero_asiento)


class Argentur:
    def __init__(self, sistema_activo: bool):
        self.sistema_activo = sistema_activo
        self.servicios = []
        self.ventas = []


    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)

    def agregar_venta(self, venta):
        self.ventas.append(venta)

    def obtener_ventas(self):
        return self.ventas

    def obtener_servicios_disponibles(self):
        return [s for s in self.servicios if len(s.obtener_lugares_disponibles()) > 0]
    
    def obtener_servicio_disponible(self, id_servicio:str):
        for servicio in self.obtener_servicios_disponibles():
            if servicio.obtener_id() == id_servicio:
                return servicio
        return None
    
    def obtener_estado_sistema(self):
        return self.sistema_activo

class GeneradorInforme:
    def __init__(self, ventas):
        self.ventas = ventas

    def generar(self, fecha_desde: datetime, fecha_hasta: datetime):
        total_facturado = 0
        ventas_por_destino = defaultdict(int)
        pagos_por_medio = defaultdict(int)

        for venta in self.ventas:
            fecha_venta = venta.obtener_fecha_venta()
            if fecha_desde <= fecha_venta <= fecha_hasta:
                total_facturado += venta.obtener_precio_venta()

                destino = venta.obtener_destino()
                ventas_por_destino[destino] += 1

                medio_pago = venta.obtener_medio_pago()
                pagos_por_medio[medio_pago] += 1

        return {
            "total_facturado": total_facturado,
            "ventas_por_destino": ventas_por_destino,
            "pagos_por_medio": pagos_por_medio
        }













