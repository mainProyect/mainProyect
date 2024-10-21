class PersonajePrincipal:
    def  __init__(self, nombre):
        if not isinstance(nombre,str):
            raise TypeError("El nombre tiene que ser una cadena de caranteres")
        self.nombre=nombre
        self.ataque = 1
        self.defensa = 1
        self.speed = 1
        self.attSpeed = 1
    def  __str__():
        return f'{self.nombre}\n    Ataque -> {self.ataque}\n   Defensa -> {self.defensa}\n    Speed -> {self.speed}\n    Velocidad de ataque -> {self.attSpeed}'


miProtagonista = PersonajePrincipal("Robot prueba 'A'")
print(miProtagonista.__str__())        

