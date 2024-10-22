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
