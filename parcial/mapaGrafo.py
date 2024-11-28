class Ubicacion:
    def __init__(self, nombre, tipo, peso=0):
        #Representa una ubicación del mundo (ciudad, mazmorras, etc.)
        self.nombre = nombre  # Nombre de la ubicación
        self.tipo = tipo      # Tipo de ubicación 
        self.peso = peso      # Peso asociado a la ubicación 
        self.aristas = []     # Lista de ubicaciones conectadas a esta

    def agregarArista(self, destino):
        #Agrega una ruta entre esta ubicación y el destino.
        self.aristas.append(destino)

    def __repr__(self):
        return f"{self.nombre} ({self.tipo}, Peso: {self.peso})"


class GrafoMundo:
    def __init__(self):
        self.grafo = {}  # Diccionario que almacenará las ubicaciones

    def agregarUbicacion(self, nombre, tipo, peso=0):
        #Agrega una nueva ubicación al grafo si no existe.
        if nombre not in self.grafo:
            self.grafo[nombre] = Ubicacion(nombre, tipo, peso)

    def agregarRuta(self, origen, destino):
        #Agrega una ruta entre dos ubicaciones.
        # Asegurarse de que las ubicaciones existen en el grafo
        if origen not in self.grafo:
            print(f"Ubicación {origen} no existe en el grafo.")
            return
        if destino not in self.grafo:
            print(f"Ubicación {destino} no existe en el grafo.")
            return
        
        # Agregar la ruta de origen a destino
        self.grafo[origen].agregarArista(self.grafo[destino])
        
        # Si el grafo es no dirigido, también agregamos la ruta en el sentido inverso
        self.grafo[destino].agregarArista(self.grafo[origen])

    def mostrarGrafo(self):
        #Muestra el grafo de manera legible con las ubicaciones y sus rutas.
        for ubicacion in self.grafo.values():
            print(f"Ubicación: {ubicacion.nombre} ({ubicacion.tipo}, Peso: {ubicacion.peso})")
            for arista in ubicacion.aristas:
                print(f"  -> {arista.nombre} ({arista.tipo})")


# Ejemplo de uso
grafo = GrafoMundo()

# Agregar ubicaciones (nodos)
grafo.agregarUbicacion("Ciudad A", "Ciudad", peso=3)
grafo.agregarUbicacion("Mazmorra B", "Mazmorra", peso=5)
grafo.agregarUbicacion("Ciudad C", "Ciudad", peso=2)
grafo.agregarUbicacion("Castillo D", "Castillo", peso=4)

# Agregar rutas (aristas) entre las ubicaciones
grafo.agregarRuta("Ciudad A", "Mazmorra B")
grafo.agregarRuta("Ciudad A", "Ciudad C")
grafo.agregarRuta("Mazmorra B", "Castillo D")
grafo.agregarRuta("Ciudad C", "Castillo D")

# Mostrar el grafo
grafo.mostrarGrafo()
