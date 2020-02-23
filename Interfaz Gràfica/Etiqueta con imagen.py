from tkinter import *

from tkinter import messagebox

Ventana = Tk()

Ventana.title("Etiqueta personalizada")

Etiqueta = Label(Ventana, text="¡Hola Mundo!")

Imagen = PhotoImage(file = "jack.png")


def clickearImagen(Evento):
	messagebox.showinfo("Hola", "Hiciste clic a la imagen")

Etiqueta.config(image = Imagen) 

Etiqueta.pack(fill = Y, expand = 1)

Etiqueta.bind("<Button-1>", clickearImagen)

Ventana.mainloop()