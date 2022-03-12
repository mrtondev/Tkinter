
from tkinter import *

window = Tk()

class Application():
    def __init__(self) :
        self.window = window
        self.tela()
        window.mainloop()
    def tela(self):
        self.window.title("Cadastro de clientes")
        self.window.config(background= 'black')
        self.window.geometry('700x500')
        self.window.resizable(True,True)
        self.window.maxsize(width=900,height=700)
        self.window.minsize(width=400,height=300)

Application()