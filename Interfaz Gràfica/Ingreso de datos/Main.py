from tkinter import *
from tkinter import messagebox

Ventana = Tk()

Ventana.title("Ingreso de datos")

def cerrarVentana():
	if messagebox.askyesno("Salir", "¿Deseas salir de la aplicación?"):
		Ventana.destroy()

def mostrarInformacion(Evento):
	messagebox.showinfo(message="Has apretado la tecla F1", title="Información")

Ventana.protocol("WM_DELETE_WINDOW", cerrarVentana)
Ventana.bind("<F1>", mostrarInformacion)

Ventana.mainloop()
