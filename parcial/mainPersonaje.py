"""Se crea una clase PersonalePrincipal, la
cual tiene distintos metodos de interaccion."""
from armasOneHand import ArmaOneHand, rugidoDeAcero,  FiloSusurrante
import tkinter as tk
import random
from enemigos import *
from armasOneHand import ListaEnlazada
from arbolHabilidades import *
from arbolBinarioDeBusqueda import *
from combate import *
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
        daño=(self.pAttack*multiplicador)-enemigo.pDef+aleatorio
        return max(daño,0)
    """Metodo en el que se llama al que calcula el daño e imprime el daño hecho por el personaje a otro"""
    def atacar(self, enemigo):
        daño=self.calcularDaño(enemigo)
        print(f'{self.nombre} le ah hecho {daño} de daño a {enemigo.nombre}, quedando en = {self.vida - daño}')
        return enemigo.vida-daño
    """Segun el nivel del personaje va a tener distintas opciones para cambiar de clase"""


    def __str__(self):
        return f'{self.nombre}\n    Ataque fisico -> {self.pAttack}\n    Ataque magico -> {self.mAttack}\n    Defensa magica = {self.mDef}\n    Defensa fisica -> {self.pDef}\n    Precision -> {self.accuracy}\n    Evacion -> {self.evacion}\n    Critico -> {self.rateCritical}\n    Velocidad de casteo -> {self.castingSpeed}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}\n    Habilidad de arma uno = {self.habilidadUno}\n    Habilidad de arma secundaria = {self.habilidadDos}\n    Level = {self.nivel}'
miBoss = BossGobling("Gobling Boss")
miGobling = Gobling("Gobling")
miProtagonista = PersonajePrincipal("Robot prueba 'A'")  
miProtagonista.nivel=50     
protaDos = PersonajePrincipal("Amiga")
protaDos.nivel=10
protaTres = PersonajePrincipal("Amigo")
protaTres.nivel=15
primerArbolPersonajes = ArbolPersonajes()
primerArbolPersonajes.insertar(miProtagonista)
primerArbolPersonajes.insertar(protaDos)
primerArbolPersonajes.insertar(protaTres)
arbolHabilidadesProtagonista = ArbolHabilidades()
arbolHabilidadesProtagonista.agregarHabilidad("Destello mundial")
arbolHabilidadesProtagonista.agregarHabilidad("Fascinacion provincial","Destello mundial")
arbolHabilidadesProtagonista.agregarHabilidad("Putrefaccion en orden", "Destello mundial")
arbolHabilidadesProtagonista.agregarHabilidad("Espada de luz", "Putrefaccion en orden")
combate.agregarParticipante(miBoss)
combate.agregarParticipante(miGobling)
combate.agregarParticipante(miProtagonista)
combate.agregarParticipante(protaDos)
combate.agregarParticipante(protaTres)
combate.mostrarOrden()
     


    
root = tk.Tk()

def estadisticas1P():
    estadisticas.config(text=miProtagonista.__str__())
    button.grid_remove()
    buttonVolver.grid(row=3,column=2)

def volver():
    estadisticas.config(text=miProtagonista.nombre)
    buttonVolver.grid_remove()
    button.grid()

def estadisticas2P():
    estadisticas2Personaje.config(text=miGobling.__str__())
    button2P.grid_remove()
    buttonVolver2P.grid(row=3,column=4)

def volver2P():
    estadisticas2Personaje.config(text=miGobling.nombre)
    buttonVolver2P.grid_remove()
    button2P.grid()

def mostrarArbolHabilidades():
    habilidades = arbolHabilidadesProtagonista.mostrarHabilidades(arbolHabilidadesProtagonista.raiz)
    arbolDeMiPersonaje.config(text=habilidades)
    botonArbol.grid_remove()
    botonVolverArbol.grid(row=2,column=3)

def volverArbol():
    arbolDeMiPersonaje.config(text="Arbol de habilidades")
    botonVolverArbol.grid_remove()
    botonArbol.grid() 

root.geometry("1920x1080")
root.title("El Quinto anillo de los infiernos")

arbolDeMiPersonaje = tk.Label(root,text="Arbol de habilidades", font=("Acadian Runes", 12), width=50,height=15, relief = "raised", bg="#4CAF50")
arbolDeMiPersonaje.grid(row=3,column=3)
botonArbol = tk.Button(root, text = "Mostra arbol de habilidades", command=mostrarArbolHabilidades)
botonArbol.grid(row=2,column=3)
botonVolverArbol = tk.Button(root,text="Volver", command=volverArbol)

estadisticas = tk.Label(root,text=miProtagonista.nombre, font=("Acadian Runes", 12), width=50,height=15, relief = "raised", bg="#4CAF50")
estadisticas.config(padx=10, pady=10)
estadisticas.grid(row=2, column=2)
buttonVolver=tk.Button(root,text="Volver", command=volver)
button = tk.Button(root, text="Mostrar estadisticas", command=estadisticas1P)
button.grid(row=3,column=2)

#Aca se declara la interfaz de el enemigo con su boton de estadisticas.

estadisticas2Personaje = tk.Label(root,text=miGobling.nombre, font=("Acadian Runes", 12), width=50,height=15, relief = "raised", bg="#4CAF50")
estadisticas2Personaje.config(padx=10, pady=10)
estadisticas2Personaje.grid(row=2, column=4)
buttonVolver2P=tk.Button(root,text="Volver", command=volver2P)
button2P = tk.Button(root, text="Mostrar estadisticas", command=estadisticas2P)
button2P.grid(row=3,column=4)

root.mainloop()






