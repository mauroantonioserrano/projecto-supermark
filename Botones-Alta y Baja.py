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

        GLabel_0=tk.Label(root)
        GLabel_0["bg"] = "#ccbcc6"
        ft = tkFont.Font(family='Times',size=10)
        GLabel_0["font"] = ft
        GLabel_0["fg"] = "#333333"
        GLabel_0["justify"] = "center"
        GLabel_0["text"] = ""
        GLabel_0.place(x=80,y=50,width=404,height=327)

        GButton_408=tk.Button(root)
        GButton_408["bg"] = "#16d74a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_408["font"] = ft
        GButton_408["fg"] = "#000000"
        GButton_408["justify"] = "center"
        GButton_408["text"] = "Dar un Alta"
        GButton_408.place(x=250,y=190,width=66,height=38)
        GButton_408["command"] = self.GButton_408_command

        GButton_924=tk.Button(root)
        GButton_924["anchor"] = "center"
        GButton_924["bg"] = "#c81414"
        ft = tkFont.Font(family='Times',size=10)
        GButton_924["font"] = ft
        GButton_924["fg"] = "#000000"
        GButton_924["justify"] = "center"
        GButton_924["text"] = "Dar una baja"
        GButton_924.place(x=250,y=250,width=66,height=38)
        GButton_924["command"] = self.GButton_924_command

        GButton_606=tk.Button(root)
        GButton_606["bg"] = "#7b777a"
        ft = tkFont.Font(family='Times',size=10)
        GButton_606["font"] = ft
        GButton_606["fg"] = "#000000"
        GButton_606["justify"] = "center"
        GButton_606["text"] = "SALIR"
        GButton_606.place(x=430,y=70,width=38,height=30)
        GButton_606["command"] = self.GButton_606_command

        GLabel_388=tk.Label(root)
        GLabel_388["anchor"] = "center"
        GLabel_388["bg"] = "#ccbcc6"
        ft = tkFont.Font(family='Times',size=16)
        GLabel_388["font"] = ft
        GLabel_388["fg"] = "#060606"
        GLabel_388["justify"] = "center"
        GLabel_388["text"] = "Alta de Cliente"
        GLabel_388.place(x=220,y=130,width=136,height=37)

        GLabel_25=tk.Label(root)
        GLabel_25["anchor"] = "s"
        GLabel_25["bg"] = "#ccbcc6"
        ft = tkFont.Font(family='Times',size=28)
        GLabel_25["font"] = ft
        GLabel_25["fg"] = "#43b461"
        GLabel_25["justify"] = "center"
        GLabel_25["text"] = "Supermark"
        GLabel_25.place(x=210,y=80,width=153,height=51)

    def GButton_408_command(self):
        print("command")


    def GButton_924_command(self):
        print("command")


    def GButton_606_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
