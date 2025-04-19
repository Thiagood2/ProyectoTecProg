from datetime import datetime
from usuarios import Pasajero
from viajes import Ciudad, Itinerario, Unidad
from transporte import Servicio, Argentur

# Crear ciudades
c1 = Ciudad("CBA", "Córdoba", "Córdoba")
c2 = Ciudad("MDZ", "Mendoza", "Mendoza")
c3 = Ciudad("SFE", "Santa Fe", "Santa Fe")

# Crear itinerario
it = Itinerario(c1, c2)
it.agregar_paradas(c3)

# Crear unidad
u = Unidad("ABC123")

# Crear servicio
s1 = Servicio(1, u, datetime(2025, 5, 10, 8), datetime(2025, 5, 10, 18), "Turista", 15000, it)

empresa = Argentur(True)
empresa.agregar_servicio(s1)
empresa.mostrar_servicios()
