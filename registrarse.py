import tkinter as tk
import tkinter.font as tkFont
import sqlite3

class App:
    def __init__(self, root):
        #setting title
        root.title("registrarse")
        #setting window size
        width=634
        height=638
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        self.tabla_registro()

        GLabel_485=tk.Label(root)
        GLabel_485["activebackground"] = "#1e90ff"
        GLabel_485["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_485["font"] = ft
        GLabel_485["fg"] = "#333333"
        GLabel_485["justify"] = "center"
        GLabel_485["text"] = "Completa con tus datos para Comenzar"
        GLabel_485.place(x=140,y=10,width=344,height=66)

        GLabel_34=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_34["font"] = ft
        GLabel_34["fg"] = "#333333"
        GLabel_34["justify"] = "right"
        GLabel_34["text"] = "Apellido"
        GLabel_34.place(x=120,y=120,width=70,height=25)

        GLabel_817=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_817["font"] = ft
        GLabel_817["fg"] = "#333333"
        GLabel_817["justify"] = "right"
        GLabel_817["text"] = "Nombre"
        GLabel_817.place(x=120,y=160,width=70,height=25)

        self.ingresar_apellido=tk.Entry(root)
        self.ingresar_apellido.focus()
        self.ingresar_apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_apellido["font"] = ft
        self.ingresar_apellido["fg"] = "#333333"
        self.ingresar_apellido["justify"] = "left"
        self.ingresar_apellido["text"] = "Ingresa tu apellido"
        self.ingresar_apellido.place(x=210,y=110,width=170,height=39)

        self.ingresar_nombre=tk.Entry(root)
        self.ingresar_nombre.focus()
        self.ingresar_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_nombre["font"] = ft
        self.ingresar_nombre["fg"] = "#333333"
        self.ingresar_nombre["justify"] = "left"
        self.ingresar_nombre["text"] = "ingresa tu nombre"
        self.ingresar_nombre.place(x=210,y=160,width=168,height=37)

        GLabel_609=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_609["font"] = ft
        GLabel_609["fg"] = "#333333"
        GLabel_609["justify"] = "right"
        GLabel_609["text"] = "DNI"
        GLabel_609.place(x=110,y=210,width=70,height=25)

        self.ingresar_dni=tk.Entry(root)
        self.ingresar_dni.focus()
        self.ingresar_dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_dni["font"] = ft
        self.ingresar_dni["fg"] = "#333333"
        self.ingresar_dni["justify"] = "left"
        self.ingresar_dni["text"] = "ingresa tu Dni"
        self.ingresar_dni.place(x=210,y=210,width=167,height=37)

        GLabel_165=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_165["font"] = ft
        GLabel_165["fg"] = "#333333"
        GLabel_165["justify"] = "right"
        GLabel_165["text"] = "Nombre de Usuario"
        GLabel_165.place(x=40,y=260,width=148,height=47)

        self.ingresar_nombre_de_usuario=tk.Entry(root)
        self.ingresar_nombre_de_usuario.focus()
        self.ingresar_nombre_de_usuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_nombre_de_usuario["font"] = ft
        self.ingresar_nombre_de_usuario["fg"] = "#333333"
        self.ingresar_nombre_de_usuario["justify"] = "left"
        self.ingresar_nombre_de_usuario["text"] = "nombre de Usuario"
        self.ingresar_nombre_de_usuario.place(x=210,y=260,width=168,height=39)

        GLabel_9=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "#333333"
        GLabel_9["justify"] = "right"
        GLabel_9["text"] = "Contraseña"
        GLabel_9.place(x=100,y=310,width=86,height=30)

        self.ingresar_constrasenia=tk.Entry(root)
        self.ingresar_constrasenia.focus()
        self.ingresar_constrasenia["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_constrasenia["font"] = ft
        self.ingresar_constrasenia["fg"] = "#333333"
        self.ingresar_constrasenia["justify"] = "left"
        self.ingresar_constrasenia["text"] = "contraseña"
        self.ingresar_constrasenia.place(x=210,y=310,width=164,height=37)

        email_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        email_label["font"] = ft
        email_label["fg"] = "#333333"
        email_label["justify"] = "right"
        email_label["text"] = "E-mail"
        email_label.place(x=110,y=370,width=70,height=25)

        self.ingresar_email=tk.Entry(root)
        self.ingresar_email.focus()
        self.ingresar_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_email["font"] = ft
        self.ingresar_email["fg"] = "#333333"
        self.ingresar_email["justify"] = "left"
        self.ingresar_email["text"] = "micorreo@gmail.com"
        self.ingresar_email.place(x=210,y=360,width=164,height=41)

        GLabel_672=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_672["font"] = ft
        GLabel_672["fg"] = "#333333"
        GLabel_672["justify"] = "right"
        GLabel_672["text"] = "Domicilio"
        GLabel_672.place(x=110,y=460,width=70,height=25)

        self.ingresar_domicilio=tk.Entry(root)
        self.ingresar_domicilio.focus()
        self.ingresar_domicilio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_domicilio["font"] = ft
        self.ingresar_domicilio["fg"] = "#333333"
        self.ingresar_domicilio["justify"] = "left"
        self.ingresar_domicilio["text"] = "domicilio"
        self.ingresar_domicilio["relief"] = "ridge"
        self.ingresar_domicilio.place(x=210,y=460,width=162,height=35)

        GLabel_823=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_823["font"] = ft
        GLabel_823["fg"] = "#333333"
        GLabel_823["justify"] = "right"
        GLabel_823["text"] = "Telefono"
        GLabel_823.place(x=110,y=510,width=70,height=25)

        self.ingresar_telefono=tk.Entry(root)
        self.ingresar_telefono.focus()
        self.ingresar_telefono["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_telefono["font"] = ft
        self.ingresar_telefono["fg"] = "#333333"
        self.ingresar_telefono["justify"] = "left"
        self.ingresar_telefono["text"] = "telefono de contacto"
        self.ingresar_telefono.place(x=210,y=510,width=161,height=36)

        boton_confirmar=tk.Button(root)
        boton_confirmar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        boton_confirmar["font"] = ft
        boton_confirmar["fg"] = "#000000"
        boton_confirmar["justify"] = "center"
        boton_confirmar["text"] = "Confirmar"
        boton_confirmar.place(x=280,y=570,width=98,height=35)
        boton_confirmar["command"] = self.boton_confirmar_command

        boton_limpiar=tk.Button(root)
        boton_limpiar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        boton_limpiar["font"] = ft
        boton_limpiar["fg"] = "#000000"
        boton_limpiar["justify"] = "center"
        boton_limpiar["text"] = "Limpiar"
        boton_limpiar.place(x=60,y=590,width=98,height=36)
        boton_limpiar["command"] = self.boton_limpiar_command

        boton_cerrar=tk.Button(root)
        boton_cerrar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        boton_cerrar["font"] = ft
        boton_cerrar["fg"] = "#000000"
        boton_cerrar["justify"] = "center"
        boton_cerrar["text"] = "Cerrar"
        boton_cerrar.place(x=400,y=570,width=89,height=33)
        boton_cerrar["command"] = self.boton_cerrar_command

        GLabel_112=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_112["font"] = ft
        GLabel_112["fg"] = "#333333"
        GLabel_112["justify"] = "right"
        GLabel_112["text"] = "Confirma tu E-mail"
        GLabel_112.place(x=30,y=410,width=147,height=30)

        self.repetir_email=tk.Entry(root)
        self.repetir_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.repetir_email["font"] = ft
        self.repetir_email["fg"] = "#333333"
        self.repetir_email["justify"] = "left"
        self.repetir_email["text"] = "repite tu correo"
        self.repetir_email.place(x=210,y=410,width=161,height=36)

    def tabla_registro(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()
        # cursor.execute("DROP TABLE usuario")
        cursor.execute("""CREATE TABLE IF NOT EXISTS usuario (id INTEGER PRIMARY KEY AUTOINCREMENT, apellido TEXT (25) NOT NULL, nombre TEXT (25) NOT NULL, 
        DNI INTEGER(9) NOT NULL, nombre_de_usuario TEXT NOT NULL,contraseña TEXT (25) NOT NULL, mail TEXT (30) NOT NULL,confirmar_mail TEXT (30) NOT NULL, domicilio TEXT (30) NOT NULL,telefono INTEGER (25) NOT NULL)""")
        #limpiar=self.tabla_registro.delete(self.t)
        conexion.close()

    def boton_confirmar_command(self):
        conexion=sqlite3.connect("supermercado.db")
        cursor=conexion.cursor()
        a=self.ingresar_apellido.get()
        b=self.ingresar_nombre.get()
        c=self.ingresar_dni.get()
        d=self.ingresar_nombre_de_usuario.get()
        e=self.ingresar_constrasenia.get()
        f=self.ingresar_email.get()
        r=self.repetir_email.get()
        g=self.ingresar_domicilio.get()
        h=self.ingresar_telefono.get()
        print(a)
        print(b)
        print(c)
        print(d)
        print(e)
        print(f)
        print(r)
        print(g)
        print(h)
        cursor.execute(f"""INSERT INTO usuario VALUES(NULL, "{a}","{b}", "{c}", "{d}", "{e}", "{f}","{r}" ,"{g}", "{h}")""")
        conexion.commit()
        conexion.close()

        
    def boton_limpiar_command(self):
        limpiar=self.ingresar_apellido.delete(0,"end")
        #self.ingresar_apellido= " "
        #self.ingresar_apellido_entry["text"] =self.ingresar_apellido
        print("command")


    def boton_cerrar_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
