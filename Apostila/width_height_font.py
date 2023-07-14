from tkinter import *
class Janela:
    def __init__(self,toplevel):
        self.frl = Frame(toplevel)
        self.frl.pack()

        self.botao1 = Button(self.frl,text='Oi!')
        self.botao1['background']='green'
        self.botao1['font']=('verdana','12','italic','bold')
        self.botao1['height']=3
        self.botao1.pack()

        self.botao2 = Button(self.frl,bg='red', font=('Times','16'))
        self.botao2['text']='Tchau!'
        self.botao2['fg']='yellow'
        self.botao2['width']=12
        self.botao2.pack()

raiz=Tk()
Janela(raiz)
raiz.mainloop()