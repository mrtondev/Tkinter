from io import BytesIO
import pypokedex
import PIL.Image
import PIL.ImageTk
import tkinter as tk
import urllib3

def load_pokemon():
    input_text = text_id_name.get(1.0, "end-1c").strip()  # Remover espaços em branco
    
    if not input_text:
        show_error("Digite o número ou nome do Pokémon.")
        return
    
    try:
        pokemon = pypokedex.get(name=input_text)
    except pypokedex.pypokedex.PyPokedexError:
        show_error(f"Não foi possível encontrar o Pokémon '{input_text}'.")
        hide_pokemon_info()  # Esconde informações do Pokémon em caso de erro
    else:
        http = urllib3.PoolManager()
        response = http.request("GET", pokemon.sprites.front.get("default"))
        image = PIL.Image.open(BytesIO(response.data))
        new_width = 200
        new_height = 200
        image = image.resize((new_width, new_height))

        img = PIL.ImageTk.PhotoImage(image)
        pokemon_image.config(image=img)
        pokemon_image.image = img

        pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
        pokemon_types.config(text=" - ".join([t for t in pokemon.types]))
        hide_error()  # Esconde mensagem de erro

    finally:
        # Limpar o campo de busca, independentemente do resultado
        text_id_name.delete(1.0, "end-1c")

def hide_error():
    error_label.config(text="")

def show_error(message):
    error_label.config(text=message)

def hide_pokemon_info():
    pokemon_image.config(image="")
    pokemon_information.config(text="")
    pokemon_types.config(text="")

def on_enter_pressed(event):
    load_pokemon()

window = tk.Tk()
window.geometry("700x600")
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

error_label = tk.Label(window, text="", fg="red")
error_label.pack()

text_id_name.bind("<Return>", on_enter_pressed)

window.mainloop()
