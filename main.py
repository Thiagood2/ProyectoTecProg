from datetime import datetime
from viajes import Ciudad, Itinerario, Unidad
from transporte import Servicio, Argentur

# Crear ciudades
c1 = Ciudad("CBA", "Córdoba", "Córdoba")
c2 = Ciudad("MDZ", "Mendoza", "Mendoza")
c3 = Ciudad("SFE", "Santa Fe", "Santa Fe")
c4 = Ciudad("LGR", "Las Grutas", "Rio Negro")
c5 = Ciudad("USH", "Usuahia", "Tierra del Fuego")

# Crear itinerario
it1 = Itinerario(c1, c2)
it1.agregar_paradas(c3)
it1.agregar_paradas(c4)

it2 = Itinerario(c3, c5)
it2.agregar_paradas(c2)
it2.agregar_paradas(c4)

# Crear unidad
u1 = Unidad("ABC123")
u2 = Unidad("BFD323")
u3 = Unidad("CTA587")

# Crear servicio
s1 = Servicio(1, u1, datetime(2025, 5, 10, 8), datetime(2025, 5, 10, 18), "Turista", 15000, it1)
s2 = Servicio(2, u2, datetime(2025, 5, 15, 8), datetime(2025, 5, 15, 20), "Premium", 28000, it2)


empresa = Argentur(True)
empresa.agregar_servicio(s1)
empresa.agregar_servicio(s2)
empresa.mostrar_servicios()
