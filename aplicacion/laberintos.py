from aplicacion.util import Direcciones

class Laberinto:
    def __init__(self):
        self.gridSize = 60
        self.ancho = 660
        self.alto = 480
        self.estadoInicial = (1,1)
        self.estadoActual = self.estadoInicial
        self.objetivo = (8,5)
        self.costFn = lambda x: 1
    # Direcciones
    _direcciones = {Direcciones.ARRIBA: (0, -1),
                   Direcciones.ABAJO: (0, 1),
                   Direcciones.DERECHA:  (1, 0),
                   Direcciones.IZQUIERDA:  (-1, 0),
                   Direcciones.DETENER:  (0, 0)}

    _directionsAsList = _direcciones.items()

    def getEstadoInicial(self):
        return self.estadoInicial
    
    def getEstadoObjetivo(self):
        return self.objetivo

    def esObjetivo(self, estado):
        return estado == self.objetivo
    
    def expandir(self, estado):
        """
        Devuelve los estados hijos, la acción que se requiere y un costo de 1.

        Como se menciona en funciones.py:
             Para un estado dado, este método devuelve una lista de tripletas,
         (hijo, accion, costo), donde 'hijo' es un
         estado hijo o nodo hijo del nodo o estado actual, 'accion' es la acción
         requerida para llegar ahí, y 'costo' es el costo incremental
         de expandirse a ese hijo
        """

        hijos = []
        for accion in self.getAcciones(estado):
            siguienteEstado = self.getSiguienteEstado(estado, accion)
            cost = self.getCostoAccion(estado, accion, siguienteEstado)
            hijos.append( ( siguienteEstado, accion, cost) )
        
        return hijos
    

    def getAcciones(self, estado):
        posibles_acciones = [Direcciones.ARRIBA, Direcciones.ABAJO, Direcciones.DERECHA, Direcciones.IZQUIERDA]
        acciones_validas_desde_el_estado = []
        for accion in posibles_acciones:
            x, y = estado
            dx, dy = self._direcciones[accion]
            nextx, nexty = int(x + dx), int(y + dy)
            if (nextx, nexty) not in self.getParedes():
                acciones_validas_desde_el_estado.append(accion)
        return acciones_validas_desde_el_estado

    def getSiguienteEstado(self, estado, accion):
        assert accion in self.getAcciones(estado), (
            "Acción inválida enviada a getCostoAccion().")
        x, y = estado
        dx, dy = self._direcciones[accion]
        nextx, nexty = int(x + dx), int(y + dy)
        return (nextx, nexty)

    def getCostoAccion(self, estado, accion, siguienteEstado):
        assert siguienteEstado == self.getSiguienteEstado(estado, accion), (
            "Siguiente estado inválido enviado a getCostoAccion().")
        return self.costFn(siguienteEstado)

class LaberintoSmall(Laberinto):
    
    def __init__(self):
        self.gridSize = 60
        self.ancho = 660
        self.alto = 480
        self.estadoInicial = (1,1)
        self.estadoActual = self.estadoInicial
        self.objetivo = (8,5)
        self.costFn = lambda x: 1
    
    
    
    def getParedes(self):
        paredes = [(0,0), (1,0), (2,0), (3,0), (4,0), (5,0), (6,0), (7,0), (8,0), (9,0), 
                    (0,1), (0,2), (0,3), (0,4), (0,5), (0,6), (0,7),
                    (2,3), (2,4), (2,5), (3,5), (4,5), (4,4),
                    (2,2), (3,2), (4,2), (6,2), (7,2), (8,2),
                    (6,4),(6,5),(7,4),(7,5),
                    (10,0), (10,1), (10,2), (10,3), (10,4), (10,5), (10,6), (10,7),
                    (1,7),(2,7),(3,7),(4,7),(5,7),(6,7),(7,7),(8,7),(9,7)]
        return paredes
    

