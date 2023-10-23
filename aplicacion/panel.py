import tkinter
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import *
import math, time
from aplicacion.laberintos import LaberintoSmall, LaberintoMediano, LaberintoMediano2, LaberintoMediano3, CuatroEsquinas
from funciones import Busqueda
from aplicacion import util

class Panel:
    def __init__(self, tablero, root, canvas):
        self.tablero = tablero
        self.root = root
        self.canvas = canvas
        self.mostrar()
    
    def mostrar(self):
        font = ('Helvetica', str(12), 'bold')
        titulo = tkinter.Label(self.root, text="Inteligencia Artificial", font=font, fg="white", bg="green")
        titulo.pack(side=tkinter.TOP)
        
        descripcion = tkinter.Label(self.root, 
                        text="Escenarios para agentes inteligentes\nen la ejecución de algoritmos de búsqueda", 
                        fg="white", 
                        bg="green", padx=10)
        descripcion.pack()
        
        lLaberinto = tkinter.Label(self.root, text="Laberinto", fg="white", bg="green")
        lLaberinto.pack(pady=(20,0))
        self.cLaberinto = Combobox(self.root, state="readonly",
                                values=["", "Sencillo", "Elaborado Opción 1", "Elaborado Opción 2", "Elaborado Opción 3", "Cuatro Esquinas"])
        self.cLaberinto.bind("<<ComboboxSelected>>", self.mostrarLaberinto)
        self.cLaberinto.pack()

        lAlgoritmo = tkinter.Label(self.root, text="Algoritmo de Búsqueda", fg="white", bg="green")
        lAlgoritmo.pack(pady=(20,0))
        self.cAlgoritmo = Combobox(self.root, state="readonly",
                                values=["", "Manual", "Búsqueda en Profundidad", "Búsqueda en Anchura", "Búsqueda A*"])
        self.cAlgoritmo.bind("<<ComboboxSelected>>", self.selAlgoritmo)
        self.cAlgoritmo.pack()

        bEjecutar = Button(self.root, text="Ejecutar", command=self.ejecutarBusqueda)
        bEjecutar.pack(pady=(30,0))
    
    def mostrarLaberinto(self, event):
        self.tablero.canvas.delete('all')

        laberinto = event.widget.get()
        if laberinto == "Sencillo":
            self.tablero.laberinto = LaberintoSmall()
        if laberinto == "Elaborado Opción 1":
            self.tablero.laberinto = LaberintoMediano()
        if laberinto == "Elaborado Opción 2":
            self.tablero.laberinto = LaberintoMediano2()
        if laberinto == "Elaborado Opción 3":
            self.tablero.laberinto = LaberintoMediano3()
        if laberinto == "Cuatro Esquinas":
            self.tablero.laberinto = CuatroEsquinas()

        self.tablero.gridSize = self.tablero.laberinto.gridSize
        self.tablero.ancho = self.tablero.laberinto.ancho
        self.tablero.alto = self.tablero.laberinto.alto

        
        self.tablero.crearGrid()
        self.tablero.dibujarParedes()
        if laberinto == "Cuatro Esquinas":
            self.tablero.colocarObjetivos()
        else:
            self.tablero.colocarObjetivo()
        self.tablero.colocarAgente()
        self.tablero.canvas.update()
        self.tablero.canvas.update_idletasks()

    def selAlgoritmo(self, event):
        algoritmo = event.widget.get()
        if algoritmo == "Manual":
            self.controlManual()

    def ejecutarBusqueda(self):
        laberinto = self.cLaberinto.get()
        algoritmo = self.cAlgoritmo.get()
        if laberinto == "" or algoritmo == "":
            self.mensaje("Seleccione el laberinto y el algoritmo a ejecutar")
            return
        if algoritmo == "Manual":
            self.controlManual()
            return
        
        if algoritmo == "Búsqueda en Profundidad":
            self.enProfundidad(self.tablero.laberinto)
        
        if algoritmo == "Búsqueda en Anchura":
            self.enAnchura(self.tablero.laberinto)
        
        if algoritmo == "Búsqueda A*":
            self.aStar(self.tablero.laberinto)
    
    def mensaje(self, texto):
        messagebox.showinfo(
            message=texto,
            title="Alerta"
        )
    
    def newCoords(self, x,y):
        x0 = math.floor((x * self.tablero.gridSize) + self.tablero.gridSize/4)
        y0 = math.floor((y * self.tablero.gridSize) + self.tablero.gridSize/4)
        return (x0,y0)
    

    def controlManual(self):
        self.tablero.root.bind('<Left>', self.left)
        self.tablero.root.bind('<Right>', self.right)
        self.tablero.root.bind('<Up>', self.up)
        self.tablero.root.bind('<Down>', self.down)
    
    def left(self, event):
        x = self.tablero.gridSize * -1
        y = 0
        xa, ya = self.tablero.laberinto.estadoActual
        xa -= 1
        self.mover(self.tablero.idAgente, xa, ya, x, y)

    def right(self, event):
        x = self.tablero.gridSize
        y = 0
        xa, ya = self.tablero.laberinto.estadoActual
        xa += 1
        self.mover(self.tablero.idAgente, xa, ya, x, y)

    def up(self, event):
        x = 0
        y = self.tablero.gridSize * -1
        xa, ya = self.tablero.laberinto.estadoActual
        ya -= 1
        self.mover(self.tablero.idAgente, xa, ya, x, y)
    def down(self, event):
        x = 0
        y = self.tablero.gridSize
        xa, ya = self.tablero.laberinto.estadoActual
        ya += 1
        self.mover(self.tablero.idAgente, xa, ya, x, y)

    def mover(self, agente, xn, yn, x, y):
        if (xn,yn) not in self.tablero.laberinto.getParedes():
            self.tablero.laberinto.estadoActual = (xn,yn)
            self.tablero.canvas.move(agente, x, y)
            if (xn,yn) == self.tablero.laberinto.objetivo:
                self.tablero.canvas.itemconfigure(self.tablero.idObjetivo, fill="red")
                self.tablero.canvas.delete(self.tablero.idObjetivo)
                messagebox.showinfo(
                    message="¡¡¡Felicidades!!!, has encontrado el objetivo",
                    title="Completado"
                )
    

    def enProfundidad(self, laberinto):
        acciones = Busqueda().busquedaEnProfundidad(laberinto)
        for accion in acciones:
            funcion = getattr(self, accion)
            if funcion(accion) == False:
                break
            self.tablero.canvas.update()
            time.sleep(0.3)
    
    def enAnchura(self, laberinto):
        acciones = Busqueda().busquedaEnAnchura(laberinto)
        for accion in acciones:
            funcion = getattr(self, accion)
            if funcion(accion) == False:
                break
            self.tablero.canvas.update()
            time.sleep(0.5)
    
    def aStar(self, laberinto):
        acciones = Busqueda().busquedaAestrella(laberinto)
        for accion in acciones:
            funcion = getattr(self, accion)
            if funcion(accion) == False:
                break
            self.tablero.canvas.update()
            time.sleep(0.5)
    

    def Izquierda(self, accion):
        x = self.tablero.gridSize * -1
        y = 0
        xa, ya = self.tablero.laberinto.estadoActual
        xa -= 1
        return self.moverAgente(self.tablero.idAgente, xa, ya, x, y)

    def Derecha(self, accion):
        x = self.tablero.gridSize
        y = 0
        xa, ya = self.tablero.laberinto.estadoActual
        xa += 1
        return self.moverAgente(self.tablero.idAgente, xa, ya, x, y)

    def Arriba(self, accion):
        x = 0
        y = self.tablero.gridSize * -1
        xa, ya = self.tablero.laberinto.estadoActual
        ya -= 1
        return self.moverAgente(self.tablero.idAgente, xa, ya, x, y)
    def Abajo(self, accion):
        x = 0
        y = self.tablero.gridSize
        xa, ya = self.tablero.laberinto.estadoActual
        ya += 1
        return self.moverAgente(self.tablero.idAgente, xa, ya, x, y)
    

    def moverAgente(self, agente, xn, yn, x, y):
        if (xn,yn) not in self.tablero.laberinto.getParedes():
            self.tablero.laberinto.estadoActual = (xn,yn)
            self.tablero.canvas.move(agente, x, y)
            if (xn,yn) == self.tablero.laberinto.objetivo:
                self.tablero.canvas.itemconfigure(self.tablero.idObjetivo, fill="red")
                self.tablero.canvas.delete(self.tablero.idObjetivo)
                messagebox.showinfo(
                    message="¡¡¡Felicidades!!!, has encontrado el objetivo",
                    title="Completado"
                )
            return True
        else:
            util.raiseMovimientoIlegal()
            return False