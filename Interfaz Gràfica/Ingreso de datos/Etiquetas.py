from tkinter import *

Ventana = Tk()

Ventana.title("Etiqueta personalizada")

Etiqueta = Label(Ventana, text="¡Hola Mundo!")

Etiqueta.config(fg="blue",  # Foreground
             	bg="red",   # Background
             	font=("Arial",24)) 

Etiqueta.pack()

Ventana.mainloop()