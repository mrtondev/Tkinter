from tkinter import *

class Janela:
    def __init__(self,toplevel):
        self.frl = Frame(toplevel)
        self.frl.pack()
        self.botao = Button(self.frl, text='Oi!', background='green')
        self.botao.pack()
raiz=Tk()
Janela(raiz)
raiz.mainloop()        