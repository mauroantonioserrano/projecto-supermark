import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from carrito import Carrito
from PIL import Image,ImageTk

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
          # Crea una imagen a partir de un archivo
        self.imagen = Image.open("istockphoto-1275827044-612x612 - Editada.png")
        self.imagen=self.imagen.resize((1300,700),Image.ANTIALIAS)

        
        # Crea una imagen que pueda ser mostrada en un widget de tkinter
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)
        

       




        
        
        label_imagen = tk.Label()
        label_imagen.configure(image=self.imagen_tk)
        label_imagen.place(relx=0,rely=0)

        GLabel_789=tk.Label(root)
        ft = tkFont.Font(family='Times',size=28)
        GLabel_789["font"] = ft
        GLabel_789["fg"] = "black"
        GLabel_789["bg"]="#78ccee"
        GLabel_789["justify"] = "center"
        GLabel_789["text"] = "Bienvenidos "
        GLabel_789.place(x=210,y=120,width=180,height=50)

        GLabel_892=tk.Label(root)
        ft = tkFont.Font(family='Times',size=38)
        GLabel_892["font"] = ft
        GLabel_892["fg"] = "black"
        GLabel_892["bg"]="#67ff41"
        GLabel_892["justify"] = "center"
        GLabel_892["text"] = "SuperMarket"
        GLabel_892.place(relx=0.26,y=40,width=300,height=48)

        GButton_319=tk.Button(root)
        GButton_319["bg"] = "#009688"
        ft = tkFont.Font(family='Times',size=13)
        GButton_319["font"] = ft
        GButton_319["fg"] = "black"
        GButton_319["justify"] = "center"
        GButton_319["text"] = "Buscar Producto"
        GButton_319["relief"] = "groove"
        GButton_319.place(x=220,rely=0.60,width=126,height=45)
        GButton_319["command"] = self.GButton_319_command

       

    def GButton_319_command(self):
        ventana_carrito=tk.Toplevel()
        app=Carrito(ventana_carrito)

if __name__ == "__main__":
    root = tk.Tk()
    ventana_bienvenido = Ventana_Bienvenido(root)
    root.mainloop()
