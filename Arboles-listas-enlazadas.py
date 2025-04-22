# 2241917 - Vanessa Martinez Angarita
class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.hijos = []

class Arbol:
    def __init__(self):
        self.raiz = None
        self.nodos = {}  

    def agregarNodo(self, dato, padre=None):
        nuevo = Nodo(dato)
        self.nodos[dato] = nuevo

        if padre is None:
            self.raiz = nuevo
        else:
            self.nodos[padre].hijos.append(nuevo)

    def mostrar(self, nodo=None, nivel=0):
        if nodo is None:
            nodo = self.raiz
        print("  " * nivel + f"- {nodo.dato}")
        for hijo in nodo.hijos:
            self.mostrar(hijo, nivel + 1)

    def peso(self):
        if self.raiz is None:
            return 0
        total = 1
        nodos = [self.raiz]
        while nodos:
            actual = nodos.pop()
            for hijo in actual.hijos:
                total += 1
                nodos.append(hijo)
        return total

    def altura(self):
        def calcular(nodo):
            if not nodo.hijos:
                return 1
            alturas = []
            for hijo in nodo.hijos:
                alturas.append(calcular(hijo))
            maximo = 0
            for a in alturas:
                if a > maximo:
                    maximo = a
            return 1 + maximo

        return calcular(self.raiz) if self.raiz else 0

    def orden(self):
        def calcular(nodo):
            hijosActuales = 0
            for _ in nodo.hijos:
                hijosActuales += 1
            mayor = hijosActuales
            for hijo in nodo.hijos:
                hijosdelhijo = calcular(hijo)
                if hijosdelhijo > mayor:
                    mayor = hijosdelhijo
            return mayor

        return calcular(self.raiz) if self.raiz else 0
        
def main():
    arbol = Arbol()

    cantidad = int(input("Cuantos nodos va a ingresar? "))

    for i in range(cantidad):
        dato = input(f"Nombre del nodo {i+1} ")
        if i == 0:
            arbol.agregarNodo(dato)
        else:
            padre = input(f"Quién es el padre de {dato}? ")
            if padre not in arbol.nodos:
                print("El padre ngresado no existe. Comience de nuevo")
                return
            arbol.agregarNodo(dato, padre)

    print("\n--- Árbol ---")
    arbol.mostrar()

    print("\n--- Datos ---")
    print("Peso:", arbol.peso())
    print("Altura:", arbol.altura())
    print("Orden:", arbol.orden())

if __name__ == "__main__":
    main()
    
