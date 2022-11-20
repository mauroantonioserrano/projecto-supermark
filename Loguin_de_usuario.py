import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("Registro de Cliente")
        #setting window size
        width=917
        height=511
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        
        



        GLabel_229=tk.Label(root)
        ft = tkFont.Font(family='Times',size=48)
        GLabel_229["font"] = ft
        GLabel_229["fg"] = "#5ece5e"
        GLabel_229["justify"] = "center"
        GLabel_229["text"] = "SuperMark"
        GLabel_229.place(relx=0.35,rely=0.05,width=300,height=100)

        GLabel_352=tk.Label(root)
        ft = tkFont.Font(family='Times',size=33)
        GLabel_352["font"] = ft
        GLabel_352["fg"] = "#333333"
        GLabel_352["justify"] = "center"
        GLabel_352["text"] = "Login"
        GLabel_352.place(relx=0.40,rely=0.30,width=200,height=45)

        GLabel_383=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_383["font"] = ft
        GLabel_383["fg"] = "#333333"
        GLabel_383["justify"] = "left"
        GLabel_383["text"] = "Nombre de Usario"
        GLabel_383.place(relx=.20,rely=.45,width=200,height=32)

        GLabel_787=tk.Label(root)
        ft = tkFont.Font(family='Times',size=18)
        GLabel_787["font"] = ft
        GLabel_787["fg"] = "#333333"
        GLabel_787["justify"] = "right"
        GLabel_787["text"] = "Contraseña"
        GLabel_787.place(x=180,rely=.60,width=200,height=32)

        nombre_de_usuario=tk.Entry(root)
        nombre_de_usuario.focus()
        nombre_de_usuario["bg"] = "#f6f1f1"
        nombre_de_usuario["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        nombre_de_usuario["font"] = ft
        nombre_de_usuario["fg"] = "#333333"
        nombre_de_usuario["justify"] = "left"
        nombre_de_usuario["relief"] = "flat"
        nombre_de_usuario.place(x=420,rely=.45,width=180,height=32)

        contrasenia=tk.Entry(root)
        contrasenia["bg"] = "#f7f5f5"
        contrasenia["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=13)
        contrasenia["font"] = ft
        contrasenia["fg"] = "#333333"
        contrasenia["justify"] = "left"
        contrasenia["relief"] = "flat"
        contrasenia.place(x=420,rely=.60,width=180,height=32)

        boton_ingresar=tk.Button(root)
        boton_ingresar["bg"] = "#009688"
        ft = tkFont.Font(family='Times',size=18)
        boton_ingresar["font"] = ft
        boton_ingresar["fg"] = "#ffffff"
        boton_ingresar["justify"] = "center"
        boton_ingresar["text"] = "Ingresar"
        boton_ingresar["relief"] = "groove"
        boton_ingresar.place(relx=0.20,rely=0.72,width=145,height=43)
        boton_ingresar["command"] = self.boton_ingresar_command

        boton_registrarse=tk.Button(root)
        boton_registrarse["bg"] = "#52ed20"
        ft = tkFont.Font(family='Times',size=13)
        boton_registrarse["font"] = ft
        boton_registrarse["fg"] = "#ffffff"
        boton_registrarse["justify"] = "center"
        boton_registrarse["text"] = "Registrarse"
        boton_registrarse.place(x=770,y=30,width=95,height=41)
        boton_registrarse["command"] = self.boton_registrarse_command

    def boton_ingresar_command(self):
        print("command")


    def boton_registrarse_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
