import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import sqlite3 
from tkinter import*
class Aplicacion(Frame):
    def __init__(self, marco):
        super().__init__(marco)
        self.marco=marco
        self.pack()
        self.crear_componentes()
        self.obtener_productos()
        self.agregar_productos()
        self.editar_productos()

  


    def obtener_productos(self):
        conexion=sqlite3.connect("basededatosdesupermercado.db")
        cursor=conexion.cursor()
        obtener=cursor.execute("SELECT * FROM Producto")
        # ob=cursor.fetchall()
        # for i in ob:
        #     print(i)
        hijos=self.tabla.get_children()

        for e in hijos:
            self.tabla.delete(e)

        for i in obtener: 
            self.tabla.insert("",0,text=i[1],values=i[2])

        conexion.close()



    def agregar_productos(self):
        conexion=sqlite3.connect("basededatosdesupermercado.db")
        cursor=conexion.cursor()

        nom=self.txtNombre.get()
        pre=self.precio.get()

        lista=[(None,nom,pre)]
        cursor.executemany("INSERT INTO Producto VALUES(?,?,?)",lista)
        conexion.commit()
        conexion.close()
        self.obtener_productos()

    
    
    
    def eliminar_productos(self):
        d=self.tabla.item(self.tabla.selection())['text']
        
        conexion = sqlite3.connect("basededatosdesupermercado.db")
        cursor = conexion.cursor()
        cursor.execute(f"DELETE FROM Producto WHERE  nombre='{d}'")
        conexion.commit()
        conexion.close()
        self.obtener_productos()


    def editar_productos(self):
        

        conexion = sqlite3.connect("basededatosdesupermercado.db")
        cursor=conexion.cursor()

        n=self.tabla.item(self.tabla.selection())["text"]
        # p=self.tabla.item(self.tabla.selection())['values'][0]
        # print(p)
        nom=self.n_nombre.get()
        pre=self.n_precio.get()
        print(pre)

        cursor.execute(f'UPDATE Producto SET nombre="{nom}",precio="{pre}" WHERE nombre="{n}"')
        conexion.commit()
        conexion.close()
        self.obtener_productos()

        
        

    
    

        
        
    def crear_componentes(self):
        GLabel_654=tk.Label()
        GLabel_654["bg"] = "#6ea8d3"
        GLabel_654["cursor"] = "spider"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_654["font"] = ft
        GLabel_654["fg"] = "#000000"
        GLabel_654["justify"] = "center"
        GLabel_654["text"] = "Nombre: "
        GLabel_654.place(x=110,y=100,width=93,height=31)

        GLabel_344=tk.Label()
        GLabel_344["bg"] = "#598ebc"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_344["font"] = ft
        GLabel_344["fg"] = "#010101"
        GLabel_344["justify"] = "center"
        GLabel_344["text"] = "Precio:"
        GLabel_344.place(x=110,y=160,width=93,height=30)

        self.txtNombre=tk.Entry()
        self.txtNombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.txtNombre["font"] = ft
        self.txtNombre["fg"] = "#333333"
        self.txtNombre["justify"] = "left"
        self.txtNombre["text"] = "nombre"
        self.txtNombre.focus()
        self.txtNombre.place(x=230,y=100,width=203,height=30)

        self.precio=tk.Entry()
        self.precio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.precio["font"] = ft
        self.precio["fg"] = "#333333"
        self.precio["justify"] = "left"
        self.precio["text"] = "precio"
        self.precio.place(x=230,y=160,width=201,height=30)

        agregar_producto=tk.Button()
        agregar_producto["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        agregar_producto["font"] = ft
        agregar_producto["fg"] = "#000000"
        agregar_producto["justify"] = "center"
        agregar_producto["text"] = "Agregar Producto"
        agregar_producto.place(x=210,y=220,width=191,height=30)
        agregar_producto["command"] = self.agregar_productos

        GLabel_464=tk.Label()
        GLabel_464["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=17)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "Añadir Producto"
        GLabel_464.place(x=180,y=40,width=263,height=30)

        # boton=tk.Button(text="hola")
        # boton.place(relx=0.12,rely=0.48)
        self.tabla=ttk.Treeview(height=12,columns=2)
        self.tabla.heading("#0",text="Nombre",anchor=CENTER)
        self.tabla.heading("#1",text="precio",anchor=CENTER )
        self.tabla.place(relx=0.20, rely=0.60)

        self.mensaje=tk.Label(text="", fg="red")
        self.mensaje.place(x=230 ,y=130)

        GButton_483=tk.Button()
        GButton_483["activebackground"] = "#d22b2b"
        GButton_483["bg"] = "#ad2323"
        GButton_483["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        GButton_483["font"] = ft
        GButton_483["fg"] = "#fcfcfc"
        GButton_483["justify"] = "center"
        GButton_483["text"] = "Eliminar"
        GButton_483.place(x=80,y=270,width=208,height=30)
        GButton_483["command"] = self.eliminar_productos

        GButton_55=tk.Button()
        GButton_55["bg"] = "#1e90ff"
        ft = tkFont.Font(family='Times',size=10)
        GButton_55["font"] = ft
        GButton_55["fg"] = "#fffefe"
        GButton_55["justify"] = "center"
        GButton_55["text"] = "Actulizar"
        GButton_55.place(relx=0.65,rely=0.30,width=220,height=30)
        GButton_55["command"] = self.editar_productos

        t_nombre=tk.Label()
        t_nombre['text']="ingrese un nuevo nombre"
        t_nombre.place(relx=0.67,rely=0.12)

        self.n_nombre=tk.Entry()
        self.n_nombre.place(relx=0.67,rely=0.15, width=180,height=20)

        t_precio=tk.Label()
        t_precio["text"]="Ingrese un nuevo precio"
        t_precio.place(relx=0.67,rely=0.20)

        self.n_precio=tk.Entry()
        self.n_precio.place(relx=0.67, rely=0.23,width=180,height=20)

    


    # def agregar_producto_command(self):
    #     nombre=self.txtNombre.get()
    #     precio=self.precio.get()
    #     self.txtNombre.delete(0,"end")
    #     self.precio.delete(0,"end")



principal=Tk()
principal.wm_title("Producto")
principal.geometry("720x640")
marco=Aplicacion(principal)
principal.mainloop()
