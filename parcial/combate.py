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
import sqlite3
conexion = sqlite3.connect("miBaseDeDatos.db")
cursor = conexion.cursor()
cursor.execute("""
    CREATE TABLE IF NOT EXISTS Usuarios(
        id INTEGER PRIMARY KEY,
        nombre TEXT NOT NULL,
        edad INTEGER NOT NULL,
        profesion TEXT NOT NULL
        )
""")
cursor.execute("""
    CREATE TABLE Pedidos(
        id INTEGER PRIMARY KEY,
        usuarioId INTEGER NOT NULL,
        producto TEXT NOT NULL,
        cantidad INTEGER NOT NULL,
        stock INTEGER NOT NULL,
        fecha DATE DEFAULT CURRENT_DATE,
        FOREIGN KEY (usuarioId) REFERENCES Usuarios(id)
               )
""")
cursor.execute("""
    INSERT INTO Usuarios (nombre, edad, profesion) VALUES
        ('Miguel',30, "Tecnico en programacion" ),
        ('Luis', 40,"EjemploUno"),
        ('Ana',50, "Politologa );
""")
conexion.commit()

cursor.execute("SELECT edad FROM Usuarios")
usuarios = cursor.fetchall()
print(usuarios)
conexion.close()


