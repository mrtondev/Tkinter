import tkinter as tk

def on_button_click():
    text= entry.get()
    label.config(text=f"Você digitou: {text}")

root = tk.Tk()
root.title("Exemplo Avançado de Tkinter")

label = tk.Label(root, text="Digite algo e clique no botão:")
label.pack()

entry=tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Clique aqui", command=on_button_click)
button.pack()

root.mainloop()