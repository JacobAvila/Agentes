import tkinter
from tkinter import *
from PIL import Image, ImageTk
import math, time
from aplicacion.laberintos import LaberintoSmall, LaberintoMediano
from aplicacion.panel import Panel

class Tablero:
    def __init__(self, laberinto):
        self.laberinto = laberinto
        self.gridSize = self.laberinto.gridSize
        self.ancho = self.laberinto.ancho
        self.alto = self.laberinto.alto
        self.idAgente = 0
        self.idObjetivo = 0
        self.IdAgente = Image
        self.iniciar()

    def iniciar(self):
        self.root = tkinter.Tk()
        self.root.title("Agente Inteligente")
        self.root.config(bg="green")
        self.root.iconbitmap("./aplicacion/images/web_hi_res_512.ico")
        self.root.geometry(str(self.ancho + 300) + "x" + str(self.alto))
        self.root.resizable(0,0)
        self.canvas = tkinter.Canvas(self.root, width=self.ancho, height=self.alto, background='black')
        self.canvas.pack(side=tkinter.LEFT)
        panel = Panel(self, self.root, self.canvas)
        self.crearFondo()
        #self.crearGrid()
        #self.dibujarParedes()
        #self.colocarObjetivo()
        #self.colocarAgente()
        self.canvas.update()
        self.root.mainloop()
        
    def crearFondo(self):
        coords = [0, 0, 0,self.alto-1, self.ancho-1, self.alto-1, self.ancho-1, 0]
        self.canvas.create_polygon(coords, outline='#000000', fill='#000000', smooth=False, width=1)
    
    def crearGrid(self):
        cantY = math.floor(self.alto/self.gridSize)
        for i in range(cantY):
            self.canvas.create_line(0,self.gridSize * i, self.ancho-1, self.gridSize * i, fill='#222222', width=0.3)
        cantX = math.floor(self.ancho/self.gridSize)
        for i in range(cantX):
            self.canvas.create_line(self.gridSize * i, 0, self.gridSize * i, self.alto-1, fill='#222222', width=0.3)
        
        self.gridDim = (cantX, cantY)
        self.grid = []
        for x in range(0, cantX):
            for y in range(0, cantY):
                self.grid.append((x,y))

    def dibujarParedes(self):
        paredes = self.laberinto.getParedes()
        for x,y in paredes:
            xi = x * self.gridSize
            xf = xi + self.gridSize - 1
            yi = y * self.gridSize
            yf = yi + self.gridSize - 1
            coord = [xi, yi, xi,yf, xf, yf, xf, yi]
            self.canvas.create_polygon(coord, outline='blue', fill='blue', smooth=False)
    
    def colocarObjetivo(self):
        objetivo = self.laberinto.objetivo
        r = 10
        x,y = objetivo
        x0 = x * self.gridSize + (self.gridSize/2 - r/2) - r + 4
        y0 = y * self.gridSize + (self.gridSize/2 - r/2) - r + 5
        x1 = x0 + self.gridSize/2
        y1 = y0 + self.gridSize/2
        self.idObjetivo = self.canvas.create_oval(x0, y0, x1, y1, outline="white", fill="white")
    
    def colocarObjetivos(self):
        objetivos = self.laberinto.objetivo
        for objetivo in objetivos:
            r = 10
            x,y = objetivo
            x0 = x * self.gridSize + (self.gridSize/2 - r/2) - r + 4
            y0 = y * self.gridSize + (self.gridSize/2 - r/2) - r + 5
            x1 = x0 + self.gridSize/2
            y1 = y0 + self.gridSize/2
            self.idObjetivo = self.canvas.create_oval(x0, y0, x1, y1, outline="white", fill="white")
    
    def colocarAgente(self):
        x,y = self.laberinto.estadoInicial
        x0 = math.floor((x * self.gridSize) + self.gridSize/4)
        y0 = math.floor((y * self.gridSize) + self.gridSize/4)
        image = Image.open('./aplicacion/images/src_images_robot.png')
        ancho= image.width
        alto = image.height
        w = math.floor(((self.gridSize/2)/ancho)*ancho)
        h = math.floor(((self.gridSize/2)/ancho)*alto)
        imagen = image.resize((w,h))
        img = ImageTk.PhotoImage(imagen)
        self.idAgente = self.canvas.create_image(x0,y0, image=img, anchor="nw", state=tkinter.NORMAL)
        self.root.update()
        self.canvas.move(self.idAgente, 0, 0)
        #print("id ", self.idAgente)
        self.IdAgente.image = img
        #self.agente = tkinter.Label(self.canvas, image=img, bg="black", width=w, height=h)
        #self.agente.pack()
        #self.agente.place(x=x0, y=y0)


