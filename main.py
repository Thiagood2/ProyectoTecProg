from datetime import datetime
from viajes import Ciudad, Itinerario, Unidad,Asiento
from transporte import Servicio, Argentur
from vistas import VistaServicio, VistaReserva, VistaInforme
from usuarios import Reserva, Pasajero, Venta
from pagos import TarjetaCredito, MercadoPago, Uala


# Crear ciudades
c1 = Ciudad("CBA", "Córdoba", "Córdoba")
c2 = Ciudad("MDZ", "Mendoza", "Mendoza")
c3 = Ciudad("SFE", "Santa Fe", "Santa Fe")
c4 = Ciudad("LGR", "Las Grutas", "Rio Negro")
c5 = Ciudad("USH", "Ushuaia", "Tierra del Fuego")

# Crear Asientos para Unidad 1
asientos_u1 = [
    Asiento(1, False),
    Asiento(2, False),
    Asiento(3, False),
    Asiento(4, False),
    Asiento(5, False)
]

# Crear Asientos para Unidad 2
asientos_u2 = [
    Asiento(1, False),
    Asiento(2, False),
    Asiento(3, False),
    Asiento(4, False),
    Asiento(5, False)
]

# Crear Asientos para Unidad 3 (algunos ocupados)
asientos_u3 = [
    Asiento(1, True),
    Asiento(2, False),
    Asiento(3, True),
    Asiento(4, False),
    Asiento(5, False)
]

# Crear unidades con sus propios asientos
u1 = Unidad("ABC123", asientos_u1)
u2 = Unidad("BFD323", asientos_u2)
u3 = Unidad("CTA587", asientos_u3)

# Crear itinerario
it1 = Itinerario(c1, c2)
it1.agregar_paradas(c3)
it1.agregar_paradas(c4)

