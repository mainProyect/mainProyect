class Nodo:
    def __init__(self,valor):
        self.valor= valor
        self.izquierda = None
        self.derechar = None
class arbolBinario:
    def __init__(self):
        self.raiz= None
        
    def agregar(self,valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self.raiz
    def _agregarRecursivo(self, nodo, valor):
        if valor< nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._agregarRecursivo(nodo.izquierdo,valor)
        else:
            if nodo.derecho is None:
                nodo.derecho = Nodo(valor)
            else:
                self._agregarRecursivo(nodo.derecho,valor)
                