

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
        return self.ciudad_origen

    def obtener_ciudad_destino(self):
        return self.ciudad_destino

    def obtener_paradas(self):
        return self.paradas_itermedias






class Unidad:
    def __init__(self,patente:str):
        self.patente = patente
        self.asientos = []



class Asiento:
    def __init__(self,numero:int,ocupado:bool):
        self.numero_asiento = numero
        self.ocupado = ocupado