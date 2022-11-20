import tkinter as tk
import tkinter.font as tkFont

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

        GLabel_973=tk.Label(root)
        GLabel_973["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_973["font"] = ft
        GLabel_973["fg"] = "#333333"
        GLabel_973["justify"] = "center"
        GLabel_973["text"] = ""
        GLabel_973.place(x=40,y=20,width=531,height=481)

        GLabel_565=tk.Label(root)
        GLabel_565["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_565["font"] = ft
        GLabel_565["fg"] = "#333333"
        GLabel_565["justify"] = "center"
        GLabel_565["text"] = "Apellido"
        GLabel_565.place(x=60,y=70,width=70,height=25)

        GLineEdit_744=tk.Entry(root)
        GLineEdit_744["bg"] = "#f9f5f5"
        GLineEdit_744["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_744["font"] = ft
        GLineEdit_744["fg"] = "#333333"
        GLineEdit_744["justify"] = "center"
        GLineEdit_744["text"] = ""
        GLineEdit_744.place(x=180,y=70,width=215,height=30)

        GLabel_33=tk.Label(root)
        GLabel_33["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_33["font"] = ft
        GLabel_33["fg"] = "#333333"
        GLabel_33["justify"] = "center"
        GLabel_33["text"] = "Nombre"
        GLabel_33.place(x=60,y=110,width=70,height=25)

        GLabel_216=tk.Label(root)
        GLabel_216["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_216["font"] = ft
        GLabel_216["fg"] = "#333333"
        GLabel_216["justify"] = "center"
        GLabel_216["text"] = "DNI"
        GLabel_216.place(x=50,y=150,width=70,height=25)

        GLabel_445=tk.Label(root)
        GLabel_445["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_445["font"] = ft
        GLabel_445["fg"] = "#333333"
        GLabel_445["justify"] = "center"
        GLabel_445["text"] = "ID  Cliente"
        GLabel_445.place(x=40,y=190,width=128,height=30)

        GLabel_528=tk.Label(root)
        GLabel_528["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_528["font"] = ft
        GLabel_528["fg"] = "#333333"
        GLabel_528["justify"] = "center"
        GLabel_528["text"] = "Contraseña"
        GLabel_528.place(x=70,y=230,width=70,height=25)

        GLabel_128=tk.Label(root)
        GLabel_128["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_128["font"] = ft
        GLabel_128["fg"] = "#333333"
        GLabel_128["justify"] = "center"
        GLabel_128["text"] = "E-mail"
        GLabel_128.place(x=50,y=260,width=82,height=30)

        GLabel_131=tk.Label(root)
        GLabel_131["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_131["font"] = ft
        GLabel_131["fg"] = "#333333"
        GLabel_131["justify"] = "center"
        GLabel_131["text"] = "Confirmar Email"
        GLabel_131.place(x=70,y=310,width=90,height=30)

        GLabel_992=tk.Label(root)
        GLabel_992["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_992["font"] = ft
        GLabel_992["fg"] = "#333333"
        GLabel_992["justify"] = "center"
        GLabel_992["text"] = "Domicilio"
        GLabel_992.place(x=60,y=350,width=70,height=25)

        GLabel_402=tk.Label(root)
        GLabel_402["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_402["font"] = ft
        GLabel_402["fg"] = "#333333"
        GLabel_402["justify"] = "center"
        GLabel_402["text"] = "Telefono"
        GLabel_402.place(x=60,y=390,width=70,height=25)

        GLineEdit_965=tk.Entry(root)
        GLineEdit_965["bg"] = "#f9f5f5"
        GLineEdit_965["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_965["font"] = ft
        GLineEdit_965["fg"] = "#333333"
        GLineEdit_965["justify"] = "center"
        GLineEdit_965["text"] = ""
        GLineEdit_965.place(x=180,y=110,width=215,height=30)

        GLineEdit_655=tk.Entry(root)
        GLineEdit_655["bg"] = "#f9f5f5"
        GLineEdit_655["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_655["font"] = ft
        GLineEdit_655["fg"] = "#333333"
        GLineEdit_655["justify"] = "center"
        GLineEdit_655["text"] = ""
        GLineEdit_655.place(x=180,y=150,width=215,height=30)

        GLineEdit_634=tk.Entry(root)
        GLineEdit_634["bg"] = "#f9f5f5"
        GLineEdit_634["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_634["font"] = ft
        GLineEdit_634["fg"] = "#333333"
        GLineEdit_634["justify"] = "center"
        GLineEdit_634["text"] = ""
        GLineEdit_634.place(x=180,y=190,width=215,height=30)

        GLineEdit_810=tk.Entry(root)
        GLineEdit_810["bg"] = "#f9f5f5"
        GLineEdit_810["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_810["font"] = ft
        GLineEdit_810["fg"] = "#333333"
        GLineEdit_810["justify"] = "center"
        GLineEdit_810["text"] = ""
        GLineEdit_810.place(x=180,y=230,width=215,height=30)

        GLineEdit_857=tk.Entry(root)
        GLineEdit_857["bg"] = "#f9f5f5"
        GLineEdit_857["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_857["font"] = ft
        GLineEdit_857["fg"] = "#333333"
        GLineEdit_857["justify"] = "center"
        GLineEdit_857["text"] = ""
        GLineEdit_857.place(x=180,y=270,width=215,height=30)

        GLineEdit_44=tk.Entry(root)
        GLineEdit_44["bg"] = "#f9f5f5"
        GLineEdit_44["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_44["font"] = ft
        GLineEdit_44["fg"] = "#333333"
        GLineEdit_44["justify"] = "center"
        GLineEdit_44["text"] = ""
        GLineEdit_44.place(x=180,y=310,width=215,height=30)

        GLineEdit_838=tk.Entry(root)
        GLineEdit_838["bg"] = "#f9f5f5"
        GLineEdit_838["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_838["font"] = ft
        GLineEdit_838["fg"] = "#333333"
        GLineEdit_838["justify"] = "center"
        GLineEdit_838["text"] = ""
        GLineEdit_838.place(x=180,y=350,width=215,height=30)

        GButton_660=tk.Button(root)
        GButton_660["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_660["font"] = ft
        GButton_660["fg"] = "#000000"
        GButton_660["justify"] = "center"
        GButton_660["text"] = "Modificar"
        GButton_660.place(x=270,y=450,width=70,height=25)
        GButton_660["command"] = self.GButton_660_command

        GButton_407=tk.Button(root)
        GButton_407["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_407["font"] = ft
        GButton_407["fg"] = "#000000"
        GButton_407["justify"] = "center"
        GButton_407["text"] = "Cerrar"
        GButton_407.place(x=430,y=450,width=70,height=25)
        GButton_407["command"] = self.GButton_407_command

        GLineEdit_375=tk.Entry(root)
        GLineEdit_375["bg"] = "#f9f5f5"
        GLineEdit_375["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_375["font"] = ft
        GLineEdit_375["fg"] = "#333333"
        GLineEdit_375["justify"] = "center"
        GLineEdit_375["text"] = ""
        GLineEdit_375.place(x=180,y=390,width=215,height=30)

        GLabel_414=tk.Label(root)
        GLabel_414["bg"] = "#d9cfd5"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_414["font"] = ft
        GLabel_414["fg"] = "#333333"
        GLabel_414["justify"] = "center"
        GLabel_414["text"] = "Alta de Cliente"
        GLabel_414.place(x=210,y=20,width=170,height=44)

        GButton_618=tk.Button(root)
        GButton_618["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=10)
        GButton_618["font"] = ft
        GButton_618["fg"] = "#000000"
        GButton_618["justify"] = "center"
        GButton_618["text"] = "Guardar"
        GButton_618.place(x=90,y=450,width=70,height=25)
        GButton_618["command"] = self.GButton_618_command

    def GButton_660_command(self):
        print("command")


    def GButton_407_command(self):
        print("command")


    def GButton_618_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
