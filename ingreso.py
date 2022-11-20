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

        GLabel_759=tk.Label(root)
        ft = tkFont.Font(family='Times',size=26)
        GLabel_759["font"] = ft
        GLabel_759["fg"] = "#333333"
        GLabel_759["justify"] = "center"
        GLabel_759["text"] = "Bienvenidos a Supermark"
        GLabel_759.place(x=130,y=60,width=360,height=70)

        GButton_985=tk.Button(root)
        GButton_985["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        GButton_985["font"] = ft
        GButton_985["fg"] = "#000000"
        GButton_985["justify"] = "center"
        GButton_985["text"] = "Admnistrador"
        GButton_985.place(x=230,y=240,width=146,height=75)
        GButton_985["command"] = self.GButton_985_command

        GButton_849=tk.Button(root)
        GButton_849["bg"] = "#f0f0f0"
        ft = tkFont.Font(family='Times',size=16)
        GButton_849["font"] = ft
        GButton_849["fg"] = "#000000"
        GButton_849["justify"] = "center"
        GButton_849["text"] = "Usuario"
        GButton_849.place(x=230,y=340,width=148,height=73)
        GButton_849["command"] = self.GButton_849_command

        GLabel_114=tk.Label(root)
        ft = tkFont.Font(family='Times',size=14)
        GLabel_114["font"] = ft
        GLabel_114["fg"] = "#333333"
        GLabel_114["justify"] = "center"
        GLabel_114["text"] = "Selecciona tu perfil para ingresar al sistema:"
        GLabel_114.place(x=110,y=160,width=400,height=80)

    def GButton_985_command(self):
        print("command")


    def GButton_849_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()