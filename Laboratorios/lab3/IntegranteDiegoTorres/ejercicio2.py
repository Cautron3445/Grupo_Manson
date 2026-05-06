encuesta = {"Python": 45, 
            "C++": 28, 
            "C": 15, 
            "Java": 12, 
            "Rust": 8
            }

import matplotlib.pyplot as plt

def graficar_encuesta(**encuesta):

    print("------Resultados de la Encuesta--------")

    for lenguaje, votos in encuesta.items():
     print(f"{lenguaje}: {votos} votos")

graficar_encuesta(Python=45, Cplusplus=28, C=15, Java=12, Rust=8)

plt.bar(encuesta.keys(), encuesta.values(), color=['red', 'blue', 'green', 'orange', 'purple'])
plt.title("Resultados de la Encuesta de Lenguajes de Programación")
plt.xlabel("Lenguajes de Programación")
plt.ylabel("Número de Votos")
plt.show()