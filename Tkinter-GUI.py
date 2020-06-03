from tkinter import *
from tkinter import messagebox
import random

root = Tk()
root.title("Tarea POO")

texto = Label(root, text="Ingrese sus datos", bg="pink", fg="black", width=50)
texto.grid(row=0, column=0, columnspan=3, sticky=W+E)

etiqueta1 = Label(root, text="Título")
etiqueta1.grid(row=1, column=0)

etiqueta2 = Label(root, text="Ruta")
etiqueta2.grid(row=2, column=0)

etiqueta3 = Label(root, text="Descripsión")
etiqueta3.grid(row=3, column=0)

e1 = Entry(root)
e2 = Entry(root)
e3 = Entry(root)
e1.grid(row=1, column=1)
e2.grid(row=2, column=1)
e3.grid(row=3, column=1)
e1.config(textvariable=StringVar())
e2.config(textvariable=StringVar())
e3.config(textvariable=StringVar())

def callback():
    resultado = messagebox.askquestion("Alta", "¿Está seguro de guardar estos datos?")
    if (resultado == "yes"):
        print('Título: ' + e1.get() + '\nRuta: ' + e2.get() + '\nDescripsión: ' + e3.get())
    else:
        print("Los datos no se han guardado")
c = Button(root, text="Alta", command=callback)
c.grid(row=4, column=1)

color = ['blue', 'red', 'yellow', 'pink', 'green', 'grey', 'purple', 'violet', 'lightblue']
def changecolor():
	root.configure(bg=random.sample(color,1))
d = Button(root, text="Sorpresa", command=changecolor)
d.grid(row=4, column=2)


mainloop()