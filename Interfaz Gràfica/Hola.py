from tkinter import *

Ventana = Tk()

Ventana.title("FS Anticheat")

#Ventana.geometry("800x600")

Ventana.iconbitmap("fs.ico")

#Ventana.resizable(False, False)

Panel = Frame()

Panel.pack()

Panel.pack(fill="both", expand=True)

Panel.config(bg="red")

Panel.config(width="800", height="600", bd=10, relief="sunken")


Ventana.mainloop()