import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import sqlite3
from  PIL import Image,ImageTk
from tkinter import messagebox


class Carrito:
    def __init__(self, root):
        #setting title
        root.title("Tienda")
        #setting window size
        width=1000
        height=600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        self.contador=0
            # Crea una imagen a partir de un archivo
        root.imagen = Image.open("2022.png")
        root.imagen=root.imagen.resize((1000,600),Image.ANTIALIAS)

        
        # Crea una imagen que pueda ser mostrada en un widget de tkinter
        root.imagen_tk = ImageTk.PhotoImage(root.imagen)

        # Crea un widget Label y lo configura para mostrar la imagen
        label_imagen = tk.Label(root)
        label_imagen.configure(image=root.imagen_tk)
        label_imagen.place(relx=0,rely=0)

        boton_buscar=tk.Button(root)
        boton_buscar["bg"] = "#43bb43"
        ft = tkFont.Font(family='Times',size=10)
        boton_buscar["font"] = ft
        boton_buscar["fg"] = "#fcfdfe"
        boton_buscar["justify"] = "center"
        boton_buscar["text"] = "buscar 🔎"
        boton_buscar.place(x=390,rely=0.05,width=70,height=41)
        boton_buscar["command"] = self.boton_buscar_command

        self.buscar_producto_entry=tk.Entry(root)
        self.buscar_producto_entry["bg"] = "#f9f9f9"
        self.buscar_producto_entry["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.buscar_producto_entry["font"] = ft
        self.buscar_producto_entry["fg"] = "#999999"
        self.buscar_producto_entry["justify"] = "left"
        self.buscar_producto_entry["text"] = "PRODUCTO"
        self.buscar_producto_entry.place(relx=0.10,rely=0.05,width=289,height=40)

        boton_agregar=tk.Button(root)
        boton_agregar["bg"] = "#95e895"
        ft = tkFont.Font(family='Times',size=10)
        boton_agregar["font"] = ft
        boton_agregar["fg"] = "#000000"
        boton_agregar["justify"] = "center"
        boton_agregar["text"] = "AGREGAR"
        boton_agregar.place(relx=.80,rely=.25,width=170,height=35)
        boton_agregar["command"] = self.boton_agregar_command

        GLabel_355=tk.Label(root)
        GLabel_355["bg"] = "#95a495"
        ft = tkFont.Font(family='Times',size=12)
        GLabel_355["font"] = ft
        GLabel_355["fg"] = "#ffffff"
        GLabel_355["justify"] = "center"
        GLabel_355["text"] = "TOTAL DE LA COMPRA"
        GLabel_355.place(relx=0.05,rely=.90,width=169,height=37)

        self.billetitos=tk.Entry(root)
        self.billetitos["bg"] = "#999999"
        self.billetitos["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.billetitos["font"] = ft
        self.billetitos["fg"] = "#ffffff"
        self.billetitos["justify"] = "left"
        self.billetitos["text"] = "$400"
        self.billetitos.place(relx=0.22,rely=.90,width=320,height=39)
        

        # self.label_cantidad=tk.Label()
        # ft = tkFont.Font(family='Times',size=10)
        # self.label_cantidad["font"] = ft
        # self.label_cantidad["fg"] = "#333333"
        # self.label_cantidad["justify"] = ""
        # self.label_cantidad["text"] = ""
        # self.label_cantidad.place(x=680,y=180,width=98,height=28)

        boton_disminuir=tk.Button(root)
        boton_disminuir["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        boton_disminuir["font"] = ft
        boton_disminuir["fg"] = "white"
        boton_disminuir["bg"] = "red"
        boton_disminuir["justify"] = "center"
        boton_disminuir["text"] = "➖"
        boton_disminuir.place(relx=.80,rely=.35,width=70,height=30)
        boton_disminuir["command"] = self.boton_disminuir_command

        incrementar_cantidad=tk.Button(root)
        incrementar_cantidad["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=15)
        incrementar_cantidad["font"] = ft
        incrementar_cantidad["fg"] = "white"
        incrementar_cantidad["bg"] = "green"
        incrementar_cantidad["justify"] = "center"
        incrementar_cantidad["text"] = "➕"
        incrementar_cantidad.place(relx=0.90,rely=.35,width=70,height=30)
        incrementar_cantidad["command"] = self.incrementar_cantidad_command

        boton_subtotal=tk.Button(root)
        boton_subtotal["bg"] = "yellow"
        ft = tkFont.Font(family='Times',size=15)
        boton_subtotal["font"] = ft
        boton_subtotal["fg"] = "#000000"
        boton_subtotal["justify"] = "center"
        boton_subtotal["text"] = "Sub Total 💲"
        boton_subtotal.place(relx=0.39,rely=0.91,width=150,height=31)
        boton_subtotal["command"] = self.boton_subtotal_command

        boton_pagar=tk.Button(root)
        boton_pagar["bg"] = "green"
        ft = tkFont.Font(family='Times',size=15)
        boton_pagar["font"] = ft
        boton_pagar["fg"] = "#000000"
        boton_pagar["justify"] = "center"
        boton_pagar["text"] = "Pagar 💵"
        boton_pagar.place(relx=0.55,rely=0.91,width=150,height=31)
        boton_pagar["command"] = self.boton_pagar_command

        # label_imagen = tk.Label(root)
        # label_imagen.configure(image=root.imagen_tk)
        # label_imagen.place(relx=0,rely=0)

        boton_eliminar=tk.Button(root)
        boton_eliminar["bg"] = "red"
        ft = tkFont.Font(family='Times',size=20)
        boton_eliminar["font"] = ft
        boton_eliminar["fg"] = "#ffffff"
        boton_eliminar["justify"] = "center"
        boton_eliminar["text"] = "🗑"
        boton_eliminar.place(relx=.55,rely=.60,width=100,height=50)
        boton_eliminar["command"] = self.boton_eliminar_command

        GLabel_803=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_803["font"] = ft
        GLabel_803["fg"] = "#333333"
        GLabel_803["bg"] = "#bbbbbb"
        GLabel_803["justify"] = "center"
        GLabel_803["text"] = "Cantidad de productos"
        GLabel_803.place(x=600,y=70,width=136,height=30)

        self.label_contador_producto=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        self.label_contador_producto["font"] = ft
        self.label_contador_producto["fg"] = "#333333"
        self.label_contador_producto["justify"] = "center"
        self.label_contador_producto["text"] = ""
        self.label_contador_producto.place(x=740,y=70,width=150,height=27)
        
        GLabel_767=tk.Label(root)
        GLabel_767["bg"] = "#bbbbbb"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_767["font"] = ft
        GLabel_767["fg"] = "#333333"
        GLabel_767["justify"] = "center"
        GLabel_767["text"] = "Carrito"
        GLabel_767.place(relx=0.20,rely=0.50,width=228,height=37)

        GLabel_768=tk.Label(root)
        GLabel_768["bg"] = "#bbbbbb"
        ft = tkFont.Font(family='Times',size=13)
        GLabel_768["font"] = ft
        GLabel_768["fg"] = "#333333"
        GLabel_768["justify"] = "center"
        GLabel_768["text"] = "Catalogo de Productos"
        GLabel_768.place(relx=0.15,rely=0.13,width=228,height=37)

        GLabel_847=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_847["font"] = ft
        GLabel_847["fg"] = "#d33d3d"
        GLabel_847["justify"] = "center"
        GLabel_847["text"] = "ingresar el nombre del producto"
        GLabel_847.place(x=80,y=0,width=251,height=30)


        self.tabla=ttk.Treeview(root,height=6,columns=("marca","descripcion","precio","cantidad"))

        self.tabla.column("#0",width=80)
        self.tabla.column("marca",width=80)
        self.tabla.column("descripcion",width=80)
        self.tabla.column("precio",width=80)
        self.tabla.column("cantidad", width=89)
        
        self.tabla.heading("#0", text="nombre")
        self.tabla.heading("marca",text="marca")
        self.tabla.heading("descripcion",text="descripcion")
        self.tabla.heading("precio",text="precio")
        self.tabla.heading("cantidad",text="stock")


        

        # carritos=self.tabla.insert("","end",text="NOMBRE DE PRODUCTOS")
        # self.tabla.insert(carritos,"end",text="gaseosa")
        # self.tabla.insert(carritos,"end",text="leche" )
        # self.tabla.insert(carritos,"end",text="chocolate" )
        # usuario=self.tabla.insert("","end",text="NOMBRE DE USUARIOS")
        # self.tabla.insert(usuario,"end",text="naomi")
        # print(self.tabla.item(carritos))

        
        self.tabla.place(relx=0.05,rely=0.20)


        self.ticket=ttk.Treeview(root,columns=("marca","cantidad","pagar"),height=8)
        self.ticket.heading("#0",text="productos")
        self.ticket.heading("#1",text="marca")
        self.ticket.heading("#2",text="cantidad")
        self.ticket.heading("#3",text="pagar")

        self.ticket.column("#0",width=80)
        self.ticket.column("marca",width=80)
        self.ticket.column("cantidad",width=80)
        self.ticket.column("pagar",width=80)
        

        self.ticket.place(relx=0.05,rely=0.60,width=490)

        
    

        
    

    def boton_buscar_command(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()
        buscar=self.buscar_producto_entry.get()
        consulta=cursor.execute(f"SELECT * FROM tienda WHERE  nombre LIKE  '{buscar}%' or marca LIKE '{buscar}%'")
        # s=cursor.fetchall()
        # for i in s:
        #     print(i)
        hijos=self.tabla.get_children()
        for h in hijos:
            self.tabla.delete(h)

        for i in consulta:
            self.tabla.insert("",0,text=i[1] ,values=(i[2],i[3],i[4],i[5]))

        conexion.commit()
        conexion.close()

    def incrementar_cantidad_command(self):
        self.cantidadproducto=self.cantidadproducto+1
        self.total=self.precio_incial*self.cantidadproducto

        limpiar=self.ticket.delete(self.t)
        self.t=self.ticket.insert("","end",text=self.clave, values=(self.marca,self.cantidadproducto,self.total))

    
    def boton_disminuir_command(self):
        self.cantidadproducto=self.cantidadproducto-1

        self.total_disminuir=self.precio_incial * self.cantidadproducto
        limpieza=self.ticket.delete(self.t)

        self.t=self.ticket.insert("","end",text=self.clave, values=(self.marca,self.cantidadproducto,self.total_disminuir))

    def boton_eliminar_command(self):
        limpiar=self.ticket.delete(self.ticket.selection())
        self.contador=self.contador-1
        self.label_contador_producto["text"]=self.contador

        
    

    def boton_agregar_command(self):
        if self.tabla.selection():
            self.contador=self.contador+1
            self.label_contador_producto["text"]=self.contador
            self.clave=self.tabla.item(self.tabla.selection())["text"]
            self.valores=self.tabla.item(self.tabla.selection())["values"]


            # print(self.clave)
            self.marca=self.valores[0]
            self.precio_incial=float(self.valores[2])
            
        
    
            self.cantidadproducto=1

            self.t=self.ticket.insert("","end",text=self.clave, values=(self.marca,self.cantidadproducto,self.precio_incial))
    
        else:
            self.label_contador_producto["text"]="selecciona un producto"


    
    def boton_subtotal_command(self):
        self.billetitos.delete(0,"end")

        suma=0
        for i in self.ticket.get_children():
            celda=float(self.ticket.set(i,"pagar"))
            suma=suma+celda

        entrada=self.billetitos.insert(0,suma)

        
    def boton_pagar_command(self):
        messagebox.showinfo(message="su compra fue realizada",title="compra exitosa")

        

    

if __name__ == "__main__":
    root = tk.Tk()
    carrito = Carrito(root)
    root.mainloop()
