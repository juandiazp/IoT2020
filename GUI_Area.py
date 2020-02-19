#GUI_Area.py.
from tkinter import *
from Area import Area
from tkinter import messagebox

class AreaGUI:
    def __init__(self):
        self.window = Tk()
        self.window.geometry("400x500")
        self.c = Area()
        
        self.lbl_h = Label(self.window, text = "Valor de la altuara:")
        self.lbl_h.pack()
        v1 = DoubleVar()
        self.txt_h = Entry(self.window, textvariable=v1)
        self.txt_h.pack()

        self.lbl_b = Label(self.window, text="Valor de la base:")
        self.lbl_b.pack()
        v2 = DoubleVar()
        self.txt_b = Entry(self.window, textvariable=v2)
        self.txt_b.pack()

        

        self.btn_areatriangulo = Button(self.window, text="Area Triangulo", command=self.areatriangulo)
        self.btn_areatriangulo.pack()

        self.lbl_bme = Label(self.window, text="Valor de la base menor:")
        self.lbl_bme.pack()
        v1 = DoubleVar()
        self.txt_bme = Entry(self.window, textvariable=v1)
        self.txt_bme.pack()

        self.lbl_bma = Label(self.window, text="Valor de la base mayor:")
        self.lbl_bma.pack()
        v2 = DoubleVar()
        self.txt_bma = Entry(self.window, textvariable=v2)
        self.txt_bma.pack()

        self.lbl_ha = Label(self.window, text = "Valor de la altuara:")
        self.lbl_ha.pack()
        v3 = DoubleVar()
        self.txt_ha = Entry(self.window, textvariable=v3)
        self.txt_ha.pack()
        

        self.btn_areatrapecio = Button(self.window, text="Area Trapecio", command=self.areatrapecio)
        self.btn_areatrapecio.pack()

        self.lbl_r = Label(self.window, text = "Valor del radio:")
        self.lbl_r.pack()
        v1 = DoubleVar()
        self.txt_r = Entry(self.window, textvariable=v1)
        self.txt_r.pack()

        self.btn_areacirculo = Button(self.window, text="Area Circulo", command=self.areacirculo)
        self.btn_areacirculo.pack()
   

    def areatriangulo(self):
        self.c.h = float(self.txt_h.get())
        self.c.b = float(self.txt_b.get())
        self.c.areatriangulo()
        messagebox.showinfo(message = "El area del triangulo es: "+ str(self.c.r), title="Resultado")

    def areatrapecio(self):
        self.c.h = float(self.txt_ha.get())
        self.c.b = float(self.txt_bma.get())
        self.c.a = float(self.txt_bme.get())
        self.c.areatrapecio()
        messagebox.showinfo(message = "El area del trapecio es: "+ str(self.c.r), title="Resultado")

    def areacirculo(self):
        self.c.r = float(self.txt_r.get())
        self.c.areacirculo()
        messagebox.showinfo(message = "El area del circulo es: "+ str(self.c.a), title="Resultado")

area = AreaGUI()
