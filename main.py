from datetime import datetime
from viajes import Ciudad, Itinerario, Unidad,Asiento
from transporte import Servicio, Argentur
from vistas import VistaServicio
from usuarios import Reserva, Pasajero

# Crear ciudades
c1 = Ciudad("CBA", "Córdoba", "Córdoba")
c2 = Ciudad("MDZ", "Mendoza", "Mendoza")
c3 = Ciudad("SFE", "Santa Fe", "Santa Fe")
c4 = Ciudad("LGR", "Las Grutas", "Rio Negro")
c5 = Ciudad("USH", "Usuahia", "Tierra del Fuego")

#Crear Asientos
a1 = Asiento(1,True)
a2 = Asiento(2,False)
a3 = Asiento(3,True)
a4 = Asiento(4,False)
a5 = Asiento(5,False)

Asientos = [a1,a2,a3,a4,a5]
Asientos_ocupados = [a1,a3]

# Crear itinerario
it1 = Itinerario(c1, c2)
it1.agregar_paradas(c3)
it1.agregar_paradas(c4)

it2 = Itinerario(c3, c5)
it2.agregar_paradas(c2)
it2.agregar_paradas(c4)

# Crear unidad
u1 = Unidad("ABC123",Asientos)
u2 = Unidad("BFD323",Asientos)
u3 = Unidad("CTA587",Asientos_ocupados)

# Crear servicio
s1 = Servicio("001", u1, datetime(2025, 5, 10, 8), datetime(2025, 5, 10, 18), "Turista", 15000, it1)
s2 = Servicio("002", u2, datetime(2025, 5, 15, 8), datetime(2025, 5, 15, 20), "Premium", 28000, it2)
s3 = Servicio("003",u3,datetime(2025, 5, 15, 8), datetime(2025, 5, 15, 20), "Turista",16000,it2)


empresa = Argentur(True)
empresa.agregar_servicio(s1)
empresa.agregar_servicio(s2)
empresa.agregar_servicio(s3)


if __name__ == "__main__":
    vista_servicio = VistaServicio()
    pasajero = None
    while True:
        print("\n\n--- MENU PRINCIPAL ---")
        print("1. Consultar Servicios Disponibles")
        if pasajero is not None:
            print('2. Realizar Reserva')
        else:   
            print('2. Registrarse como Usuario')
        print("3. Consultar Informe")
        print("4. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Vista de Servicios Disponibles
            vista_servicio.mostrar_servicios_disp(empresa)
        elif opcion == "2":
            # Realizar Reserva
            if pasajero is not None:
                print('\n\n -- Busqueda de Servicio --')
                id_servicio = input("Ingrese el ID del servicio: ")
                servicio = empresa.obtener_servicio_disponible(id_servicio)
                if servicio is None:
                    print("ERROR: Servicio no encontrado.")
                    continue
                vista_servicio.mostrar_servicio_especifico(servicio)
                numero_asiento = int(input("Ingrese el número de asiento: "))
                reserva = Reserva.realizar_reserva(servicio, pasajero, numero_asiento)
                if reserva is not None:
                    print("Realizando reserva...")
                    print(f"Reserva realizada: Pasajero {pasajero.obtener_nombre()}, asiento {numero_asiento}, servicio del {servicio.obtener_fecha_partida()}.")
                else:
                    print("No se pudo realizar la reserva.")
            else:
                # Registro de Pasajero
                print("\n -- Registro de Pasajero --")
                nombre = input("Ingrese su nombre: ")
                email = input("Ingrese su email: ")
                dni = int(input("Ingrese su DNI: "))
                pasajero = Pasajero(nombre, email, dni)
        elif opcion == "3":
            #Consultar Informe (a implementar)
            print("Funcionalidad de informe no implementada.")
        elif opcion == "4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")