it2 = Itinerario(c3, c5)
it2.agregar_paradas(c2)
it2.agregar_paradas(c4)


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
    vista_informe = VistaInforme()
    pasajero = None

    while True:
        print("\n\n--- MENU PRINCIPAL ---")
        print("1. Consultar Servicios Disponibles")
        if pasajero is not None:
            print('2. Realizar Reserva')
        else:   
            print('2. Registrarse como Usuario')      
        print("3. Consultar Informe")
        print("4. Consultar Reservas")
        

        if (pasajero is not None) and (len(pasajero.obtener_reservas()) > 0):
            print("5. Consultar Reservas Pendientes")
            print("6. Pagar Reservas Pendientes")
        print("F4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            # Vista de Servicios Disponibles
            vista_servicio.mostrar_servicios_disp(empresa)
        elif opcion == "2":
            # Busqueda del Servicio
            if pasajero is not None:
                print('\n\n -- Busqueda de Servicio --')
                id_servicio = input("Ingrese el ID del servicio: ")
                servicio = empresa.obtener_servicio_disponible(id_servicio)
                if servicio is None:
                    print("ERROR: Servicio no encontrado.")
                    continue
                vista_servicio.mostrar_servicio_especifico(servicio)

                # Realizar Reserva
                numero_asiento = int(input("Ingrese el número de asiento: "))
                reserva = Reserva.realizar_reserva(servicio, pasajero, numero_asiento)
                if reserva is not None:
                    print("Realizando reserva...")
                    print(f"Reserva realizada: Pasajero {pasajero.obtener_nombre()}, asiento {numero_asiento}, servicio del {servicio.obtener_fecha_partida()}.")
                    servicio.agregar_reserva(reserva)
                else:
                    print("No se pudo realizar la reserva.")
            else:
                # Registro de Pasajero
                print("\n -- Registro de Pasajero --")
                nombre = input("Ingrese su nombre: ")
                email = input("Ingrese su email: ")
                dni = int(input("Ingrese su DNI: "))
                pasajero = Pasajero(nombre, email, dni)
                print(f"Pasajero registrado: {pasajero.obtener_nombre()}, DNI: {pasajero.obtener_dni()}")

        elif opcion == "3":
             #Consultar Informe
             print("\n--- Generar Informe ---")
             fecha_desde_str = input("Ingrese la fecha desde (YYYY-MM-DD): ")
             fecha_hasta_str = input("Ingrese la fecha hasta (YYYY-MM-DD): ")
             fecha_desde = datetime.strptime(fecha_desde_str, "%Y-%m-%d")
             fecha_hasta = datetime.strptime(fecha_hasta_str, "%Y-%m-%d")
             vista_informe.mostrar_informe(empresa.obtener_ventas(), fecha_desde, fecha_hasta)
        
        elif opcion == "4":
            #Consultar Reservas de Pasajero
            print("\n\n -- Historial de Reservas Pagadas --")
            if pasajero is not None:
               reservas_pagadas = pasajero.obtener_reservas_pagas()

               if len(reservas_pagadas) == 0:
                print("No tiene reservas pagadas.")
               else:
                vista_reserva = VistaReserva()
                for reserva in reservas_pagadas:
                    vista_reserva.mostrar_reserva_pagada(reserva)
            else:
                print("Debe registrarse como pasajero para consultar el historial.")

        elif opcion == "5":
            #Consultar Reservas Pendientes a pagar de Pasajero
            print("\n\n -- Sus Reservas Pendientes --")
            vista_reserva = VistaReserva()
            vista_reserva.mostrar_reservas_pasajero(pasajero)

        elif opcion == "6":
            # Concretar ventas (pagar reservas pendientes)
            print("\n\n -- Pagar Reservas Pendientes --")
            if pasajero is not None:
                reservas_pendientes = [reserva for reserva in pasajero.obtener_reservas() if not reserva.estado_expirado()]
                if len(reservas_pendientes) == 0:
                    print("No tiene reservas pendientes de pago.")
                else:
                    print("Reservas pendientes:")
                    for i, reserva in enumerate(reservas_pendientes, start=1):
                        print(f"{i}. Asiento {reserva.obtener_asiento()}, Servicio: {reserva.obtener_id_servicio()}, Precio: ${reserva.obtener_precio_reserva()}")
            
                    opcion_reserva = int(input("Seleccione el número de la reserva que desea pagar: "))
                    if 1 <= opcion_reserva <= len(reservas_pendientes):
                        reserva_a_pagar = reservas_pendientes[opcion_reserva - 1]

                        # Elegir medio de pago
                        print("\nSeleccione el medio de pago:")
                        print("1. Tarjeta de Crédito")
                        print("2. MercadoPago")
                        print("3. Ualá")
                        opcion_pago = int(input("Ingrese el número del medio de pago: "))
                
                        if opcion_pago == 1:
                            nro = input("Ingrese el número de la tarjeta: ")
                            dni = int(input("Ingrese el DNI del titular: "))
                            nombre = input("Ingrese el nombre del titular: ")
                            fecha_vencimiento_str = input("Ingrese la fecha de vencimiento (YYYY-MM-DD): ")
                            fecha_vencimiento = datetime.strptime(fecha_vencimiento_str, "%Y-%m-%d")
                            tarjetacredito = TarjetaCredito(nro, dni, nombre, fecha_vencimiento)
                            venta = Venta.realizar_venta(empresa,reserva_a_pagar,datetime.now(), tarjetacredito)  

                        elif opcion_pago == 2:
                            celular = input("Ingrese su número de celular: ")
                            email = input("Ingrese su email: ")
                            mercadopago = MercadoPago(celular, email)
                            venta = Venta.realizar_venta(empresa,reserva_a_pagar,datetime.now(), mercadopago)  

                        elif opcion_pago == 3:
                            email = input("Ingrese su email: ")
                            nombre = input("Ingrese el nombre del titular: ")
                            uala = Uala(email, nombre)
                            venta = Venta.realizar_venta(empresa,reserva_a_pagar,datetime.now(), uala) 
                        else:
                            print("Opción de medio de pago no válida.")
                            continue
                    else:
                        print("Opción no válida.")
            else:
                print("Debe registrarse como pasajero para pagar reservas.")
        
        elif opcion == "F4":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

