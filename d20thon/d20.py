import math
from tkinter import *
from PIL import ImageTk, Image

root =Tk()

root.geometry("1440x900")
root.title("D20")    


# Image().grid(row=1,column = 0)
Button(text='Rolar o D20').grid(row= 2, column=0)

img = ImageTk.PhotoImage(Image.open("/home/ayrton/Documentos/code/python/Tkinter/d20thon/d20.py"))
l = Label(image=img)
l.pack()

# img = PhotoImage(file = "~/Documentos/code/python/Tkinter/d20thon/images/img.jpg")

label_imagem = Label(root, image=img).Pack()




root.mainloop()