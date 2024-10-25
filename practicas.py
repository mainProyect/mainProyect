"""Se crea una clase PersonalePrincipal, la
cual tiene distintos metodos de interaccion."""
import random
class PersonajePrincipal:
    def  __init__(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("El nombre tiene que ser una cadena de caranteres")
        self.nombre=nombre
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
    """Metodo para subir de nivel a personaje mientas este Sea menor a 100"""
    def subirNivel(self, incrementoPAttack=1, 
                   inceementomMAttack=1
                   incrementoPDef = 1,
                   incrementoMDef=1,
                   incrementoAccuracy=1,
                   incrementoEvacion=1,
                   incrementoRateCritical=1,
                   incrementoCastingSpeed=1,
                   incrementoSpeed=1,
                   incrementoAttspeed=1):
            if not isinstance(self,PersonajePrincipal())
        self.nivel+=1
        self.pAttack+=incrementoPAttack
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
class Mago(PersonajePrincipal):
      def __init__(self):
          super.__init__(nombre):
          self.ataque
            



miProtagonista = PersonajePrincipal("Robot prueba 'A'")
print(miProtagonista.__str__())        
miGoblin=Gobling("AllStar")

miProtagonista.atacar(miGoblin)

