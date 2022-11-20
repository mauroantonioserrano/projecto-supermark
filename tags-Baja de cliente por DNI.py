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

        GLabel_630=tk.Label(root)
        GLabel_630["bg"] = "#b8abb3"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_630["font"] = ft
        GLabel_630["fg"] = "#a38f9b"
        GLabel_630["justify"] = "center"
        GLabel_630["text"] = ""
        GLabel_630.place(x=100,y=70,width=438,height=344)

        GLabel_178=tk.Label(root)
        GLabel_178["bg"] = "#b8abb3"
        ft = tkFont.Font(family='Times',size=18)
        GLabel_178["font"] = ft
        GLabel_178["fg"] = "#060606"
        GLabel_178["justify"] = "center"
        GLabel_178["text"] = "DNI"
        GLabel_178.place(x=140,y=170,width=70,height=25)

        GLineEdit_77=tk.Entry(root)
        GLineEdit_77["bg"] = "#f4eff2"
        GLineEdit_77["borderwidth"] = "2px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_77["font"] = ft
        GLineEdit_77["fg"] = "#333333"
        GLineEdit_77["justify"] = "center"
        GLineEdit_77["text"] = ""
        GLineEdit_77.place(x=210,y=170,width=196,height=30)

        GButton_480=tk.Button(root)
        GButton_480["bg"] = "#686f87"
        ft = tkFont.Font(family='Times',size=10)
        GButton_480["font"] = ft
        GButton_480["fg"] = "#000000"
        GButton_480["justify"] = "center"
        GButton_480["text"] = "Buscar"
        GButton_480.place(x=410,y=170,width=69,height=30)
        GButton_480["command"] = self.GButton_480_command

        GButton_539=tk.Button(root)
        GButton_539["bg"] = "#f81111"
        ft = tkFont.Font(family='Times',size=8)
        GButton_539["font"] = ft
        GButton_539["fg"] = "#000000"
        GButton_539["justify"] = "center"
        GButton_539["text"] = "ELIMINAR"
        GButton_539.place(x=190,y=230,width=63,height=33)
        GButton_539["command"] = self.GButton_539_command

        GButton_525=tk.Button(root)
        GButton_525["bg"] = "#686f87"
        ft = tkFont.Font(family='Times',size=8)
        GButton_525["font"] = ft
        GButton_525["fg"] = "#000000"
        GButton_525["justify"] = "center"
        GButton_525["text"] = "SALIR"
        GButton_525.place(x=380,y=230,width=63,height=33)
        GButton_525["command"] = self.GButton_525_command

        GButton_258=tk.Button(root)
        GButton_258["bg"] = "#686f87"
        ft = tkFont.Font(family='Times',size=8)
        GButton_258["font"] = ft
        GButton_258["fg"] = "#000000"
        GButton_258["justify"] = "center"
        GButton_258["text"] = "GUARDAR"
        GButton_258.place(x=280,y=230,width=63,height=33)
        GButton_258["command"] = self.GButton_258_command

        GLabel_728=tk.Label(root)
        GLabel_728["bg"] = "#b8abb3"
        ft = tkFont.Font(family='Times',size=28)
        GLabel_728["font"] = ft
        GLabel_728["fg"] = "#5fb878"
        GLabel_728["justify"] = "center"
        GLabel_728["text"] = "Supermark"
        GLabel_728.place(x=220,y=110,width=183,height=30)

    def GButton_480_command(self):
        print("command")


    def GButton_539_command(self):
        print("command")


    def GButton_525_command(self):
        print("command")


    def GButton_258_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
