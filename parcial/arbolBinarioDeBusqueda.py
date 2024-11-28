class NodoPersonaje:
    def __init__(self, personaje):
        self.personaje = personaje  # Se guarda el personaje ingresado en el metodo insertar del arbol
        self.izquierda = None  # Hijo izquierdo iniciado en None
        self.derecha = None  # Hijo derecho iniciado en None

class ArbolPersonajes:
    def __init__(self):
        self.raiz = None  # Se inicia el arbol con una Raiz que inicia en None

    def insertar(self, personaje):
        """Inserta un personaje en el arbol en orden segun el nivel.(Esto camuflajea el metodo insertarRecursivo en privado)"""
        nuevoNodo = NodoPersonaje(personaje)
        if self.raiz is None:
            self.raiz = nuevoNodo
        else:
            self._insertarRecursivo(self.raiz, nuevoNodo)

    def _insertarRecursivo(self, nodoActual, nuevoNodo):
        """Método recursivo privado para insertar el nodo correctamente en el árbol binario."""
        if nuevoNodo.personaje.nivel < nodoActual.personaje.nivel:
            if nodoActual.izquierda is None:
                nodoActual.izquierda = nuevoNodo
            else:
                self._insertarRecursivo(nodoActual.izquierda, nuevoNodo)
        else:
            if nodoActual.derecha is None:
                nodoActual.derecha = nuevoNodo
            else:
                self._insertarRecursivo(nodoActual.derecha, nuevoNodo)

    def buscar(self, nivel):
        """Busca un personaje por su nivel.(Metodo usado como capa, para camuflar el metodo privado buscarRecursivo)"""
        return self._buscarRecursivo(self.raiz, nivel)

    def _buscarRecursivo(self, nodoActual, nivel):
        """Método recursivo privado para buscar el personaje por nivel."""
        if nodoActual is None:
            return None
        if nodoActual.personaje.nivel == nivel:
            return nodoActual.personaje
        elif nivel < nodoActual.personaje.nivel:
            return self._buscarRecursivo(nodoActual.izquierda, nivel)
        else:
            return self._buscarRecursivo(nodoActual.derecha, nivel)

    def eliminar(self, nivel):
        """Elimina un personaje por su nivel.(Mascara de el metodo privado eliminarRecursivo)"""
        self.raiz = self._eliminarRecursivo(self.raiz, nivel)

    def _eliminarRecursivo(self, nodoActual, nivel):
        """Método recursivo privado para eliminar un nodo del árbol."""
        if nodoActual is None:
            return nodoActual

        if nivel < nodoActual.personaje.nivel:
            nodoActual.izquierda = self._eliminarRecursivo(nodoActual.izquierda, nivel)
        elif nivel > nodoActual.personaje.nivel:
            nodoActual.derecha = self._eliminarRecursivo(nodoActual.derecha, nivel)
        else:
            # Nodo encontrado, ahora se elimina el nodo
            if nodoActual.izquierda is None:
                return nodoActual.derecha
            elif nodoActual.derecha is None:
                return nodoActual.izquierda
            else:
                # Nodo con dos hijos, buscar el nodo más pequeño en el subárbol derecho
                minimo = self._buscarMinimo(nodoActual.derecha)
                nodoActual.personaje = minimo.personaje
                nodoActual.derecha = self._eliminarRecursivo(nodoActual.derecha, minimo.personaje.nivel)

        return nodoActual

    def _buscarMinimo(self, nodo):
        """Busca el nodo con el valor más pequeño en un subárbol."""
        while nodo.izquierda is not None:
            nodo = nodo.izquierda
        return nodo

    def mostrarArbol(self, nodo, nivel=0):
        """Muestra el árbol en formato de texto."""
        if nodo:
            print(" " * (nivel * 4) + f"Nivel: {nodo.personaje.nivel} - {nodo.personaje.nombre}")
            self.mostrarArbol(nodo.izquierda, nivel + 1)
            self.mostrarArbol(nodo.derecha, nivel + 1)

