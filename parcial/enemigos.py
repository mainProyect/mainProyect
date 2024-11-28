import random
class Gobling:
    def __init__(self,nombre):
        self.nombre=nombre
        self.vida = 100
        self.mana = 100
        self.pAttack= 10
        self.mAttack = 1
        self.mDef=1
        self.pDef=1
        self.accuracy=1
        self.evacion=1
        self.rateCritical= 1
        self.castingSpeed= 1
        self.speed = 1
        self.attSpeed = 2
        self.nivel=1
    def __str__(self):
        return f'{self.nombre}\n    Ataque fisico-> {self.pAttack}\n    Ataque magico -> {self.mAttack}\n    Defensa magica = {self.mDef}\n    Defensa fisica = {self.pDef}\n    Precision = {self.accuracy}\n    Evacion = {self.evacion}\n    Critico = {self.rateCritical}\n    Velocidad de casteo = {self.castingSpeed}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'

class BossGobling:
    def __init__(self,nombre):
        self.nombre=nombre
        self.vida = 200
        self.mana = 200
        self.pAttack= 15
        self.mAttack = 2
        self.mDef=2
        self.pDef=2
        self.accuracy=3
        self.evacion=3
        self.rateCritical= 3
        self.castingSpeed= 3
        self.speed = 2
        self.attSpeed = 2
        self.nivel=5
    def calcularDaño(self,enemigo,multiplicador=1.0):
        aleatorio=random.randint(-5,5)
        daño=(self.pAttack*multiplicador)-enemigo.pDef+aleatorio
        if enemigo.vida <=100:
            enemigo.vida-=daño 
        return max(daño,0)
    def ataqueEspecial(self, enemigo, multiplicador=2.0):
        daño=self.calcularDaño(enemigo,multiplicador)
        if enemigo.vida <=100:
            enemigo.vida-=daño 
        print (f'{self.nombre} hizo {daño} ah {enemigo.nombre}\n queda en {enemigo.vida}')
        return daño
    """Metodo en el que se llama al que calcula el daño e imprime el daño hecho por el personaje a otro"""
    def atacar(self, enemigo):
        daño=self.calcularDaño(enemigo)
        print(f'{self.nombre} le ah hecho {daño} de daño a {enemigo.nombre}')
    def __str__(self):
        return f'{self.nombre}\n    Ataque fisico-> {self.pAttack}\n   Ataque magico -> {self.mAttack}\n    Defensa magica = {self.mDef}\n    Defensa fisica = {self.pDef}\n    Precision = {self.accuracy}\n    Evacion = {self.evacion}\n    Critico = {self.rateCritical}\n    Velocidad de casteo = {self.castingSpeed}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'












