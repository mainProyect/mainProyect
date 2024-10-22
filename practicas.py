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
    def subirNivel(self):
        self.nivel+1
        return self.nivel
    def calcularDaño(self,enemigo,multiplicador=1.0):
        aleatorio=random.randint(-5,5)
        daño=(self.ataque*multiplicador)-enemigo.defensa+aleatorio
        return max(daño,0)
    def atacar(self, enemigo):
        daño=self.calcularDaño(enemigo)
        print(f'{self.nombre} le ah hecho {daño} de daño a {enemigo.nombre}')
    def cambiarDeClase(self):
        if self.nivel==5:
            print(f'{self.nombre}, ah alcanzado el nivel 5, cambia de clase.')
            return Mago(self, nombre)
        return self
    def  __str__(self):
        return f'{self.nombre}\n    Ataque -> {self.ataque}\n   Defensa -> {self.defensa}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'
class Mago(PersonajePrincipal):
    def __init__(self, nombre):
        super().__init__(self,nombre)

class Gobling:
    def __init__(self,nombre):
        self.nombre = nombre
        self.vida = 100
        self.mana = 100
        self.defensa = 2
        self.ataque = 3
        self.speed = 3
        self.attSpeed= 3
    def __str__(self):
        return f'{self.nombre}\n    Ataque -> {self.ataque}\n   Defensa -> {self.defensa}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}\n    VIDA -> {self.vida}\n    MANA -> {self.mana}'



miProtagonista = PersonajePrincipal("Robot prueba 'A'")
print(miProtagonista.__str__())        
miGoblin=Gobling("AllStar")

miProtagonista.atacar(miGoblin)

