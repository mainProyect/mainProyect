class Mago(PersonajePrincipal):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.pAttack+= 1
        self.mAttack += 5
        self.mDef+=2
        self.pDef+=1
        self.accuracy+=incrementoAccuracy
        self.evacion+=incrementoEvacion
        self.rateCritical+=incrementoRateCritical
        self.castingSpeed+=incrementoCastingSpeed
        self.speed +=incrementoSpeed
        self.attSpeed +=incrementoAttspeed
    