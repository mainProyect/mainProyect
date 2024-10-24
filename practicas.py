"""Se crea una clase PersonalePrincipal, la
cual tiene distintos metodos de interaccion."""
import random
class PersonajePrincipal:
    def  __init__(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("El nombre tiene que ser una cadena de caranteres")
        self.nombre=nombre
        self.ataque = 10
        self.defensa = 1
        self.speed = 1
        self.attSpeed = 2
        self.nivel=1
    """Metodo para subir de nivel a personaje mientas este Sea menor a 100"""
    def subirNivel(self, incrementoDeAtaque=1, incrementoDefensa = 1, incrementoAttspeed=1):
        self.nivel+=1
        self.ataque+=incrementoDeAtaque
        self.incrementoDefensa+=incrementoDefensa
        self.incrementoAttspeed+=incrementoAttspeed

        return self.nivel
    """Metodo para calcular el daño de un personaje hacia otro"""
    def calcularDaño(self,enemigo,multiplicador=1.0):
        aleatorio=random.randint(-5,5)
        daño=(self.ataque*multiplicador)-enemigo.defensa+aleatorio
        return max(daño,0)
    """Metodo en el que se llama al que calcula el daño e imprime el daño hecho por el personaje a otro"""
    def atacar(self, enemigo):
        daño=self.calcularDaño(enemigo)
        print(f'{self.nombre} le ah hecho {daño} de daño a {enemigo.nombre}')
    """Segun el nivel del personaje va a tener distintas opciones para cambiar de clase"""
    def cambiarDeClase(self):
        if self.nivel==5:
            print(f'{self.nombre}, ah alcanzado el nivel 5, cambia de clase.')
            return Mago(self, nombre)
        return self
    def  __str__(self):
        return f'{self.nombre}\n    Ataque -> {self.ataque}\n   Defensa -> {self.defensa}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'




miProtagonista = PersonajePrincipal("Robot prueba 'A'")
print(miProtagonista.__str__())        
miGoblin=Gobling("AllStar")

miProtagonista.atacar(miGoblin)

