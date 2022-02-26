from tkinter import *
import random

def moverBoton(e):
    w = ventana.winfo_width()
    h = ventana.winfo_height()
    print(h)

    botonW = boton.winfo_width()
    botonH = boton.winfo_height()
   
    moverX = random.randrange(0, w - botonW)
    moverY = random.randrange(0, h - botonH)
    
    boton.place(x=moverX, y=moverY)
    
ventana = Tk()
ventana.title("Click Me")
ventana.configure(bg="#E83FCF", cursor="hand2")
ventana.geometry("400x695+950+0")
ventana.resizable(False, False)

boton = Button(ventana, text="CLICK ME", font="arial 13", fg="#E83FCF",
width=20, height=3, bd=0, bg="#27E8DB", command=ventana.quit)
boton.place(x=100, y=300)

boton.bind("<Enter>", moverBoton)

ventana.mainloop()



