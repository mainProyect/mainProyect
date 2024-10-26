from listaEnlazadaPersonajes import listaArmasOneHand
class ArmaOneHand:
    def __init__(self,nombre,pAtack,mAtack, tipo):
        if not isinstance(tipo,str) or not isinstance(nombre,str) or not isinstance(pAtack,int) or not isinstance(mAtack,int):
            raise  TypeError("Uno de los valores ingresados no es correcto")
        self.nombre = nombre
        self.pAtack = pAtack
        self.mAtack = mAtack
        self.tipo = tipo
        self.habilidad = None
    def __str__(self):
        return (f'{self.nombre}:\n    P.Atack = {self.pAtack}\n    M.Atack = {self.mAtack}\n    Tipo: {self.tipo}\n    Habilidad especial = {self.habilidad}')
rugidoDeAcero = ArmaOneHand("Rugido de Acero", 2,1, "Fist")
FiloSusurrante = ArmaOneHand("Filo Susurrante", 3,1,"Daga")
cortaViento = ArmaOneHand("Cortaviento", 4,2,"Espada")
dagaDeLaNiebla = ArmaOneHand("Daga de la Niebla", 3,1,"Daga")
garraDeLasSombras =ArmaOneHand("Garra de Sombras", 5,3, "Fist")
destelloDeCarmesi = ArmaOneHand("Destello Carmesí",1,7,"Baston")
golpeDelHalcon = ArmaOneHand("Golpe del Halcón", 10,5, "Fist")
mandibulaDelLoBo = ArmaOneHand("Mandíbula del Lobo", 20,10,"Fist")
listaArmasOneHand.agregar(rugidoDeAcero)
listaArmasOneHand.agregar(FiloSusurrante)
listaArmasOneHand.agregar(cortaViento)
listaArmasOneHand.agregar(dagaDeLaNiebla)
listaArmasOneHand.agregar(garraDeLasSombras)
listaArmasOneHand.agregar(destelloDeCarmesi)
listaArmasOneHand.agregar(golpeDelHalcon)
listaArmasOneHand.agregar(mandibulaDelLoBo)
listaArmasOneHand.mostrarLista()

"""Amanecer Ardiente
Grito del Dragón
Espina del Sol
Justiciera Fantasmal
Veneno de Sirena
Rompecielos
Tempestad de Cristal
Castigadora Élfica
Ocaso Plateado
Aguijón Celestial
Ígnea de los Ancestros
Desterrador Oscuro
Némesis del Caos
Filo del Inmortal
Colmillo de la Tempestad
Guardiana del Vacío
Juramento del Guerrero
Venganza del Espíritu
Ardiente del Infinito
Trueno de los Titanes
Juicio de los Dioses
"""