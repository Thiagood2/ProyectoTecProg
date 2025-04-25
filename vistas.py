
from transporte import Servicio,Argentur

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
        for servicio in empresa.obtener_servicios_disponibles():
            self.mostrar_servicio(servicio)
        
