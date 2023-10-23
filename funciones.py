from aplicacion.util import Pila, Cola, ColaPrioridad
import time
"""
Busqueda
Implementación de las funciones para Búsqueda desinformada e informada
Búsqueda en Profundidad, Búsqueda en Arnchura y Búsqueda A*

Cada función debe devolver una lista con los movimientos válidos para que el agente se desplace del estado inicial
al objetivo.

Los movimientos válidos son: 
    Arriba 
    Abajo 
    Izquerda 
    Derecha

Por ejemplo, la función deberá devolver una lista como esta: 
['Abajo', 'Abajo', 'Abajo', 'Derecha', 'Derecha', 'Abajo', 'Derecha'. ...]

Lo que hará que el ajente se desplace paso a paso con cada una de las instrucciones de un estado a otro.

Un estado consta de las coordenadas en las que se encuentra o se puede desplazar el agente formado por un 
set de la forma (x,y).
Donde x es el eje horizontal que se incrementa a la derecha y se decrementa a la izquiera
y es el eje vertical que se incremento hacia abajo y se decrementa hacia arriba.

Por ejemplo: 
    Si el ajente se encuentra en la posición (1,1) su estado actual es (1,1) y si se desplaza un paso hacia la derecha
    su estado final será (2,1)

El algoritmo de búsqueda deberá generar la secuencia de acciones a seguir para llegar al objetivo.
El mismo algoritmo de cada tipo de búsqueda debe funcionar con todos los laberintos

El objeto laberinto tiene varios métodos que se reqieren para obtener la información que se necesita para establecer
las acciones válidas del agente.

Para almacenar los movimientos del agente, en el archivo util, que ya esta incorporado existen las funciones
para las estructuras de datos necesarias para cada tipo de búsqueda: Pila, Cola, ColaPrioridad

Cada función (Pila, Cola, ColaPrioridad) tiene los métodos push(item), pop(), isEmpty() para agregar un elemento,
sacar el elemento en turno y verificar si la estructura está vacía, respectivametne. 

Laberinto
getEstadoInicial() - devuelve el estado inicial del agente, el punto de partida.

esObjetivo(estado) - recibe el estado actual del agente y verifica si ya es el objetivo o no. Devuelve True si lo es, 
                    o False si no es el objetivo.

expandir(nodo) - recibe al nodo actual y devuelve una lista con los nodos hijos del nodo actual. Cada nodo hijo se conforma
                como (hijo, accion, costo), es decir, el nodo hijo, la acción para llegar a el (Arriba, Abajo, Izquierda, Derecha)
                y el costo para llegar a ese nodo hijo utilizando esa acción.

getCostoAccion(nodoActial, accion, nodoSiguiente) - devuelve el costo de pasar del estado actual al siguiente siguiente
                                                    dada la accion enviada (Arriba, Abajo, Izquierda o Derecha)


"""
class Busqueda:

    def busquedaEnProfundidad(self, laberinto):
        timeInicio = time.monotonic()
        timeFin = 0.0
        frontera = Pila()
        frontera.push(laberinto.getEstadoInicial())
        expanded = {}
        padre = {}
        while not frontera.isEmpty():
            nodo = frontera.pop()
            if laberinto.esObjetivo(nodo):
                expanded[nodo] = nodo
                timeFin = time.monotonic()
                print("tiempo: ",timeFin - timeInicio)
                path = self.crearRuta(expanded, padre)
                print("distancia: ", len(path))
                return path
            if nodo not in expanded.keys():
                expanded[nodo] = nodo
                hijos = laberinto.expandir(nodo)
                for hijo in hijos:
                    if hijo[0] not in expanded.keys() and hijo not in padre.values():
                        frontera.push(hijo[0])
                        padre[hijo[0]] = (nodo, hijo[1], hijo[2])
        return []
        

    def busquedaEnAnchura(self, laberinto):
        timeInicio = time.monotonic()
        timeFin = 0.0
        frontera = Cola()
        frontera.push(laberinto.getEstadoInicial())
        expanded = {}
        padre = {}
        while not frontera.isEmpty():
            nodo = frontera.pop()
            if laberinto.esObjetivo(nodo):
                expanded[nodo] = nodo
                timeFin = time.monotonic()
                print("tiempo: ",timeFin - timeInicio)
                path = self.crearRuta(expanded, padre)
                print("distancia: ", len(path))
                return path
            if nodo not in expanded.keys():
                expanded[nodo] = nodo
                hijos = laberinto.expandir(nodo)
                for hijo in hijos:
                    if hijo[0] not in expanded.keys() and hijo not in padre.values():
                        frontera.push(hijo[0])
                        padre[hijo[0]] = (nodo, hijo[1], hijo[2])
        return []
        
    

    def busquedaAestrella(self, laberinto):
        timeInicio = time.monotonic()
        timeFin = 0.0
        frontera = ColaPrioridad()
        frontera.push(laberinto.getEstadoInicial(), 0)
        expanded = {}
        padre = {}
        costos = {}
        costos[laberinto.getEstadoInicial()] = 0
        while not frontera.isEmpty():
            nodo = frontera.pop()
            if laberinto.esObjetivo(nodo):
                expanded[nodo] = nodo
                timeFin = time.monotonic()
                print("tiempo: ",timeFin - timeInicio)
                path = self.crearRuta(expanded, padre)
                print("distancia: ", len(path))
                return path
            if nodo not in expanded.keys():
                expanded[nodo] = nodo
                hijos = laberinto.expandir(nodo)
                for hijo in hijos:
                    costos[hijo[0]] = costos[nodo] + 1
                    h = self.manhattanHeuristic(hijo[0], laberinto)
                    if hijo[0] not in expanded.keys() and hijo not in padre.values():
                        costoTotal = costos[hijo[0]] + h
                        frontera.push(hijo[0], costoTotal)
                        padre[hijo[0]] = (nodo, hijo[1], hijo[2])
        return []

    def cuatroEsquinas(self, laberinto):
        #--Aquí va tu Código--
        frontera = ColaPrioridad()
        frontera.push(laberinto.getEstadoInicial(), 0)
        expanded = {}
        padre = {}
        costos = {}
        costos[laberinto.getEstadoInicial()] = 0
        while not frontera.isEmpty():
            nodo = frontera.pop()
            if laberinto.esObjetivo(nodo):
                expanded[nodo] = nodo
                return self.crearPath3(expanded, padre)
            if nodo not in expanded.keys():
                expanded[nodo] = nodo
                hijos = laberinto.expandir(nodo)
                for hijo in hijos:
                    costos[hijo[0]] = costos[nodo] + 1
                    h = self.manhattanHeuristic(hijo[0], laberinto)
                    if hijo[0] not in expanded.keys() and hijo not in padre.values():
                        costoTotal = costos[hijo[0]] + h
                        frontera.push(hijo[0], costoTotal)
                        padre[hijo[0]] = (nodo, hijo[1], hijo[2])
        
        return []
    
    #Heurística Nula
    def nullHeuristic(self, state, laberinto=None):
        """
        Una función heurística estima el costo desde el estado actual al objetivo
        más cercano en el laberinto proporcionado.  Esta es la heurística trivial.
        """
        return 0
    
    #Heurística de Manhattan
    def manhattanHeuristic(self, posicion, laberinto, info={}):
        "La distancia de Manhattan"
        xy1 = posicion  
        xy2 = laberinto.getEstadoObjetivo()
        return abs(xy1[0] - xy2[0]) + abs(xy1[1] - xy2[1])

    #Heurística Euclidiana
    def euclideanHeuristic(self, posicion, laberinto, info={}):
        "The distancia Euclidiana"
        xy1 = posicion 
        xy2 = laberinto.getEstadoObjetivo()
        return ( (xy1[0] - xy2[0]) ** 2 + (xy1[1] - xy2[1]) ** 2 ) ** 0.5
    
    def crearPath(self, problem, expanded, cameFrom):
        valores = list(expanded.values())
        start = valores[0][0]
        current = valores[len(valores)-1][0]
        valores.reverse()
        path = []
        nodos = [valores[0][0]]
        while current != start:
            path.append(expanded[current][1])
            current = cameFrom[current][0]
        
        path.reverse()
        print("Start State: ", problem.getEstadoInicial())
        print("Goal State: ", problem.getEstadoObjetivo())
        #print("Walls: ", problem.getParedes())
        print("Path: ", path)
        return path
    
    def crearPath2(self, laberinto, expanded):
        valores = list(expanded.values())
        valores.reverse()
        path = []
        nodos = [valores[0][0]]
        for n in nodos:
            for nodo in valores:
                acciones = laberinto.getAcciones(nodo[0])
                for accion in acciones:
                    if accion == expanded[n][1] and laberinto.getSiguienteEstado(nodo[0], expanded[n][1]) == n:
                        if nodo[0] not in nodos:
                            nodos.append(nodo[0])
                            path.append(expanded[n][1])
        
        path.reverse()
        return path
    
    def crearPath3(self, expanded, padre):
        #print(expanded)
        #print("*********************************")
        #print(padre)

        ruta = []
        listaExpanded = list(expanded.values())
        primero = listaExpanded[0]
        ultimo = listaExpanded[len(listaExpanded) - 1]

        while primero != ultimo:
            nodo = padre[ultimo]
            ultimo = nodo[0]
            ruta.append(nodo[1])

        ruta.reverse()
        return ruta
    
    def crearRuta(self, expanded, padre):
        ruta = []
        listaExpanded = list(expanded.values())
        primero = listaExpanded[0]
        ultimo = listaExpanded[len(listaExpanded) - 1]

        while primero != ultimo:
            nodo = padre[ultimo]
            ultimo = nodo[0]
            ruta.append(nodo[1])

        ruta.reverse()
        return ruta