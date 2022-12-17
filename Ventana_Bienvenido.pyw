import tkinter as tk
import tkinter.font as tkFont
from carrito import Carrito

class Ventana_Bienvenido:
    def __init__(self, root):
        #setting title
        root.title("Bienvenido")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GLabel_789=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_789["font"] = ft
        GLabel_789["fg"] = "#333333"
        GLabel_789["justify"] = "center"
        GLabel_789["text"] = "Bienvenidos "
        GLabel_789.place(x=210,y=120,width=180,height=80)

        GLabel_892=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_892["font"] = ft
        GLabel_892["fg"] = "#90ee90"
        GLabel_892["justify"] = "center"
        GLabel_892["text"] = "SuperMarket"
        GLabel_892.place(relx=0.22,y=40,width=350,height=57)

        GButton_319=tk.Button(root)
        GButton_319["bg"] = "#009688"
        ft = tkFont.Font(family='Times',size=13)
        GButton_319["font"] = ft
        GButton_319["fg"] = "#ffffff"
        GButton_319["justify"] = "center"
        GButton_319["text"] = "Buscar Producto"
        GButton_319["relief"] = "groove"
        GButton_319.place(x=220,rely=0.60,width=126,height=45)
        GButton_319["command"] = self.GButton_319_command

        GLabel_513=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_513["font"] = ft
        GLabel_513["fg"] = "#333333"
        GLabel_513["justify"] = "center"
        GLabel_513["text"] = "----------------------------------------------"
        GLabel_513.place(x=130,y=190,width=321,height=37)

        GLabel_58=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_58["font"] = ft
        GLabel_58["fg"] = "#333333"
        GLabel_58["justify"] = "center"
        GLabel_58["text"] = "----------------------------------------------"
        GLabel_58.place(x=170,y=110,width=236,height=31)

    def GButton_319_command(self):
        ventana_carrito=tk.Toplevel()
        app=Carrito(ventana_carrito)

if __name__ == "__main__":
    root = tk.Tk()
    ventana_bienvenido = Ventana_Bienvenido(root)
    root.mainloop()
