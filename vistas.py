
from transporte import Servicio,Argentur, GeneradorInforme
from usuarios import Reserva,Pasajero, Venta
from datetime import datetime
#Clase para mostrar todos los Prints de Servicio
class VistaServicio:
    def __init__(self):
        pass

    def mostrar_servicio(self,servicio:Servicio) ->None:
        print(f'Servicio ID: {servicio.obtener_id()}')
        self.mostrar_itinerario(servicio)
        print(f'- Calidad del Servicio: {servicio.obtener_calidad()}')
        print(f'- Precio: ${servicio.obtener_precio()}')
        print('- Fechas Disponibles: ')
        print(f'            - Salida: {servicio.obtener_fecha_partida()}')
        print(f'            - LLegada: {servicio.obtener_fecha_llegada()}')
        print('---------------------------------------------------------')

    def mostrar_itinerario(self,servicio:Servicio) ->None:
        print('Itinerario: ')
        print(f'            - Origen: {servicio.obtener_ciudad_origen()}')
        # string con todas las paradas intermedias
        paradas = servicio.obtener_paradas()
        nombres_paradas = [p.obtener_nombre_ciudad() for p in paradas]
        paradas_str = ", ".join(nombres_paradas)

        print(f'            - Paradas Intermedias: {paradas_str}')
        print(f'            - Destino: {servicio.obtener_ciudad_destino()}')


    def mostrar_servicio_especifico(self, servicio:Servicio) ->None:
        print('\n\n -- INFORMACION DEL SERVICIO --')
        print(f'Servicio ID: {servicio.obtener_id()}')
        print(f'Precio: ${servicio.obtener_precio()}')
        self.mostrar_itinerario(servicio)
        asientos_disp = servicio.obtener_lugares_disponibles()

        asientos = [a.obtener_numero_asiento() for a in asientos_disp]

        print(f'Asientos Disponibles: {asientos}')

    def mostrar_servicios_disp (self, empresa:Argentur):
        print('\n\n -- SERVICIOS DISPONIBLES --')
        if len(empresa.obtener_servicios_disponibles()) == 0:
            print('No hay servicios disponibles.')
            return
        for servicio in empresa.obtener_servicios_disponibles():
            self.mostrar_servicio(servicio)
        

class VistaReserva:
    def __init__(self):
        pass

    def mostrar_reserva(self,reserva:Reserva) ->None:

        print(f'\n\nID Servicio: {reserva.obtener_nombre_servicio()}')
        print(f'Precio Servicio: ${reserva.obtener_precio_reserva()}')
        print(f'Asiento Elegido: {reserva.obtener_asiento()}')
        print(f'Fecha Reserva: {reserva.obtener_fecha_reserva()}')
        print(f'Expira en: {reserva.obtener_tiempo_restante()}')

    def mostrar_reserva_pagada(self,reserva:Reserva) ->None:

        print(f'\n\nID Servicio: {reserva.obtener_nombre_servicio()}')
        print(f'Precio Servicio: ${reserva.obtener_precio_reserva()}')
        print(f'Asiento Elegido: {reserva.obtener_asiento()}')
        print(f'Fecha Reserva: {reserva.obtener_fecha_reserva()}')
        
    
    def mostrar_reservas_pasajero(self, pasajero:Pasajero) ->None:
        for reserva in pasajero.obtener_reservas():
            self.mostrar_reserva(reserva)
    
    def mostrar_reservas_pasajero_pagas(self, pasajero:Pasajero) ->None:
        for reserva in pasajero.obtener_reservas_pagas():
            self.mostrar_reserva(reserva)


class VistaInforme:
    def __init__(self):
        pass

    def mostrar_informe(self, ventas: list[Venta], fecha_desde: datetime, fecha_hasta: datetime) -> None:
        generarinforme = GeneradorInforme(ventas)
        informe = generarinforme.generar(fecha_desde, fecha_hasta)
        print('\n\n -- INFORME DE VENTAS --')
        print(f"Período: {fecha_desde.strftime('%d/%m/%Y')} - {fecha_hasta.strftime('%d/%m/%Y')}")

        print(f'Total Facturado: ${informe["total_facturado"]:.2f}')
        
        print("\nVentas por destino:")

        for destino, cantidad in informe["ventas_por_destino"].items():
            print(f"  {destino}: {cantidad} ventas")
        print("\nPagos por medio:")
        for medio_pago, cantidad in informe["pagos_por_medio"].items():
            print(f"  {medio_pago}: {cantidad} pagos")
        
       