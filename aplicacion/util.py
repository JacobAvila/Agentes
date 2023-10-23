
"""
 Estructuras de datos para la implementación de los algoritmos de búsqueda
"""

"""
 Clase Pila
"""
import heapq
import inspect

class Pila:
    "Estructura tipo pila con la política (LIFO) el último que entra es el primero que sale."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Push 'item' agrega un elemento a la pila"
        self.list.append(item)

    def pop(self):
        "Pop devuelve y elimina el último elemento ingresado a la pila"
        return self.list.pop()

    def isEmpty(self):
        "Devuelve verdadero si la pila está vacía"
        return len(self.list) == 0




"""
 Clase Cola
"""
class Cola:
    "Estructura tipo cola con la política (FIFO) el primero que entra es el primero que sale."
    def __init__(self):
        self.list = []

    def push(self,item):
        "Encola el elemento 'item' dentro de la cola"
        self.list.insert(0,item)

    def pop(self):
        """
          Desencola el primer elemento encolado que exista en la estructura. Esta
          operación elimina el elemento de la cola.
        """
        return self.list.pop()

    def isEmpty(self):
        "Devuelve verdadero si la cola está vacía"
        return len(self.list) == 0




"""
 Clase Cola de Prioridaqd
"""
class ColaPrioridad:
    """
      Implementa una estructura de datos tipo cola de prioridad. Donde cada elemento
      insertado tiene una prioridad asociada con el y el cliente normalmente se inserta
      en una recuperación rápida del elemento con la prioridad más baja.
    """
    def  __init__(self):
        self.heap = []
        self.count = 0

    def push(self, item, priority):
        entry = (priority, self.count, item)
        heapq.heappush(self.heap, entry)
        self.count += 1

    def pop(self):
        (_, _, item) = heapq.heappop(self.heap)
        return item

    def isEmpty(self):
        return len(self.heap) == 0

    def update(self, item, priority):
        # Si el elemento ya se encuentra en la cola de prioridad con la más alta prioridad, 
        # actualiza su prioridad y reconstruye el heap (la cola por prioridad).
        # Si el elemento ya se encuentra en la cola de prioridad con la misma o con menor prioridad, no hace nada.
        # Si el elemento no está en la cola de prioridad, hace lo mismo que el simple push.
        for index, (p, c, i) in enumerate(self.heap):
            if i == item:
                if p <= priority:
                    break
                del self.heap[index]
                self.heap.append((priority, c, item))
                heapq.heapify(self.heap)
                break
        else:
            self.push(item, priority)

class Direcciones:
    ARRIBA = 'Arriba'
    ABAJO = 'Abajo'
    DERECHA = 'Derecha'
    IZQUIERDA = 'Izquierda'
    DETENER = 'Detener'

    IZQ=       {ARRIBA: IZQUIERDA,
                   ABAJO: DERECHA,
                   DERECHA:  ARRIBA,
                   IZQUIERDA:  ABAJO,
                   DETENER:  DETENER}
                
    DER =      dict([(y,x) for x, y in IZQ.items()])
    
    REVERSA = {ARRIBA: ABAJO,
               ABAJO: ARRIBA,
               DERECHA: IZQUIERDA,
               IZQUIERDA: DERECHA,
               DETENER: DETENER}

    


def raiseNotDefined():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Método no implementado: %s en la línea %s de %s" % (method, line, fileName))

def raiseMovimientoIlegal():
    fileName = inspect.stack()[1][1]
    line = inspect.stack()[1][2]
    method = inspect.stack()[1][3]

    print("*** Movimiento ilegal al chocar con pared: %s en la línea %s de %s" % (method, line, fileName))