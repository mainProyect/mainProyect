"""Se crea una clase PersonalePrincipal, la
cual tiene distintos metodos de interaccion."""
class PersonajePrincipal:
    def  __init__(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("El nombre tiene que ser una cadena de caranteres")
        self.nombre=nombre
        self.ataque = 1
        self.defensa = 1
        self.speed = 1
        self.attSpeed = 1
        self.nivel=1
    def subirNivel(self):
        self.nivel+1
        return self.nivel
    def cambiarDeClase(self):
        if self.nivel=5:
            print(f'{self.nombre}, ah alcanzado el nivel 5, cambia de clase.')
            return Mago(self, nombre)
        return self
    def  __str__(self):
        return f'{self.nombre}\n    Ataque -> {self.ataque}\n   Defensa -> {self.defensa}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'
    


class Mago(PersonajePrincipal):
    def __init__(self, nombre):
        super().__init__(self,nombre)

miProtagonista = PersonajePrincipal("Robot prueba 'A'")
print(miProtagonista.__str__())        

