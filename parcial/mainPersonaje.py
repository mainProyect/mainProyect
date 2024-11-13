"""Se crea una clase PersonalePrincipal, la
cual tiene distintos metodos de interaccion."""
from armasOneHand import ArmaOneHand, rugidoDeAcero,  FiloSusurrante
import tkinter as tk
import random
from enemigos import Gobling
from armasOneHand import ListaEnlazada
fuente = "C:\Windows\Fonts"
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
        self.habilidadUno=[]
        self.habilidadDos=[]
        self.armaUno = []
        self.armaDos = []
    """Metodo para subir de nivel a personaje mientas este Sea menor a 100"""
    def subirNivel(self, incrementoPAttack=1, incrementoMAttack=1,incrementoPDef = 1,incrementoMDef=1,incrementoAccuracy=1,incrementoEvacion=1,incrementoRateCritical=1,incrementoCastingSpeed=1,incrementoSpeed=1,incrementoAttspeed=1):
        if self.nivel<100:          
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
        return self
    """Metodo para calcular el daño de un personaje hacia otro"""
    def agregarArmaUno(self,arma):
        if not isinstance(arma,ArmaOneHand):
            raise TypeError("El arma no es una instancia de armas de una mano")
        else:
            self.armaUno.append(arma)
            print(f"Arma uno de {self.nombre} equipado con {arma.nombre}")
            self.habilidadUno=arma.habilidad
    def agregarArmaDos(self,arma):
        if not isinstance(arma,ArmaOneHand):
            raise TypeError("El arma no es una instancia de armas de una mano")
        else:
            self.armaDos.append(arma)
            print(f"Arma dos de {self.nombre} equipado con {arma.nombre}")
            self.habilidadDos=arma.habilidad
        
    def calcularDaño(self,enemigo,multiplicador=1.0):
        aleatorio=random.randint(-5,5)
        daño=(self.pAttack*multiplicador)-enemigo.defensa+aleatorio
        return max(daño,0)
    """Metodo en el que se llama al que calcula el daño e imprime el daño hecho por el personaje a otro"""
    def atacar(self, enemigo):
        daño=self.calcularDaño(enemigo)
        print(f'{self.nombre} le ah hecho {daño} de daño a {enemigo.nombre}')
    """Segun el nivel del personaje va a tener distintas opciones para cambiar de clase"""


    def __str__(self):
        return f'{self.nombre}\n    Ataque fisico -> {self.pAttack}\n    Ataque magico -> {self.mAttack}\n    Defensa magica = {self.mDef}\n    Defensa fisica -> {self.pDef}\n    Precision -> {self.accuracy}\n    Evacion -> {self.evacion}\n    Critico -> {self.rateCritical}\n    Velocidad de casteo -> {self.castingSpeed}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}\n    Habilidad de arma uno = {self.habilidadUno}\n    Habilidad de arma secundaria = {self.habilidadDos}'

miProtagonista = PersonajePrincipal("Robot prueba 'A'")       
miGoblin=Gobling("AllStar")
miProtagonista.agregarArmaUno(rugidoDeAcero)
miProtagonista.agregarArmaDos(FiloSusurrante)

def gana():
    estadisticas.config(text=miProtagonista.__str__())
root = tk.Tk()
root.title("El Quinto anillo de los infiernos")
estadisticas = tk.Label(root,text=miProtagonista.nombre, font=("Acadian Runes", 12), width=50,height=15, relief = "raised", bg="#4CAF50")
estadisticas.config(padx=10, pady=10)
estadisticas.grid(row=1, column=2)

button = tk.Button(root, text="Mostrar estadisticas", command=gana)
button.grid(row=2,column=2)
root.mainloop()






