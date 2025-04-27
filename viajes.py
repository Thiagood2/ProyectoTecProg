

class Ciudad:
    def __init__(self,codigo:str, nombre:str,provincia:str):
        self.codigo = codigo
        self.nombre_ciudad = nombre
        self.nombre_provincia = provincia

    def obtener_codigo(self):
        return self.codigo
    def obtener_nombre_ciudad(self):
        return self.nombre_ciudad
    def obtener_provincia(self):
        return self.nombre_provincia


class Itinerario:
    def __init__(self, ciudad_origen: Ciudad, ciudad_destino: Ciudad):
        self.ciudad_origen = ciudad_origen
        self.ciudad_destino = ciudad_destino
        self.paradas_itermedias = []

    def agregar_paradas(self,ciudad:Ciudad):
        self.paradas_itermedias.append(ciudad)

    def obtener_ciudad_origen(self):
        return self.ciudad_origen.obtener_nombre_ciudad()

    def obtener_ciudad_destino(self):
        return self.ciudad_destino.obtener_nombre_ciudad()

    def obtener_paradas(self):
        return self.paradas_itermedias



class Asiento:
    def __init__(self,numero:int,ocupado:bool):
        self.numero_asiento = numero
        self.ocupado = ocupado

    def obtener_numero_asiento(self):
        return self.numero_asiento
    
    def marcar_libre(self):
        self.ocupado = False

    def marcar_ocupado(self):
        self.ocupado = True

        
    def obtener_estado(self):
        return self.ocupado

class Unidad:
    def __init__(self,patente:str, asientos_totales: list[Asiento]):
        self.patente = patente
        self.asientos = asientos_totales

    def calcular_asientos_libres(self):
        asientos_libres = []
        for asiento in self.asientos:
            if not asiento.obtener_estado():
                asientos_libres.append(asiento)
        return asientos_libres
    
    def obtener_asientos(self):
        return self.asientos
    
    def consultar_asiento_disponible(self, numero_asiento:int):
        for asiento in self.asientos:
            if asiento.obtener_numero_asiento() == numero_asiento:
                return asiento
        return None




