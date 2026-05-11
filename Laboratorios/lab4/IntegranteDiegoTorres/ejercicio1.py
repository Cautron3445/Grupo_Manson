import pandas as pd

lista_de_reproduccion = {
    "Canción": ["just the way you are", "Tipping Point", "Lazy Generation", "Imagine"],
    "Artista": ["Bruno Mars", "Tipping Point", "Lazy Generation", "John Lennon"],
    "Duración (segundos)": [230, 210, 180, 183]
}
df = pd.DataFrame(lista_de_reproduccion)