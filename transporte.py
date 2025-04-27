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

    def agregar_servicio(self, servicio: Servicio):
        self.servicios.append(servicio)

    def obtener_servicios_disponibles(self):
        return [s for s in self.servicios if len(s.obtener_lugares_disponibles()) > 0]
    
    def obtener_servicio_disponible(self, id_servicio:str):
        for servicio in self.obtener_servicios_disponibles():
            if servicio.obtener_id() == id_servicio:
                return servicio
        return None
    
    def obtener_estado_sistema(self):
        return self.sistema_activo
    
    def generar_informe(self, fecha_desde: datetime, fecha_hasta: datetime):
        generador = GeneradorInforme(self.servicios)
        informe = generador.generar(fecha_desde, fecha_hasta)

        # Mostrar el informe
        print("\n--- INFORME ---")
        print(f"Período: {fecha_desde.strftime('%d/%m/%Y')} - {fecha_hasta.strftime('%d/%m/%Y')}")
        print(f"Total facturado: ${informe['total_facturado']}")
        print("\nViajes por destino:")
        for destino, cantidad in informe["viajes_por_destino"].items():
            print(f"  {destino}: {cantidad} viajes")
        print("\nPagos por medio:")
        for medio, cantidad in informe["pagos_por_medio"].items():
            print(f"  {medio}: {cantidad} pagos")


class GeneradorInforme:
    def __init__(self, servicios):
        self.servicios = servicios

    def generar(self, fecha_desde: datetime, fecha_hasta: datetime):
        from usuarios import Reserva
        total_facturado = 0
        viajes_por_destino = defaultdict(int)
        pagos_por_medio = defaultdict(int)

        for servicio in self.servicios:
            for reserva in servicio.obtener_reservas():
                if isinstance(reserva, Reserva):
                    fecha_reserva = reserva.obtener_fecha_reserva()
                    if fecha_desde <= fecha_reserva <= fecha_hasta:
                        # Sumar al total facturado
                        total_facturado += reserva.obtener_precio_reserva()

                        # Contar viajes por destino
                        destino = servicio.obtener_ciudad_destino()
                        viajes_por_destino[destino] += 1

                        # Contar pagos por medio de pago
                        medio_pago = reserva.medio_pago.__class__.__name__
                        pagos_por_medio[medio_pago] += 1

        return {
            "total_facturado": total_facturado,
            "viajes_por_destino": viajes_por_destino,
            "pagos_por_medio": pagos_por_medio,
        }
        












