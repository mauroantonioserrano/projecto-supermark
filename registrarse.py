import tkinter as tk
import tkinter.font as tkFont

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

        ingresar_apellido=tk.Entry(root)
        ingresar_apellido.focus()
        ingresar_apellido["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_apellido["font"] = ft
        ingresar_apellido["fg"] = "#333333"
        ingresar_apellido["justify"] = "left"
        ingresar_apellido["text"] = "Ingresa tu apellido"
        ingresar_apellido.place(x=210,y=110,width=170,height=39)

        ingresar_nombre=tk.Entry(root)
        ingresar_nombre["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_nombre["font"] = ft
        ingresar_nombre["fg"] = "#333333"
        ingresar_nombre["justify"] = "left"
        ingresar_nombre["text"] = "ingresa tu nombre"
        ingresar_nombre.place(x=210,y=160,width=168,height=37)

        GLabel_609=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_609["font"] = ft
        GLabel_609["fg"] = "#333333"
        GLabel_609["justify"] = "right"
        GLabel_609["text"] = "DNI"
        GLabel_609.place(x=110,y=210,width=70,height=25)

        ingresar_dni=tk.Entry(root)
        ingresar_dni["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_dni["font"] = ft
        ingresar_dni["fg"] = "#333333"
        ingresar_dni["justify"] = "left"
        ingresar_dni["text"] = "ingresa tu Dni"
        ingresar_dni.place(x=210,y=210,width=167,height=37)

        GLabel_165=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_165["font"] = ft
        GLabel_165["fg"] = "#333333"
        GLabel_165["justify"] = "right"
        GLabel_165["text"] = "Nombre de Usuario"
        GLabel_165.place(x=40,y=260,width=148,height=47)

        ingresar_nombre_de_usuario=tk.Entry(root)
        ingresar_nombre_de_usuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_nombre_de_usuario["font"] = ft
        ingresar_nombre_de_usuario["fg"] = "#333333"
        ingresar_nombre_de_usuario["justify"] = "left"
        ingresar_nombre_de_usuario["text"] = "nombre de Usuario"
        ingresar_nombre_de_usuario.place(x=210,y=260,width=168,height=39)

        GLabel_9=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_9["font"] = ft
        GLabel_9["fg"] = "#333333"
        GLabel_9["justify"] = "right"
        GLabel_9["text"] = "Contraseña"
        GLabel_9.place(x=100,y=310,width=86,height=30)

        ingresar_constrasenia=tk.Entry(root)
        ingresar_constrasenia["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_constrasenia["font"] = ft
        ingresar_constrasenia["fg"] = "#333333"
        ingresar_constrasenia["justify"] = "left"
        ingresar_constrasenia["text"] = "contraseña"
        ingresar_constrasenia.place(x=210,y=310,width=164,height=37)

        GLabel_834=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_834["font"] = ft
        GLabel_834["fg"] = "#333333"
        GLabel_834["justify"] = "right"
        GLabel_834["text"] = "E-mail"
        GLabel_834.place(x=110,y=370,width=70,height=25)

        ingresar_email=tk.Entry(root)
        ingresar_email["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_email["font"] = ft
        ingresar_email["fg"] = "#333333"
        ingresar_email["justify"] = "left"
        ingresar_email["text"] = "micorreo@gmail.com"
        ingresar_email.place(x=210,y=360,width=164,height=41)

        GLabel_672=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_672["font"] = ft
        GLabel_672["fg"] = "#333333"
        GLabel_672["justify"] = "right"
        GLabel_672["text"] = "Domicilio"
        GLabel_672.place(x=110,y=460,width=70,height=25)

        ingresar_domicilio=tk.Entry(root)
        ingresar_domicilio["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_domicilio["font"] = ft
        ingresar_domicilio["fg"] = "#333333"
        ingresar_domicilio["justify"] = "left"
        ingresar_domicilio["text"] = "domicilio"
        ingresar_domicilio["relief"] = "ridge"
        ingresar_domicilio.place(x=210,y=460,width=162,height=35)

        GLabel_823=tk.Label(root)
        ft = tkFont.Font(family='Times',size=13)
        GLabel_823["font"] = ft
        GLabel_823["fg"] = "#333333"
        GLabel_823["justify"] = "right"
        GLabel_823["text"] = "Telefono"
        GLabel_823.place(x=110,y=510,width=70,height=25)

        ingresar_telefono=tk.Entry(root)
        ingresar_telefono["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_telefono["font"] = ft
        ingresar_telefono["fg"] = "#333333"
        ingresar_telefono["justify"] = "left"
        ingresar_telefono["text"] = "telefono de contacto"
        ingresar_telefono.place(x=210,y=510,width=161,height=36)

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

        ingresar_de_nuevo_tu_correo=tk.Entry(root)
        ingresar_de_nuevo_tu_correo["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=12)
        ingresar_de_nuevo_tu_correo["font"] = ft
        ingresar_de_nuevo_tu_correo["fg"] = "#333333"
        ingresar_de_nuevo_tu_correo["justify"] = "left"
        ingresar_de_nuevo_tu_correo["text"] = "repite tu correo"
        ingresar_de_nuevo_tu_correo.place(x=210,y=410,width=161,height=36)

    def boton_confirmar_command(self):
        print("command")


    def boton_limpiar_command(self):
        print("command")


    def boton_cerrar_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
