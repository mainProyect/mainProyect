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

class BossGobling():
    def __init__():
        self.nombre = nombre
        self.vida = 200
        self.mana = 200
        self.defensa = 4
        self.ataque = 6
        self.speed = 6
        self.attSpeed= 6
    def calcularDaño(self,enemigo,multiplicador=1.0):
        aleatorio=random.randint(-5,5)
        daño=(self.ataque*multiplicador)-enemigo.defensa+aleatorio
        return max(daño,0)
    def ataqueEspecial(self, enemigo, multiplicador=2.0):
        aleatorio=random.randint(-5,5)
        daño=(self.ataque*multiplicador)-enemigo.defensa+aleatorio
        return calcularDaño(enemigo,multiplicador=2.0)
    """Metodo en el que se llama al que calcula el daño e imprime el daño hecho por el personaje a otro"""
    def atacar(self, enemigo):
        daño=self.calcularDaño(enemigo)
        print(f'{self.nombre} le ah hecho {daño} de daño a {enemigo.nombre}')







