import tkinter as tk
import tkinter.font as tkFont
import sqlite3
from tkinter import messagebox
from PIL import Image, ImageTk

class Registrarse:
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
          # Crea una imagen a partir de un archivo
        root.imagen = Image.open("istockphoto-1275827044-612x612 - Editada.png")
        root.imagen=root.imagen.resize((850,700),Image.ANTIALIAS)

        
        # Crea una imagen que pueda ser mostrada en un widget de tkinter
        root.imagen_tk = ImageTk.PhotoImage(root.imagen)

        # Crea un widget Label y lo configura para mostrar la imagen
        label_imagen = tk.Label(root)
        label_imagen.configure(image=root.imagen_tk)
        label_imagen.place(relx=0,rely=0)


        self.tabla_registro()


        GLabel_485=tk.Label(root)
        GLabel_485["activebackground"] = "#1e90ff"
        GLabel_485["anchor"] = "nw"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_485["font"] = ft
        GLabel_485["fg"] = "white"
        GLabel_485["bg"] ="grey"
        GLabel_485["justify"] = "center"
        GLabel_485["text"] = "Completa con tus datos para registrarte "
        GLabel_485.place(x=140,y=10)

        GLabel_34=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_34["font"] = ft
        GLabel_34["fg"] = "white"
        GLabel_34["justify"] = "right"
        GLabel_34["bg"]="grey"
        GLabel_34["text"] = "Apellido"
        GLabel_34.place(relx=0.05,rely=0.15)

        GLabel_817=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_817["font"] = ft
        GLabel_817["fg"] = "white"
        GLabel_817["bg"]="grey"
        GLabel_817["justify"] = "right"
        GLabel_817["text"] = "Nombre"
        GLabel_817.place(relx=0.50,rely=0.15)

        self.ingresar_apellido=tk.Entry(root)
        self.ingresar_apellido.focus()
        self.ingresar_apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_apellido["font"] = ft
        self.ingresar_apellido["fg"] = "#333333"
        self.ingresar_apellido["justify"] = "left"
        self.ingresar_apellido["text"] = "Ingresa tu apellido"
        self.ingresar_apellido.place(relx=0.18,rely=0.15)

        self.ingresar_nombre=tk.Entry(root)
        self.ingresar_nombre.focus()
        self.ingresar_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_nombre["font"] = ft
        self.ingresar_nombre["fg"] = "#333333"
        self.ingresar_nombre["justify"] = "left"
        self.ingresar_nombre["text"] = "ingresa tu nombre"
        self.ingresar_nombre.place(relx=0.60,rely=0.15)

        GLabel_609=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_609["font"] = ft
        GLabel_609["fg"] = "white"
        GLabel_609["bg"] = "grey"
        GLabel_609["justify"] = "right"
        GLabel_609["text"] = "DNI"
        GLabel_609.place(relx=0.05,rely=0.25)

        self.ingresar_dni=tk.Entry(root)
        self.ingresar_dni.focus()
        self.ingresar_dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_dni["font"] = ft
        self.ingresar_dni["fg"] = "#333333"
        self.ingresar_dni["justify"] = "left"
        self.ingresar_dni["text"] = "ingresa tu Dni"
        self.ingresar_dni.place(relx=0.18,rely=0.25)

        GLabel_165=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_165["font"] = ft
        GLabel_165["fg"] = "white"
        GLabel_165["bg"] = "grey"
        GLabel_165["justify"] = "right"
        GLabel_165["text"] = "Nombre de Usuario"
        GLabel_165.place(relx=.5,rely=0.25)

        self.ingresar_nombre_de_usuario=tk.Entry(root)
        self.ingresar_nombre_de_usuario.focus()
        self.ingresar_nombre_de_usuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_nombre_de_usuario["font"] = ft
        self.ingresar_nombre_de_usuario["fg"] = "#333333"
        self.ingresar_nombre_de_usuario["justify"] = "left"
        self.ingresar_nombre_de_usuario["text"] = "nombre de Usuario"
        self.ingresar_nombre_de_usuario.place(relx=0.74,rely=0.25,width=140)

        GLabel_9=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "white"
        GLabel_9["bg"] ="grey"
        GLabel_9["justify"] = "right"
        GLabel_9["text"] = "Contraseña"
        GLabel_9.place(relx=0.05,rely=0.45)

        self.ingresa_contrasenia=tk.Entry(root)
        self.ingresa_contrasenia.focus()
        self.ingresa_contrasenia["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresa_contrasenia["font"] = ft
        self.ingresa_contrasenia["fg"] = "#333333"
        self.ingresa_contrasenia["justify"] = "left"
        self.ingresa_contrasenia["text"] = "contraseña"
        self.ingresa_contrasenia.place(relx=0.18,rely=0.45)

        GLabel_100=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_100["font"] = ft
        GLabel_100["fg"] = "white"
        GLabel_100["bg"] = "grey"
        GLabel_100["justify"] = "right"
        GLabel_100["text"] = "Confirmar Contraseña"
        GLabel_100.place(relx=0.50,rely=0.45)

        self.confirmar_contrasenia=tk.Entry(root)
        self.confirmar_contrasenia.focus()
        self.confirmar_contrasenia["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.confirmar_contrasenia["font"] = ft
        self.confirmar_contrasenia["fg"] = "#333333"
        self.confirmar_contrasenia["justify"] = "left"
        self.confirmar_contrasenia["text"] = "confirmar contraseña"
        self.confirmar_contrasenia.place(relx=0.76,rely=0.45,width=130)

        email_label=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        email_label["font"] = ft
        email_label["fg"] = "white"
        email_label["bg"]="grey"
        email_label["justify"] = "right"
        email_label["text"] = "E-mail"
        email_label.place(relx=0.05,rely=0.35)

        self.ingresar_email=tk.Entry(root)
        self.ingresar_email.focus()
        self.ingresar_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_email["font"] = ft
        self.ingresar_email["fg"] = "#333333"
        self.ingresar_email["justify"] = "left"
        self.ingresar_email["text"] = "micorreo@gmail.com"
        self.ingresar_email.place(relx=0.18,rely=0.35)

        GLabel_672=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_672["font"] = ft
        GLabel_672["fg"] = "white"
        GLabel_672["bg"] ="grey"
        GLabel_672["justify"] = "right"
        GLabel_672["text"] = "Domicilio"
        GLabel_672.place(relx=0.05,rely=.55)

        self.ingresar_domicilio=tk.Entry(root)
        self.ingresar_domicilio.focus()
        self.ingresar_domicilio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_domicilio["font"] = ft
        self.ingresar_domicilio["fg"] = "#333333"
        self.ingresar_domicilio["justify"] = "left"
        self.ingresar_domicilio["text"] = "domicilio"
        self.ingresar_domicilio["relief"] = "ridge"
        self.ingresar_domicilio.place(relx=0.18,rely=.55)

        GLabel_823=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_823["font"] = ft
        GLabel_823["fg"] = "white"
        GLabel_823["bg"] ="grey"
        GLabel_823["justify"] = "right"
        GLabel_823["text"] = "Telefono"
        GLabel_823.place(relx=.5,rely=.55)

        self.ingresar_telefono=tk.Entry(root)
        self.ingresar_telefono.focus()
        self.ingresar_telefono["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.ingresar_telefono["font"] = ft
        self.ingresar_telefono["fg"] = "#333333"
        self.ingresar_telefono["justify"] = "left"
        self.ingresar_telefono["text"] = "telefono de contacto"
        self.ingresar_telefono.place(relx=0.63,rely=.55)

        boton_confirmar=tk.Button(root)
        boton_confirmar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        boton_confirmar["font"] = ft
        boton_confirmar["fg"] = "white"
        boton_confirmar["bg"]="green"
        boton_confirmar["justify"] = "center"
        boton_confirmar["text"] = "Confirmar"
        boton_confirmar.place(x=280,y=570,width=98,height=35)
        boton_confirmar["command"] = self.boton_confirmar_command

        boton_limpiar=tk.Button(root)
        boton_limpiar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=11)
        boton_limpiar["font"] = ft
        boton_limpiar["bg"]="grey"
        boton_limpiar["fg"] = "white"
        boton_limpiar["justify"] = "center"
        boton_limpiar["text"] = "Limpiar"
        boton_limpiar.place(relx=.15,rely=.89,width=98,height=36)
        boton_limpiar["command"] = self.boton_limpiar_command

        self.boton_cerrar=tk.Button(root)
        self.boton_cerrar["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=13)
        self.boton_cerrar["font"] = ft
        self.boton_cerrar["fg"] = "white"
        self.boton_cerrar["bg"] = "red"
        self.boton_cerrar["justify"] = "center"
        self.boton_cerrar["text"] = "Cerrar"
        self.boton_cerrar.place(x=400,y=570,width=89,height=33)
        self.boton_cerrar["command"] =self.boton_cerrar_command

        GLabel_112=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_112["font"] = ft
        GLabel_112["fg"] = "white"
        GLabel_112["bg"] = "grey"
        GLabel_112["justify"] = "right"
        GLabel_112["text"] = "Confirma tu E-mail"
        GLabel_112.place(relx=0.5,rely=0.35)

        self.repetir_email=tk.Entry(root)
        self.repetir_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        self.repetir_email["font"] = ft
        self.repetir_email["fg"] = "#333333"
        self.repetir_email["justify"] = "left"
        self.repetir_email["text"] = "repite tu correo"
        self.repetir_email.place(relx=0.74,rely=0.35,width=140)

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
        e=self.ingresa_contrasenia.get()
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
        messagebox.showinfo(message="se han guardados sus datos",title="ventana registro")

        
    def boton_limpiar_command(self):
        self.ingresar_apellido.delete(0,"end")
        self.ingresar_nombre.delete(0,"end")
        self.ingresar_dni.delete(0,"end")
        self.ingresar_nombre_de_usuario.delete(0,"end")
        self.ingresar_email.delete(0,"end")
        self.repetir_email.delete(0,"end")
        self.ingresa_contrasenia.delete(0,"end")
        self.confirmar_contrasenia.delete(0,"end")
        self.ingresar_domicilio.delete(0,"end")
        self.ingresar_telefono.delete(0,"end")
        #self.ingresar_apellido= " "
        #self.ingresar_apellido_entry["text"] =self.ingresar_apellido
        


    def boton_cerrar_command(self):
        self.boton_cerrar.quit()


if __name__ == "__main__":
    root = tk.Tk()
    registrarse = Registrarse(root)
    root.mainloop()


