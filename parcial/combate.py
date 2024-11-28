class Combate:
    def __init__(self):
        self.participantes = []  # Lista para almacenar los personajes

    def agregarParticipante(self, personaje):
        self.participantes.append(personaje)
        # Ordenar la lista por velocidad en orden descendente usando una función auxiliar
        self.ordenarParticipantes()

    def ordenarParticipantes(self):
        #Función para ordenar participantes por velocidad.
        def obtenerVelocidad(personaje):
            return personaje.speed

        self.participantes.sort(key=obtenerVelocidad, reverse=True)

    def siguienteTurno(self):
        if not self.participantes:
            return None
        # El primer elemento siempre tiene la mayor velocidad
        return self.participantes.pop(0)

    def mostrarOrden(self):
        print("Orden de acciones:")
        for personaje in self.participantes:
            print(f" - {personaje}")
combate = Combate()

