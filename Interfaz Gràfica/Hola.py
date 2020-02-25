from tkinter import *

Ventana = Tk()

Ventana.title("FS Anticheat")

Ventana.geometry("1000x600")

Ventana.iconbitmap("fs.ico")

Ventana.resizable(True, True)

Panel = Frame()

Panel.pack()

Panel.pack( expand=False)

Panel.config(bg="blue")

Panel.config(width="100", height="200", bd=1000, relief="groove")


Ventana.mainloop()