class Nodo:
    def __init__(self,dato):
        self.dato = dato
        self.next = None
class ListaEnlazada:
    def __init__(self):
        self.head = None
    def agregar(self,nuevoData):
        nuevoPersonaje = Nodo(nuevoData)
        if self.head is None:
            self.head = nuevoPersonaje
        else:
            actual = self.head
            while actual.next is not None:
                actual = actual.next
            actual.next = nuevoPersonaje
    def mostrarLista(self):
        actual = self.head
        while actual is not None:
            print(actual.dato.__str__())
            actual = actual.next
listaArmasOneHand = ListaEnlazada()