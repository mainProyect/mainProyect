"""Se crea una clase PersonalePrincipal, la
cual tiene distintos metodos de interaccion."""
import random
from enemigos import Gobling
class PersonajePrincipal:
    def  __init__(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("El nombre tiene que ser una cadena de caranteres")
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
        self.ataquesEspeciales = []
    """Metodo para subir de nivel a personaje mientas este Sea menor a 100"""
    def subirNivel(self, incrementoPAttack=1, 
                   incrementoMAttack=1,
                   incrementoMDef=1,
                   incrementoPDef = 1,
                   incrementoAccuracy=1,
                   incrementoEvacion=1,
                   incrementoRateCritical=1,
                   incrementoCastingSpeed=1,
                   incrementoSpeed=1,
                   incrementoAttspeed=1):
        if nivel<100:          
            self.nivel+=1
            self.vida = 100
            self.mana = 100
            self.pAttack= incrementoPAttack
            self.mAttack = incrementoMAttack
            self.mDef=incrementoMDef
            self.pDef=incrementoPDef
            self.accuracy=incrementoAccuracy
            self.evacion=incrementoEvacion
            self.rateCritical= incrementoRateCritical
            self.castingSpeed= incrementoCastingSpeed
            self.speed = incrementoSpeed
            self.attSpeed = incrementoAttspeed
        return self.nivel
    """Metodo para calcular el daño de un personaje hacia otro"""
    def calcularDaño(self,enemigo,multiplicador=1.0):
        aleatorio=random.randint(-5,5)
        daño=(self.pAttack*multiplicador)-enemigo.defensa+aleatorio
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
        return f'{self.nombre}\n    Ataque fisico-> {self.pAttack}\n   Ataque magico -> {self.mAttack}\n    Defensa magica = {self.mDef}\n    Defensa fisica = {self.pDef}\n    Precision = {self.accuracy}\n    Evacion = {self.evacion}\n    Critico = {self.rateCritical}\n    Velocidad de casteo = {self.castingSpeed}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'

                       
            



miProtagonista = PersonajePrincipal("Robot prueba 'A'")
print(miProtagonista.__str__())        
miGoblin=Gobling("AllStar")

miProtagonista.atacar(miGoblin)