class LaberintoMediano(Laberinto):
    def __init__(self):
        self.gridSize = 30
        self.ancho = 960
        self.alto = 540
        self.estadoInicial = (1,1)
        self.estadoActual = self.estadoInicial
        self.objetivo = (1,16)
        self.costFn = lambda x: 1
    
    def getParedes(self):
        paredes = []
        for x in range(0,32):
            paredes.append((x,0))
        for x in range(0,32):
            paredes.append((x,17))
        for y in range(0, 18):
            paredes.append((31,y))
        for y in range(0, 18):
            paredes.append((0,y))

        paredes.append((1,15))
        paredes.append((2,15))
        paredes.append((3,15))
        paredes.append((2,14))
        paredes.append((2,13))
        paredes.append((2,12))
        paredes.append((3,12))
        paredes.append((4,12))
        paredes.append((2,2))
        paredes.append((2,3))
        paredes.append((3,2))
        paredes.append((4,2))
        paredes.append((2,4))
        paredes.append((2,5))
        paredes.append((3,5))
        paredes.append((4,5))
        for x in range(6,29):
            paredes.append((x,2))
        for y in range(3,7):
            paredes.append((28,y))

        return paredes

class LaberintoMediano2(Laberinto):
    def __init__(self):
        self.gridSize = 30
        self.ancho = 960 # 32 cuadros
        self.alto = 540  # 18 cuadros
        self.estadoInicial = (1,1)
        self.estadoActual = self.estadoInicial
        self.objetivo = (1,16)
        self.costFn = lambda x: 1
    
    def getParedes(self):
        paredes = [(30,13), (29,13), (28,13), (27,13), (26,13), (26,12), (26,11), (26,10), (26,9), (26,8), (26,7), 
                    (26,6), (26,5), (26,4), (24,3), (24,4), (24,5), (24,6), (24,7), (24,8), (24,9), (24,10), 
                    (28,3), (28,4), (28,5), (28,6), (28,7), (28,9), (28,10), (28,11), 
                    (25,12), (24,12), (23, 12), (22, 12), (22,11), (22,10), (22,9), (22,8), (22,7), (22,6), 
                    (22,5), (22,4), (20,3), (20,4), (20,5),(20,6),(20,7),(20,8), (22, 10), (21, 10), (20, 10), (19,10),
                    (18,10), (18, 9), (18, 8), (18,6), (17,6), (16,6), (18,4), (17,4), (16,4), (15,4), (14,4), 
                    (14,3), (14,5), (14,6), (16,8), (15,8), (14,8), (12,8), (11,8), (9,7), (7,9),
                    (8,9), (9,9),
                    (9,6), (10,6), (11,6), (12,6), (13,6), (9,5), (9,4), (9,3),
                    (5,4), (6,4), (5,5), (6,5), (7,4), (7,5), (7,6), (7,7),
                    (17, 12), (17, 13),(17, 14), (18,14), (19,14), (20,14), (18,12), (19,12), (20,12), (20,13), (20,14),
                    (21,14), (22,14), (23,14), (24,14),
                    (22,15), (23,15), (24,15), (25,15), (26,15), (27,15), (28,15), (29,15),
                    (14,9), (15,9), (16,9), (16,10), (16,11), (16,12), (16,13), (16,14),
                    (11,9), (12,9), (11,10), (12,10), (11,11), (12,11), (13,11), (14,11),
                    (15,13), (14,13), (13,13), (12,13), (11,13), (10,13),
                    (15,14), (14,14), (13,14), (12,14), (11,14), (10,14), (10,15),
                    (5,15), (6,15), (7,15), (8,15), (9,15),
                    (6,11), (6,12), (6,13), (7,11), (7,13), (8,11), (8,12), (8,13),
                    (9,11), (10,11),
                    (1,7), (2,7), (3,7), (4,7), (5,7), (5,8), (2,9), (3,9), (4,9), (5,9), (6,9),
                    (2,10), (3,10), (4,10)]

        for x in range(2, 6):
            paredes.append((x,2))
        for x in range(7, 13):
            paredes.append((x,2))
        for x in range(14, 16):
            paredes.append((x,2))
        for x in range(17, 30):
            paredes.append((x,2))
        for y in range(3, 12):
            paredes.append((29,y))
        for x in range(12,21):
            paredes.append((x,16))
        #bordes
        for x in range(0,32):
            paredes.append((x,0))
        for x in range(0,32):
            paredes.append((x,17))
        for y in range(0, 18):
            paredes.append((31,y))
        for y in range(0, 18):
            paredes.append((0,y))

        paredes.append((1,15))
        paredes.append((2,15))
        paredes.append((3,15))
        paredes.append((2,14))
        paredes.append((2,13))
        paredes.append((2,12))
        paredes.append((3,12))
        paredes.append((4,12))
        paredes.append((2,3))
        paredes.append((2,5))
        paredes.append((3,5))
        paredes.append((4,5))

        return paredes

