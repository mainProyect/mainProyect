class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        if not isinstance(nombre, str) or not isinstance(tipo,str) or not isinstance(nivel, int):
            raise TypeError("Tipos de datos incorrectos para los atributos de Pokemon")
        self.nombre=nombre
        self.tipo=tipo
        self.nivel=nivel
        self. __validarNivel()
    def __validarNivel(self):
        if not (1<= self.nivel <=100):
            raise ValueError("El nivel debe estar entre 1 y 100")
    def subirNivel(self):
        if self.nivel<100:
            self.nivel+=1
        else:
            print("El pokemon ya esta en el nivel maximo")
        return self.nivel
    def __str__(self):
        return (f'Pokemon:\n Nombre: {self.nombre}\n tipo: {self.tipo}\n nivel: {self.nivel}')
"""Se crea una clase Pokemon, con atributos Nombre, Tipo y nivel, se verifica que sean del tipo adecuado (STR/INT), 
"""
class Entrenador:
    def __init__(self,nombre, equipo):
        if not isinstance(nombre, str):
            raise TyperError("El nombre del entrenador tiene que ser una cadena de caracteres")
        self.nombre = nombre
        self.equipo= []

miPokemon= Pokemon("Lechonk", "normal", 1)
miPokemon.subirNivel()
print(miPokemon.__str__())
    

