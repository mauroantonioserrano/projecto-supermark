import tkinter as tk
import tkinter.font as tkFont
from tkinter import ttk
import sqlite3 
from tkinter import *
from PIL import Image, ImageTk
class Aplicacion(Frame):
    def __init__(self, marco):
        super().__init__(marco)
        self.marco=marco
        self.pack()
         # Crea una imagen a partir de un archivo
        self.imagen = Image.open("tecnologia.jpg")
        self.imagen=self.imagen.resize((1300,700),Image.ANTIALIAS)

        
        # Crea una imagen que pueda ser mostrada en un widget de tkinter
        self.imagen_tk = ImageTk.PhotoImage(self.imagen)

    
        self.crear_componentes()
        self.obtener_productos()
        self.base_de_datos()




        

    def base_de_datos(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS tienda(id INTEGER NOT NULL,nombre TEXT NOT NULL,marca TEXT,descripcion TEXT,precio REAL NOT NULL,cantidad INTEGER NOT NULL,PRIMARY KEY(id AUTOINCREMENT) )")
        conexion.commit()
        conexion.close()


    def obtener_productos(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()
        cur=cursor.execute("SELECT * FROM tienda")
        # a=cursor.fetchall()
        # for i in a:
        #    print(i)
        hijos=self.tabla.get_children()
        for h in hijos:
            self.tabla.delete(h)

        for i in cur:
            self.tabla.insert("","end",text=i[0] ,values=(i[1],i[2],i[3],i[4],i[5]))
        
        conexion.close()
   

    def agregar_productos(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()

        id=self.id.get()
        print(id)

        nombre=self.nombre.get()
        print(nombre)

        marca=self.marca.get()
        print(marca)

        descripcion=self.descripcion.get()
        print(descripcion)

        precio=self.precio.get()
        print(precio)
        cantidad=self.cantidad.get()
        print(cantidad)

        lista=[(id,nombre,marca,descripcion,precio,cantidad)]

        cursor.executemany("INSERT INTO tienda VALUES(?,?,?,?,?,?)",lista)
        conexion.commit()
        conexion.close()

        self.obtener_productos()
        


        # conexion=sqlite3.connect("basededatosdesupermercado.db")
        # cursor=conexion.cursor()

        # nom=self.txtNombre.get()
        # pre=self.precio.get()

        # lista=[(None,nom,pre)]
        # cursor.executemany("INSERT INTO Producto VALUES(?,?,?)",lista)
        # conexion.commit()
        # conexion.close()
        # self.obtener_productos()
        

    
    
    
    def eliminar_productos(self):

        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()    
        id=self.tabla.item(self.tabla.selection())["text"]
        cursor.execute(f"DELETE FROM tienda WHERE id=={id}")
        conexion.commit()
        conexion.close()
        self.obtener_productos()
        # d=self.tabla.item(self.tabla.selection())['text']
        
        # conexion = sqlite3.connect("basededatosdesupermercado.db")
        # cursor = conexion.cursor()
        # cursor.execute(f"DELETE FROM Producto WHERE  nombre='{d}'")
        # conexion.commit()
        # conexion.close()
        # self.obtener_productos()

    
        


    def editar_productos(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()

        nombre=self.nombre.get()
        print(nombre)

        marca=self.marca.get()
        descripcion=self.descripcion.get()
        precio=self.precio.get()
        cantidad=self.cantidad.get()

        id=self.tabla.item(self.tabla.selection())["text"]
        print(id)


        cursor.execute(f"UPDATE tienda SET nombre='{nombre}', marca='{marca}',descripcion='{descripcion}',precio='{precio}', cantidad='{cantidad}' WHERE id='{id}' ")
        conexion.commit()
        conexion.close()
        self.obtener_productos()



        # n=self.tabla.item(self.tabla.selection())['text']
        # v=self.tabla.item(self.tabla.selection())['values']
        # print(n)
        # print(v)
        # conexion = sqlite3.connect("basededatosdesupermercado.db")
        # cursor=conexion.cursor()

        
      
    def auto_llenar(self):
        id=self.tabla.item(self.tabla.selection())["text"]
        
        obtenercolumnas=self.tabla.item(self.tabla.selection())["values"]
        nombre=obtenercolumnas[0]
        marca=obtenercolumnas[1]
        descripcion=obtenercolumnas[2]
        precio=obtenercolumnas[3]
        cantidad=obtenercolumnas[4]


        


        i=self.id.delete(0,"end")
        i=self.id.insert(0,id)

        n=self.nombre.delete(0,"end")
        n=self.nombre.insert(0,nombre)

        m=self.marca.delete(0,"end")
        m=self.marca.insert(0,marca)

        d=self.descripcion.delete(0,"end")
        d=self.descripcion.insert(0,descripcion)
      
        p=self.precio.delete(0,"end")
        p=self.precio.insert(0,precio)

        c=self.cantidad.delete(0,"end")
        c=self.cantidad.insert(0,cantidad)


    

        

        
    
        # # print(p)
        # nom=self.n_nombre.get()
        # pre=self.n_precio.get()
        # print(pre)

        # cursor.execute(f'UPDATE Producto SET nombre="{nom}",precio="{pre}" WHERE nombre="{n}"')
        # conexion.commit()
        # conexion.close()
        # self.obtener_productos()


        
        

    
    

        
        
    def crear_componentes(self):    
        # Crea un widget Label y lo configura para mostrar la imagen
        label_imagen = tk.Label()
        label_imagen.configure(image=self.imagen_tk)
        label_imagen.place(relx=0,rely=0)

        GLabel_464=tk.Label()
        GLabel_464["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=17)
        GLabel_464["font"] = ft
        GLabel_464["fg"] = "#333333"
        GLabel_464["justify"] = "center"
        GLabel_464["text"] = "A D M I N I S T R A D O R"
        GLabel_464.place(relx=0.37,rely=0.05,width=263,height=30)

        GLabel_720=tk.Label()
        GLabel_720["bg"] = "#75afda"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_720["font"] = ft
        GLabel_720["fg"] = "#333333"
        GLabel_720["justify"] = "center"
        GLabel_720["text"] = "•marca• :"
        GLabel_720.place(x=400,y=70,width=78,height=30)

        GLabel_380=tk.Label()
        GLabel_380["bg"] = "#75afda"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_380["font"] = ft
        GLabel_380["fg"] = "#333333"
        GLabel_380["justify"] = "center"
        GLabel_380["text"] = "•Precio• :"
        GLabel_380.place(x=590,y=70,width=82,height=30)

        GLabel_492=tk.Label()
        GLabel_492["bg"] = "#75afda"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_492["font"] = ft
        GLabel_492["fg"] = "#333333"
        GLabel_492["justify"] = "center"
        GLabel_492["text"] = "•descripcion• :"
        GLabel_492.place(x=400,y=110,width=82,height=30)

        GLabel_994=tk.Label()
        GLabel_994["bg"] = "#75afda"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_994["font"] = ft
        GLabel_994["fg"] = "#333333"
        GLabel_994["justify"] = "center"
        GLabel_994["text"] = "•cantidad• :"
        GLabel_994.place(x=590,y=110,width=80,height=30)

        GLabel_866=tk.Label()
        GLabel_866["bg"] = "#75afda"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_866["font"] = ft
        GLabel_866["fg"] = "#333333"
        GLabel_866["justify"] = "center"
        GLabel_866["text"] = "•Id• :"
        GLabel_866.place(x=210,y=70,width=77,height=30)

        GLabel_841=tk.Label()
        GLabel_841["bg"] = "#75afda"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_841["font"] = ft
        GLabel_841["fg"] = "#333333"
        GLabel_841["justify"] = "center"
        GLabel_841["text"] = "•Nombre• :"
        GLabel_841.place(x=210,y=110,width=76,height=30)

        self.id=tk.Entry()
        self.id["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.id["font"] = ft
        self.id["fg"] = "#333333"
        self.id["justify"] = "left"
        self.id["text"] = "id"
        self.id.place(x=300,y=70,width=89,height=30)

        self.marca=tk.Entry()
        self.marca["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.marca["font"] = ft
        self.marca["fg"] = "#333333"
        self.marca["justify"] = "left"
        self.marca["text"] = "marca"
        self.marca.place(x=490,y=70,width=88,height=30)

        self.descripcion=tk.Entry()
        self.descripcion["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.descripcion["font"] = ft
        self.descripcion["fg"] = "#333333"
        self.descripcion["justify"] = "left"
        self.descripcion["text"] = "descripcion"
        self.descripcion.place(x=490,y=110,width=88,height=30)

        self.precio=tk.Entry()
        self.precio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.precio["font"] = ft
        self.precio["fg"] = "#333333"
        self.precio["justify"] = "left"
        self.precio["text"] = "precio"
        self.precio.place(x=690,y=70,width=89,height=30)

        self.cantidad=tk.Entry()
        self.cantidad["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.cantidad["font"] = ft
        self.cantidad["fg"] = "#333333"
        self.cantidad["justify"] = "left"
        self.cantidad["text"] = "cantidad"
        self.cantidad.place(x=690,y=110,width=91,height=30)

        self.nombre=tk.Entry()
        self.nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        self.nombre["font"] = ft
        self.nombre["fg"] = "#333333"
        self.nombre["justify"] = "left"
        self.nombre["text"] = "nombre"
        self.nombre.place(x=300,y=110,width=89,height=30)



        # boton=tk.Button(text="hola")
        # boton.place(relx=0.12,rely=0.48)
        self.tabla=ttk.Treeview(height=12,columns=("nombre","marca","descripcion","precio","cantidad"))

        self.tabla.column("#0",width=60)
        self.tabla.column("nombre",width=150)
        self.tabla.column("marca",width=120)
        self.tabla.column("descripcion",width=180)
        self.tabla.column("precio",width=60)
        self.tabla.column("cantidad",width=70)



        self.tabla.heading("#0",text="id",anchor=CENTER)
        self.tabla.heading("nombre",text="nombre",anchor=CENTER)
        self.tabla.heading("marca",text="marca",anchor=CENTER)
        self.tabla.heading("descripcion",text="descripcion",anchor=CENTER)
        self.tabla.heading("precio",text="precio",anchor=CENTER)
        self.tabla.heading("cantidad",text="cantidad",anchor=CENTER)

        self.tabla.insert("","end",text=1,values=("chocolate","cofler block","chocolate de 90 gr",120,333))
        self.tabla.place(relx=0.06, rely=0.50,relwidth=0.90)

        # self.mensaje=tk.Label(text="", fg="red")
        # self.mensaje.place(x=230 ,y=130)


        

        agregar_producto=tk.Button()
        agregar_producto["bg"] = "#90ee90"
        ft = tkFont.Font(family='Times',size=10)
        agregar_producto["font"] = ft
        agregar_producto["fg"] = "#000000"
        agregar_producto["justify"] = "center"
        agregar_producto["text"] = "Agregar Producto"
        agregar_producto.place(x=210,rely=0.30,width=191,height=30)
        agregar_producto["command"] = self.agregar_productos


        GButton_483=tk.Button()
        GButton_483["activebackground"] = "#d22b2b"
        GButton_483["bg"] = "#ad2323"
        GButton_483["cursor"] = "sizing"
        ft = tkFont.Font(family='Times',size=10)
        GButton_483["font"] = ft
        GButton_483["fg"] = "#fcfcfc"
        GButton_483["justify"] = "center"
        GButton_483["text"] = "Eliminar"
        GButton_483.place(relx=.40,rely=0.30,width=208,height=30)
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

        GButton_637=tk.Button()
        GButton_637["bg"] = "#00ced1"
        GButton_637["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GButton_637["font"] = ft
        GButton_637["fg"] = "#ffffff"
        GButton_637["justify"] = "center"
        GButton_637["text"] = "Auto Llenar"
        GButton_637.place(x=810,y=90,width=117,height=30)
        GButton_637["command"] = self.auto_llenar

    

       


    # def agregar_producto_command(self):
    #     nombre=self.txtNombre.get()
    #     precio=self.precio.get()
    #     self.txtNombre.delete(0,"end")
    #     self.precio.delete(0,"end")



principal=Tk()
principal.wm_title("Producto")
principal.geometry("1080x800")
marco=Aplicacion(principal)


principal.mainloop()
