import datetime

from tkinter import *

#colors

co0 = "#4169E1" #RoyalBlue
co01 = "#C0C0C0" #Silver
co02 = "f0f3f5" #Black


#window 

window = Tk()
window.title("Despertador")
window.geometry("1440x900")
window.configure(background= 'lightblue')
window.resizable(width=TRUE, height=TRUE)



data=datetime.date(2023,4,11)
print(data)

print(data.ctime())

ano = data.year
mes = data.month
dia = data.day

#hora = data.hora # error
print(ano, mes, dia)




mainloop()