class LaberintoMediano3(Laberinto):
    def __init__(self):
        self.gridSize = 20
        self.ancho = 960 # 48 cuadros
        self.alto = 540  # 27 cuadros
        self.estadoInicial = (1,1)
        self.estadoActual = self.estadoInicial
        self.objetivo = (46,25)
        self.costFn = lambda x: 1
    
    def getParedes(self):
        paredes = []

        for x in range(2, 6):
            paredes.append((x,2))
        for x in range(7, 13):
            paredes.append((x,2))
        for x in range(14, 16):
            paredes.append((x,2))
        for x in range(27, 33):
            paredes.append((x, 13))
        for x in range(34, 48):
            paredes.append((x, 13))

        for y in range(14, 20):
            paredes.append((27, y))
        for x in range(21, 27):
            paredes.append((x, 19))

        for x in range(17, 46):
            paredes.append((x,2))
        for y in range(3, 12):
            paredes.append((45,y))
        for x in range(42,45):
            paredes.append((x, 11))
        for x in range(12,21):
            paredes.append((x,16))
        #bordes
        for x in range(0,48):
            paredes.append((x,0))
        for x in range(0,48):
            paredes.append((x,26))
        for y in range(0, 27):
            paredes.append((47,y))
        for y in range(0, 27):
            paredes.append((0,y))

        paredes.append((1,15))
        paredes.append((2,15))
        paredes.append((3,15))
        paredes.append((2,14))
        paredes.append((2,13))
        paredes.append((2,12))
        paredes.append((3,12))
        paredes.append((4,12))
        paredes.append((2,3))
        paredes.append((2,5))
        paredes.append((3,5))
        paredes.append((4,5))

        return paredes

class CuatroEsquinas(Laberinto):

    def __init__(self):
        self.gridSize = 30
        self.ancho = 960
        self.alto = 540
        self.estadoInicial = (14,7)
        self.estadoActual = self.estadoInicial
        self.objetivo = [(1,1), (1,16), (30, 1), (30, 16)]
        self.objetivos = 4
        self.objetivosEncontrados = []
        self.costFn = lambda x: 1
    
    def esObjetivo(self, estado):
        if estado in self.objetivo:
            self.objetivos -= 1
            self.objetivosEncontrados.append(estado)
        return self.objetivos == 0

    def getEstadoObjetivo(self):
        obj = self.objetivo[0]
        for objetivo in self.objetivo:
            if objetivo not in self.objetivosEncontrados:
                obj = objetivo
        return obj
    
    def getParedes(self):
        paredes = []
        for x in range(0,32):
            paredes.append((x,0))
        for x in range(0,32):
            paredes.append((x,17))
        for y in range(0, 18):
            paredes.append((31,y))
        for y in range(0, 18):
            paredes.append((0,y))

        paredes.append((1,15))
        paredes.append((2,15))
        paredes.append((3,15))
        paredes.append((2,14))
        paredes.append((2,13))
        paredes.append((2,12))
        paredes.append((3,12))
        paredes.append((4,12))
        paredes.append((2,2))
        paredes.append((2,3))
        paredes.append((3,2))
        paredes.append((4,2))
        paredes.append((2,4))
        paredes.append((2,5))
        paredes.append((3,5))
        paredes.append((4,5))

        return paredes
    