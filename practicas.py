class Pokemon:
    def __init__(self, nombre, tipo, nivel):
        if not isinstance(nombre, str) or not isinstance(tipo,str) or not isinstance(nivel, int):
            raise TypeError("Tipos de datos incorrectos para los atributos de Pokemon")
        self.nombre=nombre
        self.tipo=tipo
        self.nivel=nivel
        self. __validarNivel()
    def subirNivel(self):
        if self.nivel<100:
            self.nivel+=1
        else:
            print("El pokemon ya esta en el nivel maximo")
        return self.nivel
    def __str__(self):
        return (f'Pokemon:
                    Nombre: {self.nombre},
                    tipo: {self.tipo},
                    nivel: {self.nivel}')
miPokemon= Pokemon("Lechonk", "normal", 1)
miPokemon.subirNivel()
print(miPokemon.__str__())
    
