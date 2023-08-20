from io import BytesIO
import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3

def load_pokemon():
    input_text = text_id_name.get(1.0, "end-1c").strip()  # Remover espaços em branco
    pokemon = pypokedex.get(name=input_text)

    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))
    image = PIL.Image.open(BytesIO(response.data))

    img = PIL.ImageTk.PhotoImage(image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=" - ".join([t for t in pokemon.types]))

    # Limpar o campo de busca
    text_id_name.delete(1.0, "end-1c")

def on_enter_pressed(event):
    load_pokemon()

window = tk.Tk()
window.geometry("600x500")
window.title("PyDex")
window.config(padx=10, pady=10)
window.resizable(True, True)

title_label = tk.Label(window, text="PyDex")
title_label.config(font=("Arial", 32))
title_label.pack(padx=10, pady=10)

pokemon_image = tk.Label(window)
pokemon_image.pack()

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 32))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 32))
pokemon_types.pack(padx=10, pady=10)

label_id_name = tk.Label(window, text="Number or Name")
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Load Pokémon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)

text_id_name.bind("<Return>", on_enter_pressed)

window.mainloop()
