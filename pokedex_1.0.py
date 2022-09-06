try:
    import pypokedex
    from PIL import Image, ImageTk
    import tkinter as tk
    import urllib3
    from io import BytesIO
except ImportError:
    import os
    os.system("pip install -r requeriments.txt")


window = tk.Tk()
window.geometry("1280x1050")
window.title("Pokedex")
window.configure(padx=10, pady=10)

scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.LEFT, fill=tk.Y)

title_label = tk.Label(window, text="Pokedex")
title_label.config(font=("Arial", 25))
title_label.pack(padx=5, pady=5)

pokemon_image = tk.Label(window)
pokemon_image.pack(padx=10, pady=7)

pokemon_information = tk.Label(window)
pokemon_information.config(font=("Arial", 12))
pokemon_information.pack(padx=10, pady=10)

pokemon_types = tk.Label(window)
pokemon_types.config(font=("Arial", 12))
pokemon_types.pack(padx=10, pady=10)

pokemon_description = tk.Label(window)
pokemon_description.config(font=("Arial", 12))
pokemon_description.pack(padx=10, pady=10)

def load_pokemon():
    pokemon = pypokedex.get(name=text_id_name.get(1.0, "end-1c"))

    http = urllib3.PoolManager()
    response = http.request("GET", pokemon.sprites.front.get("default"))
    image = Image.open(BytesIO(response.data))
    
    img = ImageTk.PhotoImage(image=image)
    pokemon_image.config(image=img)
    pokemon_image.image = img

    pokemon_information.config(text=f"{pokemon.dex} - {pokemon.name}")
    pokemon_types.config(text=f"{pokemon.types}")
    description = pokemon.get_descriptions()
    print(description)

label_id_name = tk.Label(window, text="ID or Name")  
label_id_name.config(font=("Arial", 20))
label_id_name.pack(padx=10, pady=60)

text_id_name = tk.Text(window, height=1)
text_id_name.config(font=("Arial", 15))
text_id_name.pack(padx=10, pady=3)

btn_load = tk.Button(window, text="Load Pokemon", command=load_pokemon)
btn_load.config(font=("Arial", 20))
btn_load.pack(padx=10, pady=10)


'''def motion(event):
    x, y = event.x, event.y
    print(f"x:{x} \ny:{y}")

window.bind("<Motion>", motion)
'''
window.mainloop()

