import numpy as np
import matplotlib.pyplot as plt

# Pedir al usuario cuántos términos desea utilizar
cantidad = int(input("Introduce el número de términos para construir la espiral: "))

# Construcción de la serie de Fibonacci
serie_fib = [1, 1]
while len(serie_fib) < cantidad:
    serie_fib.append(sum(serie_fib[-2:]))

# Preparar ventana de visualización
figura, eje = plt.subplots(figsize=(8, 8))

# Coordenadas iniciales y orientación
centro_x, centro_y = 0, 0
direccion = 0

# Recorrer cada valor de Fibonacci para formar los arcos
for indice, radio in enumerate(serie_fib[:cantidad]):

    # Definir rango angular del cuarto de circunferencia
    angulos = np.linspace(
        np.deg2rad(direccion),
        np.deg2rad(direccion + 90),
        100
    )

    # Coordenadas del arco
    x = centro_x + radio * np.cos(angulos)
    y = centro_y + radio * np.sin(angulos)

    # Graficar arco
    eje.plot(x, y, color='navy', linewidth=2)

    # Ajustar posición para el próximo arco
    if indice < cantidad - 1:
        siguiente_radio = serie_fib[indice + 1]
        nueva_direccion = np.deg2rad(direccion + 90)

        desplazamiento = radio - siguiente_radio
        centro_x += desplazamiento * np.cos(nueva_direccion)
        centro_y += desplazamiento * np.sin(nueva_direccion)

    # Rotar orientación
    direccion += 90

# Configuración visual final
eje.set_aspect('equal')
eje.set_title(f"Espiral basada en Fibonacci ({cantidad} términos)")
eje.grid(alpha=0.5, linestyle='--')

plt.show()