import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_850=tk.Button(root)
        GButton_850["bg"] = "#43bb43"
        ft = tkFont.Font(family='Times',size=10)
        GButton_850["font"] = ft
        GButton_850["fg"] = "#fcfdfe"
        GButton_850["justify"] = "center"
        GButton_850["text"] = "buscar"
        GButton_850.place(x=390,rely=0.05,width=65,height=41)
        GButton_850["command"] = self.GButton_850_command

        GLineEdit_867=tk.Entry(root)
        GLineEdit_867["bg"] = "#f9f9f9"
        GLineEdit_867["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_867["font"] = ft
        GLineEdit_867["fg"] = "#999999"
        GLineEdit_867["justify"] = "left"
        GLineEdit_867["text"] = "PRODUCTO"
        GLineEdit_867.place(relx=0.10,rely=0.05,width=289,height=40)

        GButton_314=tk.Button(root)
        GButton_314["bg"] = "#95e895"
        ft = tkFont.Font(family='Times',size=10)
        GButton_314["font"] = ft
        GButton_314["fg"] = "#000000"
        GButton_314["justify"] = "center"
        GButton_314["text"] = "AGREGAR"
        GButton_314.place(x=650,y=120,width=114,height=35)
        GButton_314["command"] = self.GButton_314_command

        GLabel_355=tk.Label(root)
        GLabel_355["bg"] = "#95a495"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_355["font"] = ft
        GLabel_355["fg"] = "#ffffff"
        GLabel_355["justify"] = "center"
        GLabel_355["text"] = "TOTAL DE LA COMPRA"
        GLabel_355.place(relx=0.05,rely=.90,width=169,height=37)

        GLineEdit_287=tk.Entry(root)
        GLineEdit_287["bg"] = "#999999"
        GLineEdit_287["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_287["font"] = ft
        GLineEdit_287["fg"] = "#ffffff"
        GLineEdit_287["justify"] = "left"
        GLineEdit_287["text"] = "$400"
        GLineEdit_287.place(relx=0.22,rely=.90,width=320,height=39)

        GLabel_535=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_535["font"] = ft
        GLabel_535["fg"] = "#333333"
        GLabel_535["justify"] = "center"
        GLabel_535["text"] = "10"
        GLabel_535.place(x=680,y=180,width=70,height=25)

        GButton_593=tk.Button(root)
        GButton_593["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_593["font"] = ft
        GButton_593["fg"] = "#000000"
        GButton_593["justify"] = "center"
        GButton_593["text"] = "-"
        GButton_593.place(x=620,y=180,width=70,height=25)
        GButton_593["command"] = self.GButton_593_command

        GButton_457=tk.Button(root)
        GButton_457["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_457["font"] = ft
        GButton_457["fg"] = "#000000"
        GButton_457["justify"] = "center"
        GButton_457["text"] = "+"
        GButton_457.place(x=740,y=180,width=70,height=25)
        GButton_457["command"] = self.GButton_457_command

        GButton_265=tk.Button(root)
        GButton_265["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_265["font"] = ft
        GButton_265["fg"] = "#000000"
        GButton_265["justify"] = "center"
        GButton_265["text"] = "Confirmar"
        GButton_265.place(x=620,y=230,width=197,height=30)
        GButton_265["command"] = self.GButton_265_command

        GButton_53=tk.Button(root)
        GButton_53["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_53["font"] = ft
        GButton_53["fg"] = "#000000"
        GButton_53["justify"] = "center"
        GButton_53["text"] = "Eliminar Producto"
        GButton_53.place(x=650,y=290,width=115,height=30)
        GButton_53["command"] = self.GButton_53_command

        GLabel_803=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_803["font"] = ft
        GLabel_803["fg"] = "#333333"
        GLabel_803["justify"] = "center"
        GLabel_803["text"] = "Cantidad de productos"
        GLabel_803.place(x=600,y=70,width=136,height=30)

        GLabel_594=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_594["font"] = ft
        GLabel_594["fg"] = "#333333"
        GLabel_594["justify"] = "center"
        GLabel_594["text"] = "1"
        GLabel_594.place(x=740,y=70,width=70,height=25)
        
        GLabel_767=tk.Label(root)
        GLabel_767["bg"] = "#bbbbbb"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_767["font"] = ft
        GLabel_767["fg"] = "#333333"
        GLabel_767["justify"] = "center"
        GLabel_767["text"] = "mi ticket"
        GLabel_767.place(relx=0.20,rely=0.50,width=228,height=37)

        GLabel_847=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_847["font"] = ft
        GLabel_847["fg"] = "#d33d3d"
        GLabel_847["justify"] = "center"
        GLabel_847["text"] = "ingresar el nombre del producto"
        GLabel_847.place(x=80,y=0,width=251,height=30)


        tabla=ttk.Treeview(root,columns=("marca","nombre del producto","peso","precio"),height=5)

        tabla.column("#0",width=80)
        tabla.column("nombre del producto",width=80)
        tabla.column("peso",width=80)
        tabla.column("precio",width=80)
        

        tabla.heading("#0",text="marca")
        tabla.heading("#1",text="nombre del producto")
        tabla.heading("#2",text="peso")
        tabla.heading("#3",text="precio")

        tabla.insert("","end",text="coca cola",values=("gaseosa ","2.25 lts","315"))

        

        # carritos=tabla.insert("","end",text="NOMBRE DE PRODUCTOS")
        # tabla.insert(carritos,"end",text="gaseosa")
        # tabla.insert(carritos,"end",text="leche" )
        # tabla.insert(carritos,"end",text="chocolate" )
        # usuario=tabla.insert("","end",text="NOMBRE DE USUARIOS")
        # tabla.insert(usuario,"end",text="naomi")
        # print(tabla.item(carritos))

        
        tabla.place(relx=0.05,rely=0.20,width=440)


        marco=ttk.Treeview(root,columns=("productos","marca","cantidad","pagar"),height=8)
        marco.heading("#0",text="productos")
        marco.heading("#1",text="marca")
        marco.heading("#2",text="cantidad")
        marco.heading("#3",text="pagar")

        marco.column("#0",width=80)
        marco.column("marca",width=80)
        marco.column("cantidad",width=80)
        marco.column("pagar",width=80)
        

        marco.place(relx=0.05,rely=0.60,width=490)

    def GButton_850_command(self):
        print("command")


    def GButton_314_command(self):
        print("command")


    def GButton_593_command(self):
        print("command")


    def GButton_457_command(self):
        print("command")


    def GButton_265_command(self):
        print("command")


    def GButton_53_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
