import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.componentes()
        
        
    def activar(self):
        mostrar=self.tabla.item(self.tabla.selection())["values"][3]
        print(mostrar)
        

            






    def componentes(self):
        self.tabla=ttk.Treeview(height=12,columns=("nombre","marca","precio","cantidad"))
        self.tabla.column("#0",width=30)
        self.tabla.column("nombre",width=90)
        self.tabla.column("marca",width=80)
        self.tabla.column("precio",width=40)
        self.tabla.column("cantidad",width=30)

        self.tabla.heading("#0",text="id")
        self.tabla.heading("nombre",text="nombre")
        self.tabla.heading("marca",text="marca")
        self.tabla.heading("precio",text="precio")
        self.tabla.heading("cantidad",text="cantidad")

        self.tabla.insert("","end",text="1",values=("caramelo","arcor","144","90"))
        self.tabla.insert("","end",text="2",values=("dulce de leche","ilolay","290","50"))
        self.tabla.insert("","end",text="3",values=("chocolate","milkaut","280","112"))

        self.tabla.pack()

        self.crear_boton=tk.Button()
        self.crear_boton["command"]=self.activar
        self.crear_boton.pack()

        
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
